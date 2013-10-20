#! /usr/bin/env python

"""
a wrapper for hadd which recalculate TProfile efficiencies in validation
files

"""
__author__ =  'Igor Marfin'
__version__=  '0.1'
__nonsense__ = 'HiggsGroup'

import time
import os
import sys
import commands
import re
from optparse import OptionParser
import math
import os.path

parser=OptionParser(usage="""

        usage: %prog  [options] file.root file1.root file2.root

        An example of the run:  
   
       ./%prog DQM_V0001_R000000001__CMSSW_5_3_11_8TeV__RelVal__TrigVal.root  `find ./ -iname "*CMSSW_5_3_11_8TeV*root" | grep crab`
  
        The current OP for pt-turn on is MEDIUM.
        You can specify a new value using --minTag option, here for example, TCHP6 point
 
       ./%prog --minTag=6 DQM_V0001_R000000001__CMSSW_5_3_11_8TeV__RelVal__TrigVal.root  `find ./ -iname "*CMSSW_5_3_11_8TeV*root" | grep crab`

"""
)





HLTPathName="HLT_DiJet40Eta2p6_BTagIP3DFastPV"
CMSSWVER="CMSSW_X_Y_Z"
DQMPATH="DQMData/Run 1/HLT/Run summary/BTag/"



parser.add_option("--minTag",dest="minTag",default="3.41",type="float",action="store")
(options,args)=parser.parse_args()


if len(args)<1 :
 parser.print_usage()
 raise SystemExit



try:
 cmssw =os.environ["CMSSW_BASE"]
 print cmssw

except KeyError:
 print "Please ini CMSSW"
 print "We neend CMSSW for properly running the program!"
 sys.exit(1)


sys.argv.append('-b-')
import ROOT
ROOT.gROOT.SetBatch(True)
sys.argv.remove('-b-')


from HLTriggerOffline.Btag.Validation.helper import *


# set up variables
try:
 Config.read("my.ini")
 HLTPathName=ConfigSectionMap("l25")["hltpathname"]
 CMSSWVER=ConfigSectionMap("l25")["cmsswver"]
except:
 print "Something wrong with ini"
 sys.exit(1)


# possible flavors:
flavors=[
'b',
'c',
'g',
'uds',
'light'
]


# minTag is cut-off of btagging discriminant. It helps to calculate the pT turn-on.
#minTag=3.41 # TCHP , 6 -- TCH6
minTag=options.minTag
maxTag=100.

minPt=0.
maxPt=350.


DQMPATH+=HLTPathName+"/"
DQMEFFPATH=DQMPATH+"efficiency/"



print DQMPATH
print DQMEFFPATH
print CMSSWVER



def calculateEfficiency1D( num, den, eff ):
 if (eff==None): 
  print "Problems with efficiency object"
  return
#Check version of the root
 cmd = "$ROOTSYS/bin/root-config --version"
 ver=commands.getoutput(cmd)
 ver=ver.split("/")
 version=float(ver[0])
 for i in range(1,num.GetNbinsX()+1):
  e=0.
  low=0.
  high=0.
  err=0.
  if version>5.27:
   if int(den.GetBinContent(i))>0. : e=float(num.GetBinContent(i))/float(den.GetBinContent(i))  
   low=ROOT.TEfficiency.Wilson(int(den.GetBinContent(i)),int(num.GetBinContent(i)),0.683,False);
   high=ROOT.TEfficiency.Wilson(int(den.GetBinContent(i)),int(num.GetBinContent(i)),0.683,True);
  else:
   ROOT.Efficiency(num.GetBinContent(i), den.GetBinContent(i), 0.683, e, low, high )

  if (e-low>high-e): err = e-low
  else: err= high-e
  #here is the trick to store info in TProfile:
  eff.SetBinContent( i, e );
  eff.SetBinEntries( i, 1 );
  eff.SetBinError( i, math.sqrt(e*e+err*err) );
  #eff.SetBinError( i, err );

 return eff


def mistagrate(  num,  den, eff ):

 if (eff==None):
  print "Problems with mistagrate object"
  return
 
  for i in range(1,num.GetNbinsX()+1):
   beff=num.GetBinContent(i);
   miseff=den.GetBinContent(i);
   miseffErr=den.GetBinError(i);
   binX = eff.GetXaxis().FindBin(beff);
   if (eff.GetBinEntries(binX)!=0): continue
   eff.SetBinContent(binX,miseff);
   eff.SetBinError(binX,miseffErr);
   eff.SetBinEntries( binX, 1 );

 return eff




