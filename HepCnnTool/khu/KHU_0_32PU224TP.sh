#!/bin/bash
#default defaultnorm1 defaultnorm0
#"sgd adam radam ranger"
for j in `echo "defaultnorm1"`
  do
    for i in `echo "sgd adam radam ranger"`
      do

        source /store/hep/common/sw/anaconda3/etc/profile.d/conda.sh; conda activate pytorch150_pyG; python train_labelByUser.py --model "$j" --lr 1e-3 --epoch 50 --batch 64 -o ~/work/result/20200822/run__model_"$j"__lr_1e-3__trackCh_pt__batch_64__optimizer_"$i" --device 0 --optimizer "$i" -c config.yaml
      done
  done
#nohup ~/work/tool/32PU224_TP.sh > nohup1.out & echo $! > nohup1_PID.txt; tail -f nohup1.out
