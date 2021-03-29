{
  gROOT->Reset();

  TFile  myFile("RPV_1400-1.root"); // Open the file
  TTree* myTree = (TTree*) myFile.Get("Delphes"); // Get the Muon tree from the file

  // Preparing the containers to be filled with data from the tree:
  int              muon_nParticle; // Number of muons in an entry

  Float_t  muon_pt[2] = {0};        // An array of the pT values for each of the muons
  Float_t  muon_eta[2];       // An array of the eta vlues for each of the muons
  Float_t  muon_phi[2];       // An array of the phi vlues for each of the muons

  // Linking the local variables to the tree branches

  myTree->SetBranchAddress("Muon_size", &muon_nParticle);
  myTree->SetBranchAddress("Muon.PT",        &muon_pt);
  myTree->SetBranchAddress("Muon.Eta",       &muon_eta);
  myTree->SetBranchAddress("Muon.Phi",       &muon_phi);
  // After this stage the local variables are still empty.

  // With every subsequent call to myTree->GetEntry(i) the local variables
  // will be filled with the content of branches

  // Create a histogram with 100 bins between 0-100000 to be filled later:
  gROOT->cd(0); // This tells ROOT to create next object in memory and not in file
  TH1D h("h_muon_pt", "Muon P_{T} histogram",20, 0, 20000);
  gStyle->SetOptStat(111111); // Tells ROOT to list histogram overflow/underflow

  
  // Loop over all entries in the tree
  //   for each entry, print the pt values and fill them to a histogram
  int nEntries = myTree->GetEntries(); // Get the number of entries in this tree
  for (int iEnt = 0; iEnt < nEntries; iEnt++) {
    myTree->GetEntry(iEnt); // Gets the next entry (filling the linked variables)


    cout<<"Entry #"<< iEnt ;
    for (int iPar = 0; iPar < muon_nParticle; iPar++) {
      //cout<<"    muon_pt["<< iPar <<"] = "<< muon_pt->at(iPar) << endl;
      cout<<"\n";
      cout<<"    muon_pt["<< iPar <<"] = "<< muon_pt << endl;
    //  h.Fill(muon_pt->at(iPar));
    }
  }
  //h.Draw(); // Draw histogram

  
  myFile.Close(); // Close file
}