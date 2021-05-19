void read_cut9(){
    static constexpr Int_t kMaxEvent = 1;
   static constexpr Int_t kMaxWeight = 1180;
   static constexpr Int_t kMaxParticle = 1552;
   static constexpr Int_t kMaxTrack = 959;
   static constexpr Int_t kMaxTower = 1714;
   static constexpr Int_t kMaxGenJet = 21;
   static constexpr Int_t kMaxGenMissingET = 1;
   static constexpr Int_t kMaxJet = 24;
   //
   static constexpr Int_t kMaxElectron = 2;
   static constexpr Int_t kMaxPhoton = 2;
   static constexpr Int_t kMaxMuon = 2;
   //
   static constexpr Int_t kMaxFatJet = 13;
   static constexpr Int_t kMaxMissingET = 1;
   static constexpr Int_t kMaxScalarHT = 1;
   static constexpr Int_t kMaxRho = 3;
   static constexpr Int_t kMaxVertex = 60;
    // .L Delphes.C;
    // 저건 직접 쳐야함.
    Delphes t;

//Long64_t nentries = t.GetEntriesFast();
//cout << nentries << endl;

// Muon
// 3.141592
// int test[2][3][4] = { 
//                      { {3, 4, 2, 3}, {0, -3, 9, 11}, {23, 12, 23, 2} },
//                      { {13, 4, 56, 3}, {5, 9, 3, 5}, {5, 1, 4, 9} }
//                  };

    int height = 10; //eta
    int width = 10; //phi

    float image[3][100][100] = {0};//electron muon photon



    for (Long64_t jentry=0; jentry<10;jentry++) {


        // Electron
        for (Long64_t i=0; i<kMaxMuon;i++) {
            t.Electron_PT[i]=0;
        }
        // t.Muon_PT[0]=0;
        // t.Muon_PT[1]=0;
        t.GetEntry(jentry);
        if (t.Electron_PT[0]>0){
            cout<<"Entry num "<<jentry<<" Electron_PT [";
            for (Long64_t j=0; j<kMaxMuon-1;j++) {
                cout<<t.Electron_PT[j]<<", ";

            }
            cout<<t.Electron_PT[kMaxMuon-1]<<"]";

            cout<<" Eta"<<" [";
            for (Long64_t j=0; j<kMaxMuon-1;j++) {
                cout<<t.Electron_Eta[j]<<", ";

            }
            cout<<t.Electron_Eta[kMaxMuon-1]<<"]";
            
            cout<<" Phi"<<" [";
            for (Long64_t j=0; j<kMaxMuon-1;j++) {
                cout<<t.Electron_Phi[j]<<", ";

            }
            cout<<t.Electron_Phi[kMaxMuon-1]<<"]"<< endl;
            
            // cout<<jentry<<" ["<<t.Muon_PT[0]<<", "<<t.Muon_PT[1]<<"]"<<endl;
        }


        // muon
        for (Long64_t i=0; i<kMaxMuon;i++) {
            t.Muon_PT[i]=0;
        }
        // t.Muon_PT[0]=0;
        // t.Muon_PT[1]=0;
        t.GetEntry(jentry);
        if (t.Muon_PT[0]>0){
            cout<<"Entry num "<<jentry<<" Muon_PT [";
            for (Long64_t j=0; j<kMaxMuon-1;j++) {
                cout<<t.Muon_PT[j]<<", ";

            }
            cout<<t.Muon_PT[kMaxMuon-1]<<"]";

            cout<<" Eta"<<" [";
            for (Long64_t j=0; j<kMaxMuon-1;j++) {
                cout<<t.Muon_Eta[j]<<", ";

            }
            cout<<t.Muon_Eta[kMaxMuon-1]<<"]";
            
            cout<<" Phi"<<" [";
            for (Long64_t j=0; j<kMaxMuon-1;j++) {
                cout<<t.Muon_Phi[j]<<", ";

            }
            cout<<t.Muon_Phi[kMaxMuon-1]<<"]"<< endl;
            
            // cout<<jentry<<" ["<<t.Muon_PT[0]<<", "<<t.Muon_PT[1]<<"]"<<endl;
        }


        // Photon
        for (Long64_t i=0; i<kMaxMuon;i++) {
            t.Photon_PT[i]=0;
        }
        // t.Muon_PT[0]=0;
        // t.Muon_PT[1]=0;
        t.GetEntry(jentry);
        if (t.Photon_PT[0]>0){
            cout<<"Entry num "<<jentry<<" Photon_PT [";
            for (Long64_t j=0; j<kMaxMuon-1;j++) {
                cout<<t.Photon_PT[j]<<", ";

            }
            cout<<t.Photon_PT[kMaxMuon-1]<<"]";

            cout<<" Eta"<<" [";
            for (Long64_t j=0; j<kMaxMuon-1;j++) {
                cout<<t.Photon_Eta[j]<<", ";

            }
            cout<<t.Photon_Eta[kMaxMuon-1]<<"]";
            
            cout<<" Phi"<<" [";
            for (Long64_t j=0; j<kMaxMuon-1;j++) {
                cout<<t.Photon_Phi[j]<<", ";

            }
            cout<<t.Photon_Phi[kMaxMuon-1]<<"]"<< endl;
            
            // cout<<jentry<<" ["<<t.Muon_PT[0]<<", "<<t.Muon_PT[1]<<"]"<<endl;
        }
        
    }

// // FatJet
//     for (Long64_t jentry=0; jentry<20;jentry++) {
//         for (int i=0; i<kMaxFatJet;i++) {
//             t.FatJet_PT[i]=0;
//         }
//         // t.Muon_PT[0]=0;
//         // t.Muon_PT[1]=0;
//         t.GetEntry(jentry);

//         cout<<"Entry num "<<jentry<<" [";
//         for (int j=0; j<kMaxFatJet-1;j++) {
//             if (t.FatJet_PT[j]>1000){
//                 cout<<t.FatJet_PT[j]<<", ";
//             }
//             else{
//                 cout<< 0 <<", ";
//             }
//         }    
//         cout<<t.FatJet_PT[kMaxFatJet-1]<<"]"<< endl;
//         // cout<<jentry<<" ["<<t.Muon_PT[0]<<", "<<t.Muon_PT[1]<<"]"<<endl;

        
        

//     }

 
 // Fill t data members with entry number 12



//t.Show();       // Show values of entry 12

//t.Show(16);     // Read and show values of entry 16
//t.Loop();  
}