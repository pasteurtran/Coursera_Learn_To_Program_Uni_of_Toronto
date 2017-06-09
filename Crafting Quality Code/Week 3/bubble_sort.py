#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 19:25:42 2017

@author: PasteurTran
"""

""" 
Bubble sort 
The point of this list is to get to 'bubble' the biggest in the list to the RIGHT 
most position. 
7 3 5 2 #7 is largest
3 7 5 2 
3 5 7 2
3 5 2 7

>>> now end is the second last, since last is sorted
Start again at front
3 5 2 | 7 - no swap on 3
3 2 5 | 7 - 5 is swapped to 2 as i moved over

>>> now
3 2 | 5 7 
2 3 5 7 - sorted

"""
def bubble_sort(L):
    
    end = len(L)-1
             
    while end != 0:
        
        for i in range(end):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i+1], L[i]
                
        end = end - 1
        
        
