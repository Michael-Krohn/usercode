from launchNtupleFromAOD import launchNtupleFromAOD

maxevents=1000
fileOutput = 'ntupleTest.root'
filesInput=[
"~/scratch/QCD_AODSIM_reHLT.root",
]
launchNtupleFromAOD(fileOutput,filesInput,maxevents)
