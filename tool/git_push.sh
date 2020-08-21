#!/bin/bash
#default defaultnorm1 defaultnorm0
#"sgd adam radam ranger"
for j in `echo "defaultnorm0 defaultnorm1"`
  do
    for i in `echo "radam"`
      do

        SAMPLEDIR=/store/hep/users/jhgoh/nurion4hep/20200808_2/hdf5_32PU_224x224/ python train_labelByUser.py --epoch 50 --batch 64 --lr 1e-3 --optimizer $i --device 1 --model $j -o ~/work/result/32PU_trackpt/"$j"_"$i"/

      done
  done
