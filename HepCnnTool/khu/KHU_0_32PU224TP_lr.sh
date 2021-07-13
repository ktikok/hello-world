#!/bin/bash
#default defaultnorm1 defaultnorm0
#"sgd adam radam ranger"
# 64 128 256 512
for k in `echo "512"`
  do
  for j in `echo "defaultnorm0"`
    do
    for i in `echo "adam"`
      do
      for l in `echo "6e-3"`
        do
        source /store/hep/common/sw/anaconda3/etc/profile.d/conda.sh; conda activate pytorch150_pyG; python train_labelByUser.py  --optimizer "$i" --model "$j" --lr "$l" --epoch 50 --batch 64 --batchPerStep "$k"  --device 0 -o ~/work/result/20200829/"$j"__"$i"__batch_64__pbs_"$k"__lr_"$l" -c config.yaml
        done  
      done
    done
  done
#python train_labelByUser.py --model "$j" --lr 1e-3 --epoch 50 --batch 64 -o ~/work/result/20200822/run__model_"$j"__lr_1e-3__trackCh_pt__batch_64__optimizer_"$i" --device 0 --optimizer "$i" -c config.yaml