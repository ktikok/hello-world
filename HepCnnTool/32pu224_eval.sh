#!/bin/bash

for i in `ls ~/work/result/32PU224/adam/`
do 

  x=`nvidia-smi | head -15 | tail -1 | head -c 63 | tail -c 3`; 
  while [ $x -gt 0 ]
  do 
    sleep 1
    x=`nvidia-smi | head -15 | tail -1 | head -c 63 | tail -c 3`; 
  done

  source /store/hep/common/sw/anaconda3/etc/profile.d/conda.sh; conda activate pytorch; SAMPLEDIR=/store/hep/users/jhgoh/nurion4hep/20200626_1/hdf5_noPU_224x224/ python eval_torch.py --batch 64 --input /users/tongilkim/work/result/32PU224/adam/$i

done




