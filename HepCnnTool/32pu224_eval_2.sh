#!/bin/bash

#for i in `echo "defaultnorm1 circpadnorm1 circpadlog3chnorm1 circpadlog5chnorm1"`
for i in `ls ~/work/result/32PU224/E100B64L4adam/`
do
  echo start : $i
  source /store/hep/common/sw/anaconda3/etc/profile.d/conda.sh; conda activate pytorch; SAMPLEDIR=/store/hep/users/jhgoh/nurion4hep/20200626_1/hdf5_32PU_224x224/ python eval_torch.py --batch 128 -d ~/work/result/32PU224/E100B64L4adam/$i/ --output ~/work/result/graphs/0716_0723/$i

done
