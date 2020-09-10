#!/bin/bash
#default defaultnorm1 defaultnorm0
#"sgd adam radam ranger"
## batch 128 bps 256
#1e-3 2e-3 5e-3 7e-3

for k in `echo "1e-3"`
do
  for j in `echo "CPlargekernelnorm0"`
    do
      for i in `echo "adam"`
        do
  
          python train_labelByUser.py --optimizer "$i" --device 0 --model "$j" --lr "$k" --epoch 50 --batch 64 --batchPerStep 1 -o ~/work/result/20200901/"$j"__"$i"__batch_64__lr_"$k" -c config.yaml
        done
    done
done
