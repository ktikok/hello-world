#!/bin/bash

#default defaultnorm1 defaultnorm0
#"sgd adam radam ranger"
#count pt

#run__lr_1e-3__batch_64__optimizer_radam/

k="count"
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
        cp ~/work/result/32PU_trackcount/"$j"_"$i"/*.csv
        
      done
  done

git add .
git commit -m "new results"
git push