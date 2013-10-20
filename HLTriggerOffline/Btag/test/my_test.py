# Auto generated configuration file
# using: 
# Revision: 1.341 
# Source: /cvs/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: TTbar_8TeV_cfi.py --step=DIGI,L1,DIGI2RAW,HLT:GRun,RAW2DIGI,L1Reco,RECO -n 10 --eventcontent FEVTDEBUGHLT --conditions auto:startup --mc --fileout output.root --no_exec --python_filename my_test.py --datamix NODATAMIXER --datatier AODSIM --processName=HLTX --pileup E8TeV_ProbDist_2011EarlyData_50ns
import FWCore.ParameterSet.Config as cms

process = cms.Process('HLTX')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_E8TeV_ProbDist_2011EarlyData_50ns_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_GRun_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)



# Input source
#process.source = cms.Source("PoolSource",
#    secondaryFileNames = cms.untracked.vstring(),
#    fileNames = cms.untracked.vstring('file:TTbar_8TeV_cfi.py_SIM.root')
#)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.341 $'),
    annotation = cms.untracked.string('TTbar_8TeV_cfi.py nevts:10'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition


#  Keep genParticles to perform matching with HLT jets
from Configuration.EventContent.EventContent_cff import *
process.FEVTDEBUGHLTEventContent.outputCommands.extend(   cms.untracked.vstring(  'keep *_genParticles_*_*',      'keep *_genParticlesForJets_*_*') )

# offline btagging 
from RecoBTag.Configuration.RecoBTag_EventContent_cff import *
process.FEVTDEBUGHLTEventContent.outputCommands.extend(RecoBTagFEVT.outputCommands)


process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    fileName = cms.untracked.string('output.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('AODSIM')
    )
)

# Additional output definition

# Other statements
process.GlobalTag.globaltag = 'START44_V7::All'

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.FEVTDEBUGHLToutput_step])

