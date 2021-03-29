void read_cut4() {
   // check if the event class is in the dictionary
   // if it is not load the definition in libEvent.so
   
   if (!TClassTable::GetDict("Event")) {
      gSystem->Load("$ROOTSYS/test/libEvent.so");
   }
   
   // read the tree generated with tree4w

   // note that we use "new" to create the TFile and TTree objects, because we
   // want to keep these objects alive when we leave this function.
   
   // TFile *f = new TFile("tree4.root");
   
    TFile *f = new TFile("RPV_1400-1.root");
   TTree *t4 = (TTree*)f->Get("Delphes");

   // create a pointer to an event object for reading the branch values.
   Event *event = new Event();
   // get two branches and set the branch address
   
   // TBranch *bntrack = t4->GetBranch("fNtrack");
   // TBranch *branch  = t4->GetBranch("event_split");

   TBranch *bntrack = t4->GetBranch("FatJet.PT");
   TBranch *branch  = t4->GetBranch("FatJet");
   
   branch->SetAddress(&event);

   Int_t nevent = t4->GetEntries();
   Int_t nselected = 0;
   Int_t nb = 0;
   for (Int_t i=0; i<nevent; i++) {
      //read branch "fNtrack"only
      bntrack->GetEntry(i);

      // reject events with more than 587 tracks
      if (event->GetNtrack() > 587)continue;

      // read complete accepted event in memory
      nb += t4->GetEntry(i);
      nselected++;

     // print the first accepted event
     if (nselected == 1) t4->Show();
     // clear tracks array
     event->Clear();
   }

   if (gROOT->IsBatch()) return;
   new TBrowser();
   t4->StartViewer();
}