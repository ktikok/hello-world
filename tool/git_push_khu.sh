#!/bin/bash

#default defaultnorm1 defaultnorm0
#"sgd adam radam ranger"
#count pt

#run__lr_1e-3__batch_64__optimizer_radam/

k="pt"
for j in `echo "default defaultnorm1 defaultnorm0"`
  do
    for i in `echo "sgd adam radam ranger"`
      do
        #knu
        #mkdir /u/user/xhdxhd6226/work/HEP-CNN-results/training/224x224_trackpt/model_"$j"/run__lr_1e-3__batch_64__optimizer_"$i"/
        #cp /u/user/xhdxhd6226/work/result/32PU_trackpt/"$j"_"$i"/*.csv /u/user/xhdxhd6226/work/HEP-CNN-results/training/224x224_trackpt/model_"$j"/run__lr_1e-3__batch_64__optimizer_"$i"/
        #gzip /u/user/xhdxhd6226/work/HEP-CNN-results/training/224x224_trackpt/model_"$j"/run__lr_1e-3__batch_64__optimizer_"$i"/*
        #cp /u/user/xhdxhd6226/work/result/32PU_trackpt/"$j"_"$i"/*.txt /u/user/xhdxhd6226/work/HEP-CNN-results/training/224x224_trackpt/model_"$j"/run__lr_1e-3__batch_64__optimizer_"$i"/
        mkdir ~/work/HEP-CNN-results/training/224x224_track"k"/model_"$j"/run__lr_1e-3__batch_64__optimizer_"$i"/
        cp ~/work/result/20200822/run__model_"$j"*optimizer_"$i"/*.csv ~/work/HEP-CNN-results/training/224x224_trackpt/model_"$j"/run__lr_1e-3__batch_64__optimizer_"$i"/
        gzip ~/work/HEP-CNN-results/training/224x224_trackpt/model_"$j"/run__lr_1e-3__batch_64__optimizer_"$i"/*
        cp ~/work/result/20200822/run__model_"$j"*optimizer_"$i"/*.txt ~/work/HEP-CNN-results/training/224x224_trackpt/model_"$j"/run__lr_1e-3__batch_64__optimizer_"$i"/
        
      done
  done

git add .
git commit -m " --lr 1e-3 --epoch 50 --batch 64 --device 2 -c config.yaml"
git push