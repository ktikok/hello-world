#!/bin/bash

#default defaultnorm1 defaultnorm0
#"sgd adam radam ranger"
#count pt

#run__lr_1e-3__batch_64__optimizer_radam/

k="pt"
for j in `echo "defaultnorm0"`
do
  for i in `echo "adam"`
  do
	  for l in `echo "64 128 256 512"`
	  do
# ~/work/result/20200825/run__model_defaultnorm0__lr_1e-3__trackCh_pt__batch_64__optimizer_adam__pbs__128/
      mkdir ~/work/HEP-CNN-results/training/224x224_track"$k"/model_"$j"/run__lr_1e-3__batch_64x"$l"/
      cp ~/work/result/20200825/run__model_defaultnorm0__lr_1e-3__trackCh_pt__batch_64__optimizer_adam__pbs_"$l"/*.csv ~/work/HEP-CNN-results/training/224x224_track"$k"/model_"$j"/run__lr_1e-3__batch_64x"$l"/
      gzip ~/work/HEP-CNN-results/training/224x224_track"$k"/model_"$j"/run__lr_1e-3__batch_64x"$l"/*
      cp ~/work/result/20200825/run__model_defaultnorm0__lr_1e-3__trackCh_pt__batch_64__optimizer_adam__pbs_"$l"/*.txt ~/work/HEP-CNN-results/training/224x224_track"$k"/model_"$j"/run__lr_1e-3__batch_64x"$l"/
      
    done
  done
done
#git add .
#git commit -m "tikim, results of model and optimizer scan"
#git push
