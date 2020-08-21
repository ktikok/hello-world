#!/usr/bin/env python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import argparse
import csv
import math

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', action='store', type=str, required=True, help='directory with prediction csv files')
parser.add_argument('-o', '--output', action='store', type=str, required=True, help='directory to store plots')
parser.add_argument('-a', '--annotate', action='store', type=bool, default=False, help='turn on annotation on figure')
args = parser.parse_args()

predFile = args.input+'/prediction.csv'
signFile = args.output+'/significance.csv'
df = pd.read_csv(predFile)
df_bkg = df[df.label==0]
df_sig = df[df.label==1]
signif, sig, bkg, thr = [], [], [], []

for i in range(0,101):
    thr.extend([round(i*0.01,3)])
    sig.extend([df_sig[df_sig.prediction >= (i*0.01)].weight.sum()])
    bkg.extend([df_bkg[df_bkg.prediction >= (i*0.01)].weight.sum()])
    signif.extend([sig[i]/math.sqrt(sig[i]+bkg[i])])

df_signif = pd.DataFrame({'Threshold':thr,'Signal':sig,'Background':bkg, 'Significance':signif})
df_signif.to_csv(signFile, index=False)


plt.plot(thr,signif, label='Signif')

if args.annotate == True:
    ymax=max(signif)
    xmax=thr[signif.index(ymax)]
    plt.plot(xmax, ymax, 'o', label='Max_signif')
    plt.annotate('thr={}\nsignif={}'.format(xmax,round(ymax,5)), xy=(0.03,0.7),xycoords='axes fraction',bbox=dict(boxstyle="round",fc="w", alpha=0.3))

plt.ylabel("Significance")
plt.xlabel("Threshold")
plt.title("signif VS thr %s" %(args.input))
plt.legend()
plt.savefig(args.output+"/Signif_VS_Thr.png")
plt.show()
