#!/bin/bash

#for i in `echo "defaultnorm1 circpadnorm1 circpadlog3chnorm1 circpadlog5chnorm1"`


#source /store/hep/common/sw/anaconda3/etc/profile.d/conda.sh; conda activate pytorch; ./draw_Sig_significance2.py -o ~/work/result/graphs/0723_0730/model_CP -i /users/swkim95/HEP-CNN3/HEP-CNN/result/64_noPU/model_CP -a True


for i in `ls /users/swkim95/HEP-CNN3/HEP-CNN/result/64_noPU/`
do
  echo start : $i
  ./draw_Sig_significance2.py -o ~/work/result/graphs/0723_0730/64_noPU/$i -i /users/swkim95/HEP-CNN3/HEP-CNN/result/64_noPU/$i -a True

done

for i in `ls /users/swkim95/HEP-CNN3/HEP-CNN/result/64_32PU/`
do
  echo start : $i
  ./draw_Sig_significance2.py -o ~/work/result/graphs/0723_0730/64_32PU/$i -i /users/swkim95/HEP-CNN3/HEP-CNN/result/64_32PU/$i -a True

done

echo 'Every things done.'