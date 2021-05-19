void read_cut8(){
    
    static constexpr Int_t kMaxMuon = 2;

    TFile f("RPV_1400-1.root");
    TTree* t; f.GetObject("Delphes", t);

    struct Muon_STRUCT{
        UInt_t          Muon_fUniqueID[kMaxMuon];   //[Muon_]
        UInt_t          Muon_fBits[kMaxMuon];   //[Muon_]
        Float_t         Muon_PT[kMaxMuon];   //[Muon_]
        Float_t         Muon_Eta[kMaxMuon];   //[Muon_]
        Float_t         Muon_Phi[kMaxMuon];   //[Muon_]
        Float_t         Muon_T[kMaxMuon];   //[Muon_]
        Int_t           Muon_Charge[kMaxMuon];   //[Muon_]
        TRef            Muon_Particle[kMaxMuon];
        Float_t         Muon_IsolationVar[kMaxMuon];   //[Muon_]
        Float_t         Muon_IsolationVarRhoCorr[kMaxMuon];   //[Muon_]
        Float_t         Muon_SumPtCharged[kMaxMuon];   //[Muon_]
        Float_t         Muon_SumPtNeutral[kMaxMuon];   //[Muon_]
        Float_t         Muon_SumPtChargedPU[kMaxMuon];   //[Muon_]
        Float_t         Muon_SumPt[kMaxMuon];   //[Muon_]
        Int_t           Muon_size;
        // Float_t Muon_PT[2];
    };

    Muon_STRUCT sParticle;

    TBranch* tb = t->GetBranch("Muon");
    tb->SetAddress(&sParticle); 

    int nEntries = t->GetEntries(); 
    for (Int_t i=0; i<nEntries; i++) {
        
        //sParticle.Muon_PT[0] = 0;
        // sParticle.Muon_PT[1] = 0;
        
        t->GetEntry(0);
        cout << sParticle.Muon_fUniqueID[0] << " and " << sParticle.Muon_fUniqueID[1] << endl;
        cout << sParticle.Muon_fBits[0] << " and " << sParticle.Muon_fBits[1] << endl;
        cout << sParticle.Muon_PT[0] << " and " << sParticle.Muon_PT[1] << endl;
        cout << sParticle.Muon_Eta[0] << " and " << sParticle.Muon_Eta[1] << endl;
        cout << sParticle.Muon_Phi[0] << " and " << sParticle.Muon_Phi[1] << endl;
        cout << sParticle.Muon_T[0] << " and " << sParticle.Muon_T[1] << endl;
        cout << sParticle.Muon_Charge[0] << " and " << sParticle.Muon_Charge[1] << endl;
    }
}