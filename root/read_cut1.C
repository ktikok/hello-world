 
#ifndef CLONESA_EVENT_SECOND_RUN
 
void clonesA_Event() {
   std::string s1(__FILE__);
   TString dir = gSystem->UnixPathName(s1.substr(0, s1.find_last_of("\\/")).c_str());
   gROOT->ProcessLine(TString(".L ")+dir+"/clonesA_Event.cxx+");
#define CLONESA_EVENT_SECOND_RUN yes
   gROOT->ProcessLine("#include \"" __FILE__ "\"");
   gROOT->ProcessLine("clonesA_Event(true)");
}
 
#else
void read_cut(){
   //read the Tree
   TFile * hfile = new TFile("RPV_1400-1.root");
   TTree *tree = (TTree*)hfile->Get("FatJet.PT");
 
   TUsrSevtData1 * event1 = 0;
   
   tree->SetBranchAddress("top1",&event1);

   for (Int_t ev = 0; ev < 8; ev++) {
      tree->Show(ev);
      cout << "Pileup event1: " <<  event1->GetPileup() << endl;

      event1->Clear();

 //     gObjectTable->Print();          // detect possible memory leaks
   }
   delete hfile;
  
 

}

}
 
void clonesA_Event(bool /*secondrun*/) {
   // Embedding this load inside the first run of the script is not yet
   // supported in v6
   //   gROOT->ProcessLine(".L clonesA_Event.cxx+");  // compile shared lib

   clonesA_Event_r();                            // read back the tree
}
 
#endif