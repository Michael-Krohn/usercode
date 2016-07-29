datasets=[

#'/SingleMuon/Run2016B-PromptReco-v2/AOD',

#'/SingleElectron/Run2016B-PromptReco-v2/AOD',

#'/BTagCSV/Run2016B-PromptReco-v2/AOD',

'/JetHT/Run2016B-PromptReco-v1/AOD',
'/JetHT/Run2016B-PromptReco-v2/AOD',
'/JetHT/Run2016C-PromptReco-v2/AOD',
'/JetHT/Run2016D-PromptReco-v2/AOD',

#'/MET/Run2016B-PromptReco-v2/AOD',

#'/HLTPhysics/Run2016B-PromptReco-v2/AOD',

#'/MuonEG/Run2016B-PromptReco-v2/AOD',

#'/ZeroBias/Run2016B-PromptReco-v2/AOD',

]
if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand
    from CRABClient.UserUtilities import config
    config = config()
    
    for dataset in datasets:
        name = 'triggerNtupleAOD_FWLite_2016_v2p0'
        config.section_("General")
        config.General.workArea = 'crab_'+name
        config.General.transferLogs=True
#        config.General.requestName = name+"_"+dataset.replace('/',"_")
        config.General.requestName = name+"_"+dataset.split('/')[1]+"_"+dataset.split('/')[2]

        config.section_("JobType")
        config.JobType.pluginName = 'Analysis'
        config.JobType.psetName = 'crab_fake_pset.py'
        config.JobType.scriptExe = 'crab_script.sh'
        import os
        os.system("tar czf python.tar.gz --dereference --directory $CMSSW_BASE python")
        os.system("voms-proxy-info -path | xargs -i  cp {}  .")
        config.JobType.inputFiles = [
                                     'fwlite_config.py',
                                     'script.py',
                                     'python.tar.gz',
#                                     'x509up_u9300',
        ]
        
        config.section_("Data")
        config.Data.inputDBS = 'global'
        config.Data.splitting = 'LumiBased'
        config.Data.unitsPerJob = 50 ##FIXME: use 20

#        config.Data.totalUnits = -1
        config.Data.totalUnits = -1

#        config.Data.totalUnits = 100*config.Data.unitsPerJob ##FIXME: use -1
#        config.Data.unitsPerJob = 1 #FIXME: use 20
#        config.Data.totalUnits = 1 #FIXME: use -1
        config.Data.outLFNDirBase = '/store/user/sdonato/' + name
        config.Data.publication = True
#        config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/Cert_246908-251883_13TeV_PromptReco_Collisions15_JSON_v2.txt'
        config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/DCSOnly/json_DCSONLY.txt' 
#'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON.txt'
        config.Data.inputDataset = dataset
#        config.Data.publishDataName = config.General.requestName
        config.Data.outputDatasetTag = config.General.requestName
        config.Data.allowNonValidInputDataset = True
	config.Site.blacklist = ['T0_*']
        
        config.section_("Site")
        config.Site.storageSite = "T2_CH_CSCS"
        print "submitting ",dataset
        crabCommand('submit',config = config)
        print "DONE ",dataset
    
