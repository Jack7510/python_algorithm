#!/usr/bin/env python3
# file: quick_sort.py
# auth: Jack Lee
# Date: Jan 31, 2017
# Desc: implementation of quick sort algorithm
#       https://en.wikipedia.org/wiki/Quicksort
#
import random


# 
# func: partition(array, low, high)
# desc: find the pivot for the array to quick sort
#       on the left of pivot, less
# para: a  - the array to be sort
#       lo - start index of the array, inclusive
#       hi - end index of the array, inclusive
# ret : pivot of the array, left of pivot, less than pivot,
#
def partition(a, lo, hi):
    pivot = a[hi]
    i = lo  # place for swapping

    # for j := lo to hi - 1 do
    for j in range(lo, hi):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]  # swap A[i] with A[j]
            i += 1

    a[i], a[hi] = a[hi], a[i]  # swap A[i] with A[hi]
    return i


#
# func: quick_sort(array, lo, hi)
# desc: implementation of quick sort algorithm in Python
# para: a  - the array to be sort
#       lo - start index of the array, inclusive
#       hi - end index of the array, inclusive
# ret : the sorted array
#
def quick_sort(a, lo, hi):
    if lo < hi:
        p = partition(a, lo, hi)
        quick_sort(a, lo, p - 1)
        quick_sort(a, p + 1, hi)

    return a


#
# func: gen_rand_list(numbers of random )
# desc: generate random number of list with bubble sort algorithm
# para: number - how many numbers of random will be generated
#
def gen_rand_list(number):
    a = []  # null list
    for i in range(number):
        a.append(random.randrange(number * 2))  # range will be 0 to 2 * number

    return a


# test program
if __name__ == '__main__':
    n = eval(input("input numbers of rand you want to generate:"))
    l = gen_rand_list(n)
    print(l)
    print(quick_sort(l, 0, len(l) - 1))