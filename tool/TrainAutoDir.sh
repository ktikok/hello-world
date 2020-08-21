#!/bin/bash

#for k in {5..0}
for k in {3..3}
do
  for i in `echo "2e-4 5e-4"`
  do
#   for j in `echo "sgd adam radam ranger"
    for j in `echo "adam"`;
    do 
      l=B_$((8*2**$k))_L_`echo $i`_O_$j
      mkdir $l
      
    done
  done
done
