#!/usr/bin/env python3
# file: heap_sort.py
# auth: Jack Lee
# Date: Jan 30, 2017
# Desc: implementation of heap sort algorithm
#     
import heapq
import random


#
# func: heapsort(array )
# desc: sort a given array with heap sort algorithm
#       heap function import from heapq modules
# para: array to be sorted
#
def heapsort(a):
    h = []
    for i in a:
        heapq.heappush(h, i)

    return [heapq.heappop(h) for i in range(len(h))]


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

    print(heapsort(l))
