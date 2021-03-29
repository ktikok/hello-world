void read_cut6(){
  gROOT->Reset();

  TFile  myFile("RPV_1400-1.root"); // Open the file
  TTree* myTree = (TTree*) myFile.Get("Delphes"); // Get the Muon tree from the file

  // Preparing the containers to be filled with data from the tree:
//   int              muon_nParticle; // Number of muons in an entry

//   vector<double>*  muon_pt;        // An array of the pT values for each of the muons
//   vector<double>*  muon_eta;       // An array of the eta vlues for each of the muons
    vector<Float_t>*  FatJet_PT;       // An array of the phi vlues for each of the muons

  // Linking the local variables to the tree branches

//   myTree->SetBranchAddress("muon_nParticle", &muon_nParticle);
//   myTree->SetBranchAddress("muon_pt",        &muon_pt);
//   myTree->SetBranchAddress("muon_eta",       &muon_eta);
   myTree->SetBranchAddress("FatJet.PT",       &FatJet_PT);
  // After this stage the local variables are still empty.

  // With every subsequent call to myTree->GetEntry(i) the local variables
  // will be filled with the content of branches

  // Create a histogram with 100 bins between 0-100000 to be filled later:
 // gROOT->cd(0); // This tells ROOT to create next object in memory and not in file

  // Loop over all entries in the tree
  //   for each entry, print the pt values and fill them to a histogram
  int nEntries = myTree->GetEntries(); // Get the number of entries in this tree
  for (int iEnt = 0; iEnt < nEntries; iEnt++) {
    myTree->GetEntry(iEnt); // Gets the next entry (filling the linked variables)


    cout<<"Entry #"<< iEnt << endl;
    for (int iPar = 0; iPar < nEntries; iPar++) {
      cout<<"    FatJet_PT["<< iPar <<"] = "<< FatJet_PT ->at(iPar) << endl;

    }
  }

  
  myFile.Close(); // Close file
}