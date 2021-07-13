#!/bin/bash

#for i in `echo "defaultnorm1 circpadnorm1 circpadlog3chnorm1 circpadlog5chnorm1"`
for i in `ls ~/work/result/32PU64/`
do
  echo start : $i
  source /store/hep/common/sw/anaconda3/etc/profile.d/conda.sh; conda activate pytorch; SAMPLEDIR=/store/hep/users/jhgoh/nurion4hep/20200626_1/hdf5_32PU_64x64/ python eval_torch.py --batch 512 -d ~/work/result/32PU64/$i/ --output ~/work/result/graphs/0709_0716/$i

done
