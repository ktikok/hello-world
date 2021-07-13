#!/bin/bash

for k in {5..0}
do
  for i in {-5..-1}
  do
    for j in `echo "sgd adam radam ranger"`
    do 
      d=B_$((8(*2**$k)))_L_1e`echo $i`_O_$j
      python train_torch.py --epoch 50 --batch $((8*(2**$k))) --lr 1e$i --optimizer $j -v /home/tongilkim/work/HEP-CNN/data/NERSC_preproc/noPU/val_SecAoutoRun5.h5 -t /home/tongilkim/work/HEP-CNN/data/NERSC_preproc/noPU/train_SecAoutoRun5.h5 -o /home/tongilkim/work/HEP-CNN/run/TrainnoPU/$d;
      
    done
  done
done
