#!/bin/bash
#default defaultnorm1 defaultnorm0
#"sgd adam radam ranger"
#run__lr_1e-3__batch_64__optimizer_radam/
for j in `echo "defaultnorm1"`
  do
    for i in `echo "sgd adam radam ranger"`
      do

        mkdir /u/user/xhdxhd6226/work/HEP-CNN-results/training/224x224_trackpt/model_"$j"/run__lr_1e-3__batch_64__optimizer_"$i"/
        cp /u/user/xhdxhd6226/work/result/32PU_trackpt/"$j"_"$i"/*.csv /u/user/xhdxhd6226/work/HEP-CNN-results/training/224x224_trackpt/model_"$j"/run__lr_1e-3__batch_64__optimizer_"$i"/
        gzip /u/user/xhdxhd6226/work/HEP-CNN-results/training/224x224_trackpt/model_"$j"/run__lr_1e-3__batch_64__optimizer_"$i"/*
        cp /u/user/xhdxhd6226/work/result/32PU_trackpt/"$j"_"$i"/*.txt /u/user/xhdxhd6226/work/HEP-CNN-results/training/224x224_trackpt/model_"$j"/run__lr_1e-3__batch_64__optimizer_"$i"/

      done
  done

git add .
git commit -m "new results"
git push