# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 09:51:20 2019

@author: paprasad
"""

l = map(int,input().strip().split())
number = int(input())

l = list(l)

l.sort()
def binary_search(l,number,low,high):
    if len(l)==1:
        if l[0]==number:
            return True
        else:
            return False
        
    elif len(l)>1:
        mid = low+high/2
        if binary_search(l[int(low):int(mid)],number,low,mid):
            return True
        elif binary_search(l[int(mid):int(high)],number,mid,high):
            return True
        else:
            return False
    else:
        return False
        
        
        
print(binary_search(l,number,0,len(l)))        