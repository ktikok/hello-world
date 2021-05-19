void setStyle(){
    gROOT->SetStyle("Plain");
    gStyle->SetOptStat(111110);
    gStyle->SetOptFit(111);
    gStyle->SetOptTitle(1);
}

void grafico(){
    TGraphErrors * graphC =new TGraphErrors("youtube.txt", "%lg%lg");
    graphC->SetTitle("Energy Resolution; 1/root(E); sigma/E");
    //graphC->SetMarkerStyle()

    TF1 *f1 = new TF1("Linear law", "[0]+x*[1]", 0.05, 0.5);
    f1->SetParNames("C:");
    graphC->Fit(f1);

    TCanvas *cC = new TCanvas();
    cC -> cd();
    graphC->Draw("APE");

    // run root
    // .L youtube.root
    // setStyle()
    // grafico()
}