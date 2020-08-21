#!/bin/bash
#default defaultnorm1 defaultnorm0#
for j in `echo "defaultnorm1"`
  do
    for i in `echo "sgd adam radam ranger"`
      do

        source /store/hep/common/sw/anaconda3/etc/profile.d/conda.sh; conda activate pytorch; SAMPLEDIR=/store/hep/users/jhgoh/nurion4hep/20200808_1/hdf5_32PU_224x224/ python train_labelByUser.py --epoch 50 --batch 64 --lr 1e-3 --optimizer $i --device 1 --model $j -o ~/work/result/32PU_trackpt/"$j"_"$i"/

      done
  done
