#
# file: merge_sort.py
# desc: implement merge sort algorithm with Python
#       https://en.wikipedia.org/wiki/Merge_sort
# auth: Jack Lee
# Date: Jan 29, 2017
#

from random import randrange


#
# func: top_down_merge( listA, begin, middle, end, ListB )
# desc: generate random number of list with merge sort algorithm
#       more description  https://en.wikipedia.org/wiki/Merge_sort
#       
# para: sort listB as source, to listA, from Begin to End. 
#       Begin is inclusive, End is exclusive
#       
def top_down_merge(list_b, first, middle, last, list_a):
    j = first
    k = middle

    # print( 'top_down_merge' , range( Begin, Mid, End ) )
    for i in range(first, last):
        # print( j, listB[j], k, listB[k] )
        if j < middle and (k >= last or list_b[j] < list_b[k]):
            list_a[i] = list_b[j]
            j += 1
        else:
            list_a[i] = list_b[k]
            k += 1

    # print( listA[ Begin : End ] )
    return


#
# func: top_down_split_merge( listA, begin, end, ListB )
# desc: generate random number of list with merge sort algorithm
#       Sort the given run of array A[] using array B[] as a source.
#       more description  https://en.wikipedia.org/wiki/Merge_sort
#       
# para: sort listB as source, to listA, from Begin to End. 
#       Begin is inclusive, End is exclusive
#       
def top_down_split_merge(list_b, first, last, list_a):
    # if size == 1,  considering sorted
    if (last - first) < 2:
        # print( Begin, End )
        return

    middle = (first + last) // 2
    # print( Begin, Middle, End )
    # recursively sort both runs from array A[] into B[]
    top_down_split_merge(list_a, first, middle, list_b)
    top_down_split_merge(list_a, middle, last, list_b)

    # merge the resulting runs from array B[] into A[]
    top_down_merge(list_b, first, middle, last, list_a)

    return


#
# func: merge_sort( list )
# desc: generate random number of list with merge sort algorithm
#       more description  https://en.wikipedia.org/wiki/Merge_sort
#       
# para: L - the list to be sorted
#       
def merge_sort(l):
    list_a = l
    # copy list A to list B, list B as working list
    list_b = list_a[:]

    # split merge from B to A, from 0 to n
    top_down_split_merge(list_b, 0, len(list_b), list_a)

    return


#
# func: gen_rand_list(numbers of random )
# desc: generate random number of list with bubble sort algorithm
# para: number - how many numbers of random will be generated
#
def gen_rand_list(number):
    a = []  # null list
    for i in range(number):
        a.append(randrange(number * 2))  # range will be 0 to 2 * number

    return a


# test program
if __name__ == '__main__':
    n = eval(input("input numbers of rand you want to generate:"))
    l = gen_rand_list(n)
    print(l)

    # bubble_sort( l )
    # insertion_sort( l )
    # insertion_sort_R( l, l.count() )
    merge_sort(l)
    print(l)
