#!/bin/bash
# circpadnorm1 circpadlog3chnorm1 circpadlog5chnorm1 circpadlog3ch circpadlog5ch circpad circpadlog5ch
for i in `echo "circpadlog3ch"`
do

  source /store/hep/common/sw/anaconda3/etc/profile.d/conda.sh; conda activate pytorch; SAMPLEDIR=/store/hep/users/jhgoh/nurion4hep/20200626_1/hdf5_32PU_224x224/ python train_labelByUser.py --epoch 100 --batch 64 --lr 1e-4 --optimizer adam --device 2 --model $i -o ~/work/result/32PU224/E100B64L4adam$i/

done