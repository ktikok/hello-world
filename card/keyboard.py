# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 13:01:02 2021

@author: pcname
"""

import time

import random

book = {
        '0':['ㅁ'],
        '1':['ㅣ'],
        '2':['.'],
        '3':['ㅡ'],
        '4':['ㄱ', 'ㅋ', 'ㄲ'],
        '5':['ㄴ', 'ㄹ'],
        '6':['ㄷ', 'ㅌ', 'ㄸ'],
        '7':['ㅂ', 'ㅍ', 'ㅃ'],
        '8':['ㅅ', 'ㅎ', 'ㅆ'],
        '9':['ㅈ', 'ㅊ', 'ㅉ']
        }

tlist = []
for i in range(10):
    tlist.append(10)
    
def test(previous):
    # for i in tlist:
    #     if i == min(tlist)
    
    pro = str(random.randint(0,9))
    while previous==pro:
        pro = str(random.randint(0,9))
    #pro = str(tlist.index(max(tlist)))
    t1=time.time()
    guess = input(pro+" : ")
    howlong = time.time()-t1
    
    # print(((time.time()-t1)//0.1)*0.1)
    if len(guess) == len(book[pro]):
        for i in book[pro]:
            if i not in guess:
                print('X')
                break
        else:
            print(round(howlong,2))
            print('O')
            tlist[int(pro)] = (tlist[int(pro)]+howlong)/2

            # if howlong < tlist[int(pro)]:
            #     tlist[int(pro)] = howlong
                #print(round(howlong,2))
                # t1=time.time()
    else:
        print('X')
        
    if max(tlist)<2:
        return
    else:
        test(pro)
    
if __name__ == "__main__":
    #t1=time.time()
    previous=''
    test(previous)