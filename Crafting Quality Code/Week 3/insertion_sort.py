#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 19:38:40 2017

@author: administrator
"""

"""
Insertion Sort
The i = 0
So you MOVE to fit based on comparison.
It goes through and passes on, remember what has happened and moves it to the front or locaiton
First it needs to FIND the index, and then put it in that position, while shifting EVYERTHING to the right

"""

def insert(L, i):
    """ (list, int) -> NoneType

    Precondition: L[:i] is sorted from smallest to largest.

    Move L[i] to where it belongs in L[:i + 1].

    >>> L = [7, 3, 5, 2]
    >>> insert(L, 1)
    >>> L
    [3, 7, 5, 2]
    """

    # The value to be inserted into the sorted part of the list.
    value = L[i]

    # Find the index, j, where the value belongs.
    # Make room for the value by shifting.
    j = i
    while j != 0 and L[j - 1] > value:
        # Shift L[j - 1] one position to the right to L[j].
        L[j] = L[j - 1]
        j = j - 1


    # Put the value where it belongs.
    L[j] = value    


def insertion_sort(L):
    """ (list) -> NoneType

    Sort the items of L from smallest to largest.

    >>> L = [7, 3, 5, 2]
    >>> insertion_sort(L)
    >>> L
    [2, 3, 5, 7]
    """

    for i in range(len(L)):
        insert(L, i)
    
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()