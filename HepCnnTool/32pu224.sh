#!/bin/bash

source /store/hep/common/sw/anaconda3/etc/profile.d/conda.sh; conda activate pytorch; SAMPLEDIR=/store/hep/users/jhgoh/nurion4hep/20200626_1/hdf5_noPU_224x224/ python train_labelByUser.py --epoch 100 --batch 64 --batchPerStep 512 --device 0 --optimizer radam -o ~/work/result/32PU224/B_64_bPS_500_O_radam_E_100/