def GetNumDenumerators(file,num,den,type):

 if (file==None): 
  print "file "+ file+ "is non-readable"
  return

 if type==0:
  numH1 = file.Get(num);
  denH1 = file.Get(den);
  if (numH1==None or denH1==None): return
  ptrden=denH1.Clone("denominator");
  ptrnum=numH1.Clone("numerator");
  ptrnum.SetBinContent(1,numH1.Integral());
  ptrden.SetBinContent(1,numH1.Integral());
  for j in range(2,numH1.GetNbinsX()+1):
         ptrnum.SetBinContent(j,numH1.Integral()-numH1.Integral(1,j-1));
         ptrden.SetBinContent(j,numH1.Integral());


 if type==1:
  numH2 = file.Get(num);
  denH2 = file.Get(den);
  if (numH2==None or denH2==None): return
  cutg_num= ROOT.TCutG("cutg_num",4);
  cutg_num.SetPoint(0,minTag,minPt);
  cutg_num.SetPoint(1,minTag,maxPt);
  cutg_num.SetPoint(2,maxTag,maxPt);
  cutg_num.SetPoint(3,maxTag,minPt);
  ptrnum = numH2.ProjectionY("numerator",0,-1,"[cutg_num]");

  cutg_den= ROOT.TCutG("cutg_den",4);
  cutg_den.SetPoint(0,-1000.,minPt);
  cutg_den.SetPoint(1,-1000.,maxPt);
  cutg_den.SetPoint(2,1000.,maxPt);
  cutg_den.SetPoint(3,1000.,minPt);
  ptrden = denH2.ProjectionY("denumerator",0,-1,"[cutg_den]");


        
 return (ptrnum, ptrden)


def Rewrite(file, path,object):
 if (file==None): 
  print "file "+ file+" is non-writable"
  return
 file.cd(path)
 object.Write("",ROOT.TObject.kOverwrite)
 return
 



if  __name__ == '__main__':
 """ main subroutine """


# hadd
 cmd = "hadd -f "
 for arg in  args: cmd+=" " + arg
 print cmd
 os.system(cmd)


 outputfile=""
 for arg in args:
  match=re.search(r'.*.root',arg)
  if match:
   outputfile=arg
   break

 file=ROOT.TFile(outputfile,"UPDATE")
 if (file==None):
  print outputfile+" can't be opened!"
  sys.exit(1)

# try to fix eff vs discr 
 effL25={}
 effL3={}

 for flavor in flavors:
# L25
  label="JetTag_L25_";
  label+=flavor;

  num,den=GetNumDenumerators(file,DQMPATH+label,DQMPATH+label,0)
  eff=file.Get(DQMEFFPATH+label+"_efficiency_vs_disc")
  
  if (num!=None and den!=None and eff!=None):  eff=calculateEfficiency1D(num,den,eff) 
  if (eff!=None): Rewrite(file,DQMEFFPATH,eff)

  effL25.update({flavor:eff})

  num,den= GetNumDenumerators (file,DQMPATH+label+"_disc_pT",DQMPATH+label+"_disc_pT",1)
  eff=file.Get(DQMEFFPATH+label+"_disc_pT"+"_efficiency_vs_pT")

  if (num!=None and den!=None and eff!=None):  eff=calculateEfficiency1D(num,den,eff)
  if (eff!=None): Rewrite(file,DQMEFFPATH,eff)
  

# L3
 
  label="JetTag_L3_";
  label+=flavor

  num,den=GetNumDenumerators(file,DQMPATH+label,DQMPATH+label,0)
  eff=file.Get(DQMEFFPATH+label+"_efficiency_vs_disc")
  
  if (num!=None and den!=None and eff!=None):  eff=calculateEfficiency1D(num,den,eff)
  if (eff!=None): Rewrite(file,DQMEFFPATH,eff)

  effL3.update({flavor:eff})

  num,den= GetNumDenumerators (file,DQMPATH+label+"_disc_pT",DQMPATH+label+"_disc_pT",1)
  eff=file.Get(DQMEFFPATH+label+"_disc_pT"+"_efficiency_vs_pT")

  if (num!=None and den!=None and eff!=None):  eff=calculateEfficiency1D(num,den,eff)
  if (eff!=None): Rewrite(file,DQMEFFPATH,eff)


# mistag rates

# L25
 eff=file.Get(DQMEFFPATH+"L25_b_c_mistagrate")
 if (eff!=None): 
  eff=mistagrate(effL25["b"], effL25["c"], eff);
  Rewrite(file,DQMEFFPATH,eff)

 eff=file.Get(DQMEFFPATH+"L25_b_light_mistagrate")
 if (eff!=None): 
  eff=mistagrate(effL25["b"], effL25["light"], eff);
  Rewrite(file,DQMEFFPATH,eff)

 eff=file.Get(DQMEFFPATH+"L25_b_g_mistagrate")
 if (eff!=None): 
  eff=mistagrate(effL25["b"], effL25["g"], eff);
  Rewrite(file,DQMEFFPATH,eff)

# L3
 eff=file.Get(DQMEFFPATH+"L3_b_c_mistagrate")
 if (eff!=None): 
  eff=mistagrate(effL3["b"], effL3["c"], eff);
  Rewrite(file,DQMEFFPATH,eff)

 eff=file.Get(DQMEFFPATH+"L3_b_light_mistagrate")
 if (eff!=None): 
  eff=mistagrate(effL3["b"], effL3["light"], eff);
  Rewrite(file,DQMEFFPATH,eff)

 eff=file.Get(DQMEFFPATH+"L3_b_g_mistagrate")
 if (eff!=None): 
  eff=mistagrate(effL3["b"], effL3["g"], eff);
  Rewrite(file,DQMEFFPATH,eff)

# End
 file.Close()
