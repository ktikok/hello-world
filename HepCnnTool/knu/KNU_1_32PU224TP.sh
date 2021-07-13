#!/bin/bash
#default defaultnorm1 defaultnorm0
#"sgd adam radam ranger"
for k in `echo "64 128"`
  do
  for j in `echo "defaultnorm0"`
    do
      for i in `echo "adam"`
        do
  
          python train_labelByUser.py --model "$j" --lr 1e-3 --epoch 50 --batch 64 -o ~/work/result/20200825/run__model_"$j"__lr_1e-3__trackCh_pt__batch_64__optimizer_"$i"__pbs_"$k" --optimizer "$i" --device 1 --batchPerStep "$k" -c config.yaml
        done
    done
  done
#python train_labelByUser.py --model "$j" --lr 1e-3 --epoch 50 --batch 64 -o ~/work/result/20200822/run__model_"$j"__lr_1e-3__trackCh_pt__batch_64__optimizer_"$i" --device 0 --optimizer "$i" -c config.yaml