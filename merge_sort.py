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
def top_down_merge( listB, Begin, Mid, End, listA ):

    j = Begin
    k = Mid

    #print( 'top_down_merge' , range( Begin, Mid, End ) )
    for i in range( Begin, End ):
    	# print( j, listB[j], k, listB[k] )
        if j < Mid and ( k >= End or listB[j] < listB[k] ) :
            listA[i] = listB[j]
            j = j + 1
        else:
        	listA[i] = listB[k]
        	k = k + 1

    #print( listA[ Begin : End ] )
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
def top_down_split_merge( listB, Begin, End, listA ):
    
    # if size == 1,  considering sorted
    if (End - Begin) < 2 :
    	#print( Begin, End )
    	return 

    Middle = (Begin + End) // 2
    #print( Begin, Middle, End )
    # recursively sort both runs from array A[] into B[]
    top_down_split_merge( listA, Begin, Middle, listB )
    top_down_split_merge( listA, Middle, End, listB )

    # merge the resulting runs from array B[] into A[]
    top_down_merge( listB, Begin, Middle, End, listA )

    return 


#
# func: merge_sort( list )
# desc: generate random number of list with merge sort algorithm
#       more description  https://en.wikipedia.org/wiki/Merge_sort
#       
# para: L - the list to be sorted
#       
def merge_sort( L ):
    listA = L
    # copy list A to list B, list B as working list
    listB = listA[:]
    
    # split merge from B to A, from 0 to n
    top_down_split_merge(listB, 0, len(listB), listA)

    return 

#
# func: gen_rand_list(numbers of random )
# desc: generate random number of list with bubble sort algorithm
# para: number - how many numbers of random will be generated
#
def gen_rand_list( number ):
	a = []									# null list
	for i in range( number ):
		a.append( randrange(number * 2) )	# range will be 0 to 2 * number

	return a


# test program
if __name__ == '__main__':
	n = eval(input("input numbers of rand you want to generate:"))
	l = gen_rand_list( n )
	print(l)

	#bubble_sort( l )
	#insertion_sort( l )
	#insertion_sort_R( l, l.count() )
	merge_sort( l )
	print(l)

