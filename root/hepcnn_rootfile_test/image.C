void image(){

       //
   static constexpr Int_t kMaxElectron = 2;
   static constexpr Int_t kMaxPhoton = 2;
   static constexpr Int_t kMaxMuon = 2;
   //
    // .L Delphes.C;
    // 저건 직접 쳐야함.
    Delphes t;
    int e, p;
    int image[3][10][10] = {0};//[electron muon photon]eta,phi
    // 0 1 2 3 4 5 6 7 8 9
    
    for (Long64_t jentry=0; jentry<5990;jentry++) {


        // Electron
        for (Long64_t i=0; i<kMaxMuon;i++) {
            t.Electron_PT[i]=0;
            t.Muon_PT[i]=0;
            t.Photon_PT[i]=0;
        }
        t.GetEntry(jentry);
        for (Long64_t j=0; j<kMaxMuon-1;j++) {
            
            if (t.Electron_PT[j]>0){
                e = int((t.Electron_Eta[j]+3.141592)/(3.141592*2/10));
                p = int((t.Electron_Phi[j]+3.141592)/(3.141592*2/10));
                image[0][e][p] = image[0][e][p]+1;
            }
        }            
        
        for (Long64_t j=0; j<kMaxMuon-1;j++) {
            
            if (t.Muon_PT[j]>0){
                e = int((t.Muon_Eta[j]+3.141592)/(3.141592*2/10));
                p = int((t.Muon_Phi[j]+3.141592)/(3.141592*2/10));
                image[1][e][p] = image[1][e][p]+1;
            }
        }            
        
        for (Long64_t j=0; j<kMaxMuon-1;j++) {

            if (t.Photon_PT[j]>0){
                e = int((t.Photon_Eta[j]+3.141592)/(3.141592*2/10));
                p = int((t.Photon_Phi[j]+3.141592)/(3.141592*2/10));
                image[2][e][p] = image[2][e][p]+1;
            }
        }                
        
    }    
    for (int i=0; i<3;i++){
        cout << "0:electron, 1:muon, 2:photon, h:e, w:p <<< i = "<< i<<endl;
        for (int j=0; j<10;j++){
            for (int k=0; k<10;k++){
                printf( "%3d" , image[i][j][k] );
                //cout << image[i][j][k] << " ";
            }
            cout << "\n";
        }
        cout << "\n";

    }

}