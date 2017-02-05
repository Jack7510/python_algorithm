#!/usr/bin/env python3

#
# Desc: implementation of binary search algorithm
#       https://en.wikipedia.org/wiki/Binary_search_algorithm
#

import random
import math
import heap_sort


#
# func: binary_search( array, target )
# para: array - the sorted array
#       target - the number to be found
# ret : index of array where target is, -1 if not found
#
def sub_binary_search(a, left, right, target_number):
    if left > right:
        return -1

    middle = math.floor((left+right) / 2)
    # log
    # print("left: ", left, "middle: ", middle, "right: ", right)

    if a[middle] < target_number:
        return sub_binary_search(a, middle + 1, right, target_number)
    elif a[middle] > target_number:
        return sub_binary_search(a, left, middle - 1, target_number)
    else:
        # now a[middle] == target_number
        return middle


def binary_search(a, target_number):
    return sub_binary_search(a, 0, len(a) - 1, target_number)


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

    l = heap_sort.heap_sort(l)
    print(l)

    target = random.randrange(n * 2)    # generate a random number to be search
    print("target: ", target)
    print("index: ", binary_search(l, target))
