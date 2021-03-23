#!/bin/bash
#default defaultnorm1 defaultnorm0
#"sgd adam radam ranger"
## batch 128 bps 256
for k in `echo "7e-3"`
do
  for j in `echo "defaultnorm0"`
    do
      for i in `echo "adam"`
        do
  
          python train_labelByUser.py --model "$j" --lr "$k" --epoch 50 --batch 128 --batchPerStep 256 -o ~/work/result/20200831/"$j"__"$i"__batch_128__bps_256__lr_"$k" --optimizer "$i" --device 0 -c config.yaml
        done
    done
done