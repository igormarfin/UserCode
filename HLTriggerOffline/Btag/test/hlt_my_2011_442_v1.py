# Auto generated configuration file
# using: 
# Revision: 1.341 
# Source: /cvs/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: step.py --step=DIGI,L1,DIGI2RAW,HLT:GRun -n 5 --eventcontent HLTDEBUG --conditions auto:startup --mc --fileout output.root --no_exec --python_filename hlt_my_2011_442_v1.py --datamix NODATAMIXER --datatier GEN-SIM-RAW --filein=/store/relval/CMSSW_4_4_2_patch8/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/PU_START44_V11_17Jul2013-v1/00000/A4426B2F-ECEE-E211-8A03-0025905938AA.root --processName HLTX
import FWCore.ParameterSet.Config as cms

process = cms.Process('HLTX')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_GRun_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(30)
)

# Input source
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 


process.source = cms.Source("PoolSource",
#    secondaryFileNames = cms.untracked.vstring(
#'/store/relval/CMSSW_4_4_2_patch8/RelValTTbar/GEN-SIM-RECO/START44_V11_17Jul2013-v1/00000/86D60F52-FAEE-E211-9995-003048FFCB74.root',
#'/store/relval/CMSSW_4_4_2_patch8/RelValTTbar/GEN-SIM-RECO/START44_V11_17Jul2013-v1/00000/AA7691EC-00EF-E211-AEE6-003048FFCB8C.root',
#'/store/relval/CMSSW_4_4_2_patch8/RelValTTbar/GEN-SIM-RECO/START44_V11_17Jul2013-v1/00000/AE278836-06EF-E211-898E-00261894387C.root'
#),


#    fileNames = cms.untracked.vstring(
#'/store/relval/CMSSW_4_4_2_patch8/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/PU_START44_V11_17Jul2013-v1/00000/A4426B2F-ECEE-E211-8A03-0025905938AA.root',
#'/store/relval/CMSSW_4_4_2_patch8/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V11_17Jul2013-v1/00000/188D3814-F4EE-E211-9AFA-003048FFD76E.root',
#'/store/relval/CMSSW_4_4_2_patch8/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V11_17Jul2013-v1/00000/284662D9-EBEE-E211-92A9-00261894389C.root',
#'/store/relval/CMSSW_4_4_2_patch8/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V11_17Jul2013-v1/00000/30CEDA88-EDEE-E211-BDF2-0025905964B2.root',
#'/store/relval/CMSSW_4_4_2_patch8/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V11_17Jul2013-v1/00000/7EB8FCCB-EBEE-E211-83E9-00261894398A.root',
#'/store/relval/CMSSW_4_4_2_patch8/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V11_17Jul2013-v1/00000/80AD8F87-F1EE-E211-9562-002590593902.root',
#'store/relval/CMSSW_4_4_2_patch8/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V11_17Jul2013-v1/00000/C4DC1981-EBEE-E211-AD3B-002590596486.root'
#)
fileNames = readFiles, secondaryFileNames = secFiles
)

readFiles.extend( [
       '/store/relval/CMSSW_4_4_2_patch8/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V11_17Jul2013-v1/00000/188D3814-F4EE-E211-9AFA-003048FFD76E.root',
       '/store/relval/CMSSW_4_4_2_patch8/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V11_17Jul2013-v1/00000/284662D9-EBEE-E211-92A9-00261894389C.root',
       '/store/relval/CMSSW_4_4_2_patch8/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V11_17Jul2013-v1/00000/30CEDA88-EDEE-E211-BDF2-0025905964B2.root',
       '/store/relval/CMSSW_4_4_2_patch8/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V11_17Jul2013-v1/00000/7EB8FCCB-EBEE-E211-83E9-00261894398A.root',
       '/store/relval/CMSSW_4_4_2_patch8/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V11_17Jul2013-v1/00000/80AD8F87-F1EE-E211-9562-002590593902.root',
       '/store/relval/CMSSW_4_4_2_patch8/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/START44_V11_17Jul2013-v1/00000/C4DC1981-EBEE-E211-AD3B-002590596486.root' ] )




secFiles.extend( [
'/store/relval/CMSSW_4_4_2_patch8/RelValTTbar/GEN-SIM-RECO/START44_V11_17Jul2013-v1/00000/86D60F52-FAEE-E211-9995-003048FFCB74.root',
       '/store/relval/CMSSW_4_4_2_patch8/RelValTTbar/GEN-SIM-RECO/START44_V11_17Jul2013-v1/00000/AA7691EC-00EF-E211-AEE6-003048FFCB8C.root',
       '/store/relval/CMSSW_4_4_2_patch8/RelValTTbar/GEN-SIM-RECO/START44_V11_17Jul2013-v1/00000/AE278836-06EF-E211-898E-00261894387C.root' ] )





process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.341 $'),
    annotation = cms.untracked.string('step.py nevts:5'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition


#  Keep genParticles to perform matching with HLT jets
from Configuration.EventContent.EventContent_cff import *
process.HLTDEBUGEventContent.outputCommands.extend(   cms.untracked.vstring(  'keep *_genParticles_*_*',      'keep *_genParticlesForJets_*_*') )

# offline btagging 
from RecoBTag.Configuration.RecoBTag_EventContent_cff import *
process.HLTDEBUGEventContent.outputCommands.extend(RecoBTagFEVT.outputCommands)



process.HLTDEBUGoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.HLTDEBUGEventContent.outputCommands,
    fileName = cms.untracked.string('output.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM-RAW')
    )
)

# Additional output definition

# Other statements
process.GlobalTag.globaltag = 'START44_V11::All'

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.HLTDEBUGoutput_step = cms.EndPath(process.HLTDEBUGoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.HLTDEBUGoutput_step])

