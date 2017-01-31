#!/usr/bin/env python3
# file: heap_sort.py
# auth: Jack Lee
# Date: Jan 30, 2017
# Desc: implementation of heap sort algorithm
#       https://en.wikipedia.org/wiki/Heapsort
#
import heapq
import random
import math


#
# func: heapsort(array )
# desc: sort a given array with heap sort algorithm by Python library
#       heap function import from heapq modules
# para: array to be sorted
#
def heapsort(a):
    h = []
    for i in a:
        heapq.heappush(h, i)

    return [heapq.heappop(h) for i in range(len(h))]


#
# subroutines for index calculation of heap index
#
def index_parent(i):
    return math.floor((i - 1) / 2)


def index_left_child(i):
    return 2 * i + 1


def index_right_child(i):
    return 2 * i + 2

#
# func: my_heap_sort( array )
# desc: implementation of heap sort. not using heap library
# para: array to be sorted
#


#
# (Repair the heap whose root element is at index 'start',
# assuming the heaps rooted at its children are valid)
#
def sift_down(a, start, end):

    root = start

    while index_left_child(root) <= end:
        child = index_left_child(root)  # left child for root
        swap = root                     # Keeps track of child to swap with

        if a[swap] < a[child]:
            swap = child

        # (If there is a right child and that child is greater)
        if (child + 1) <= end and a[swap] < a[child + 1]:
            swap = child + 1

        if swap == root:
            # (The root holds the largest element. Since we assume the heaps rooted at the
            # children are valid, this means that we are done.)
            return
        else:
            a[root], a[swap] = a[swap], a[root]     # swap two elements
            root = swap     # (repeat to continue sifting down the child now)

    return


#
# desc: Build the heap in array a so that largest value is at the root
#        (Put elements of 'a' in heap order, in-place)
#
def build_max_heap(a):

    # (start is assigned the index in 'a' of the last parent node)
    # (the last element in a 0-based array is at index count-1;
    # find the parent of that element)
    start = index_parent(len(a) - 1)

    while start >= 0:
        # (sift down the node at index 'start' to the proper place such that all nodes below
        # the start index are in heap order)
        sift_down(a, start, len(a) - 1)

        # go to next parent node
        start -= 1

    # (after sifting down the root all nodes/elements are in heap order)
    return a


def my_heap_sort(a):

    # Build the heap in array a so that largest value is at the root
    build_max_heap(a)       # heapify

    # (The following loop maintains the invariants that a[0:end] is a heap and every element
    # beyond end is greater than everything before it (so a[end:count] is in sorted order))
    count = len(a)
    end = count - 1
    while end > 0:
        # (a[0] is the root and largest value. The swap moves it in front of the sorted elements.)
        a[0], a[end] = a[end], a[0]     # swap

        # (the heap size is reduced by one), like pop the biggest one
        end -= 1
        # (the swap ruined the heap property, so restore it)
        sift_down(a, 0, end)

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

    # print(heapsort(l))
    print(my_heap_sort(l))
