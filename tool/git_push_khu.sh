#!/bin/bash

#default defaultnorm1 defaultnorm0
#"sgd adam radam ranger"
#count pt

#run__lr_1e-3__batch_64__optimizer_radam/

for k in `echo "6e-3 7e-3"`
do
for j in `echo "defaultnorm0"`
  do
    for i in `echo "adam"`
      do
        #knu
        #mkdir /u/user/xhdxhd6226/work/HEP-CNN-results/training/224x224_trackpt/model_"$j"/run__lr_1e-3__batch_64__optimizer_"$i"/
        #cp /u/user/xhdxhd6226/work/result/32PU_trackpt/"$j"_"$i"/*.csv /u/user/xhdxhd6226/work/HEP-CNN-results/training/224x224_trackpt/model_"$j"/run__lr_1e-3__batch_64__optimizer_"$i"/
        #gzip /u/user/xhdxhd6226/work/HEP-CNN-results/training/224x224_trackpt/model_"$j"/run__lr_1e-3__batch_64__optimizer_"$i"/*
        #cp /u/user/xhdxhd6226/work/result/32PU_trackpt/"$j"_"$i"/*.txt /u/user/xhdxhd6226/work/HEP-CNN-results/training/224x224_trackpt/model_"$j"/run__lr_1e-3__batch_64__optimizer_"$i"/
        
        #############################khu
        #rm -r ~/work/HEP-CNN-results/training/224x224_trackpt/model_"$j"/run__lr_1e-3__batch_64__optimizer_"$i"/
        mkdir ~/work/HEP-CNN-results/training/224x224_trackpt/model_"$j"/run__lr_"$k"__batch_64x512/
        cp ~/work/result/20200829/defaultnorm0__adam__batch_64__bps_512__lr_"$k"/*.csv ~/work/HEP-CNN-results/training/224x224_trackpt/model_"$j"/run__lr_"$k"__batch_64x512/
        gzip ~/work/HEP-CNN-results/training/224x224_trackpt/model_"$j"/run__lr_"$k"__batch_64x512/*
        cp ~/work/result/20200829/defaultnorm0__adam__batch_64__bps_512__lr_"$k"/*.txt ~/work/HEP-CNN-results/training/224x224_trackpt/model_"$j"/run__lr_"$k"__batch_64x512/
        
      done
  done
done
#git add .
#git commit -m "tikim, results of model and optimizer scan"
#git push
