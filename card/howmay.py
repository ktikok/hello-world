# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 11:12:13 2021

@author: pcname
"""

import random
import time


def again():
    table=[]
    n = 3
    for i in range(n):
        table.append([])
        for j in range(n):
            table[-1].append(random.randint(0,9))
    print('\n\n')
    for i in table:
        print(i)
    
    t1=time.time()
    time.sleep(0.3)
    print('\n\n')
    #print(time.time()-t1)    
    r=random.randint(1,3)
    print(r)
    print("")
    time.sleep(2)
    print(table[r-1])
    time.sleep(1)
    # for i in range(n):
    #     print('')
    again()
if __name__ == '__main__':
    again()