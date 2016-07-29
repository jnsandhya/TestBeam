import FWCore.ParameterSet.Config as cms

process = cms.Process("unpack")
process.load('HGCal.RawToDigi.hgcaltbdigis_cfi')
process.load('HGCal.RawToDigi.hgcaltbdigisplotter_cfi')
process.load('HGCal.Reco.hgcaltbrechitproducer_cfi')
process.load('HGCal.Reco.hgcaltbrechitplotter_cfi')

process.source = cms.Source("HGCalTBTextSource",
                            run=cms.untracked.int32(1), ### maybe this should be read from the file
#                            fileNames=cms.untracked.vstring("file:Raw_data_New.txt") ### here a vector is provided, but in the .cc only the first one is used TO BE FIXED
                            fileNames=cms.untracked.vstring("file:/afs/cern.ch/user/r/rchatter/public/data/HGC_Output_563.txt") ### here a vector is provided, but in the .cc only the first one is used TO BE FIXED
)

process.dumpRaw = cms.EDAnalyzer("DumpFEDRawDataProduct",
                              dumpPayload=cms.untracked.bool(True))

process.dumpDigi = cms.EDAnalyzer("HGCalDigiDump")

process.output = cms.OutputModule("PoolOutputModule",
                                  compressionAlgorithm = cms.untracked.string('LZMA'),
                                  compressionLevel = cms.untracked.int32(4),
                                  dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('USER'),
        filterName = cms.untracked.string('')
        ),
                                  #dropMetaData = cms.untracked.string('ALL'),
                                  eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
                                 fastCloning = cms.untracked.bool(False),
                                 fileName = cms.untracked.string('test_output.root'), #options.output),
#                                 outputCommands = process.MICROAODSIMEventContent.outputCommands,
#                                 overrideInputFileSplitLevels = cms.untracked.bool(True),
#                                 SelectEvents = SelectEventsPSet
                                 )

#process.TFileService = cms.Service("TFileService", fileName = cms.string("HGC_Output_563_Reco_Display.root") )
#process.TFileService = cms.Service("TFileService", fileName = cms.string("HGC_Output_563_Digi.root") )
process.TFileService = cms.Service("TFileService", fileName = cms.string("HGC_Output_563_Reco.root") )
#process.TFileService = cms.Service("TFileService", fileName = cms.string("HGC_Output_563_Reco_Layer.root") )
#process.TFileService = cms.Service("TFileService", fileName = cms.string("HGC_Output_563_Reco_Cluster.root") )


#process.p =cms.Path(process.hgcaltbdigis*process.hgcaltbrechits*process.hgcaltbrechitsplotter_highgain_new)
#process.p =cms.Path(process.hgcaltbdigis*process.hgcaltbdigisplotter)
process.p =cms.Path(process.hgcaltbdigis*process.hgcaltbrechits*process.hgcaltbrechitsplotter_highgain_correlation_cm)
#process.p =cms.Path(process.hgcaltbdigis*process.hgcaltbrechits*process.FourLayerRecHitPlotterMax)
#process.p =cms.Path(process.hgcaltbdigis*process.hgcaltbrechits*process.LayerSumAnalyzer)
process.end = cms.EndPath(process.output)
