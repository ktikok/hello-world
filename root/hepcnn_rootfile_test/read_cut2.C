
#include <iostream>
#include <iomanip>
#include <cmath>
#include <fstream>
#include <vector>
#include <cstring>

/****** Include the required ROOT Classes *****/
#include "TFile.h"
#include "TTree.h"
#include "TF1.h"
#include "TH1.h"
#include "TStyle.h"
#include "TPad.h"
#include "TCanvas.h"
#include "TGraphErrors.h"
#include "TPostScript.h"
#include "TLatex.h"
#include "TGaxis.h"
#include "TAxis.h"

#include "Delphes.h"		// Structure of current root file

using namespace std;

int main() {

  TFile *fileIn = new TFile("RPV_1400-1.root","READ");
  TTree *treeIn = (TTree*)fileIn->Get("Delphes"); // creating a pointer of the current TTree
  Delphes *event = new testTree(Delphes);	   // creating a pointer of testTree to read data
  event->Loop();				   // Looping over all data entries

  int nentries = int(treeIn->GetEntries()); // Getting number of entries in the tree

  const int vPoints = 11;
  double v_voltage[vPoints];
  vector<double> v_current[vPoints];
  for(int ij=0;ij<vPoints;ij++) {v_current[ij].clear();}

  for(int ij=0;ij<nentries;ij++) {

    fileIn->cd();		// Calling the current file
    event->GetEntry(ij);	// Prepare the entry for reading
    
    for(int jk=0;jk<vPoints;jk++) {
      if(ij == 0) {
	v_voltage[jk] = event->reading[jk]; // Reading voltage
      } else {
	v_current[int(2.*v_voltage[jk])].push_back(event->reading[jk]); // Reading current
      }
    }
  }

}