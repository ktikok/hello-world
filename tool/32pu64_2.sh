#!/bin/bash

for i in `echo "defaultnorm1 circpadnorm1 circpadlog3chnorm1 circpadlog5chnorm1"`
do

  source /store/hep/common/sw/anaconda3/etc/profile.d/conda.sh; conda activate pytorch; SAMPLEDIR=/store/hep/users/jhgoh/nurion4hep/20200626_1/hdf5_32PU_64x64/ python train_labelByUser.py --epoch 100 --batch 512 --lr 1e-4 --device 1 --model $i -o ~/work/result/32PU64/$i/

done
