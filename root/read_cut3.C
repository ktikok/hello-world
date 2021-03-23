void read_cut3(){
	TFile *f = TFile::Open("RPV_1400-1.root","read");
	//TFile f("RPV_1400-1.root");
	
  TTree *Delphes = (TTree*)(f->Get("Delphes"));
  //TTree* Delphes; f.GetObject("Delphes",Delphes);
  
  //Float_t FatJet_PT;
  //Float_t FatJet_PT[5990] = {0};
  Float_t FatJet_PT[13] = {0};
  
  
  Delphes->SetBranchAddress("FatJet_PT", &FatJet_PT);
  //Delphes->SetBranchAddress("FatJet.Mass", &Mass[FatJet_]);
  
  Int_t NumOfEntries = Delphes->GetEntries();
  for (int i=0; i<NumOfEntries; i++){
    
    Delphes->GetEntry(i);
    //Delphes->Show(i);
    
    //if (FatJet_PT > 30){
    if (i%1000 ==0){
      for (int j=0; j<13; j++){
        //if (FatJet_PT[0] != 0){
          std::cout << j << " th " << FatJet_PT[j] << std::endl;
        //}
      
      //break;
      }
    }
  
  }
  f->Close();
  
 

}
