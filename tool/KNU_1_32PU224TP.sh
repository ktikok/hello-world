#!/bin/bash
#default defaultnorm1 defaultnorm0
#"sgd adam radam ranger"
for j in `echo "defaultnorm1"`
  do
    for i in `echo "sgd adam"`
      do

        python train_labelByUser.py --model "$j" --lr 1e-3 --epoch 50 --batch 64 -o ~/work/result/20200822/run__model_"$j"__lr_1e-3__trackCh_pt__batch_64__optimizer_"$i" --optimizer "$i" --device 0 -c config.yaml
      done
  done
