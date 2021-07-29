#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 13:27:19 2021

@author: yhep_ex_04
"""

'''
j, q, k, a, h, d, s, c

'''
def fill_dic():
    dic = {}
    # for i in range(48,90+1): # all letters
    for i in [67, 68, 72, 83]: # only pattern
        #print(i, chr(i))
        # for j in range(48,90+1): # all letters
        for j in range(50,90+1):
            # if 48 <= i <= 57 and 48 <= j <= 57 : 
            #     dic[chr(i)+chr(j)]=''
            # if 65 <= i <= 90 and 65 <= j <= 90: # all letters
            if 48 <= j <= 57 or j in [74, 75, 81, 65]: 
                    
                dic[chr(i)+chr(j)]=''
                if j == 57:
                    dic[chr(i)+'10']=''
    print(dic)
    return(dic)

dic = {'C2': '', 'C3': '', 'C4': '', 'C5': '', 'C6': '', 'C7': '', 'C8': '', 
       'C9': '', 'C10': '', 'CA': '', 'CJ': '', 'CK': '', 'CQ': '', 
       
       'D2': '', 'D3': '', 'D4': '', 'D5': '', 'D6': '', 'D7': '', 'D8': '', 
       'D9': '', 'D10': '', 'DA': '', 'DJ': '', 'DK': '', 'DQ': '', 
       
       'H2': '', 'H3': '', 'H4': '', 'H5': '', 'H6': '', 'H7': '', 'H8': '', 
       'H9': '', 'H10': '', 'HA': '', 'HJ': '', 'HK': '', 'HQ': '', 
       
       'S2': '', 'S3': '', 'S4': '', 'S5': '', 'S6': '', 'S7': '', 'S8': '', 
       'S9': '', 'S10': '', 'SA': '', 'SJ': '', 'SK': '', 'SQ': ''}
    