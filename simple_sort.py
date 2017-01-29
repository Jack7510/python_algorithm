# author: Jack Lee
# samples of Python
# sort algorithm with Python
# Simple Sort: Bubble, Insertion
# 

from random import randrange

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


# 
# func: bubble_sort( list )
# desc: sort a list in ascend 
#       algorithm desc, https://en.wikipedia.org/wiki/Bubble_sort
# para: list - the list will be sorted
#
def bubble_sort( l ):
	n = len( l )
	if n < 2 :
		return
	
	for i in range( n ):
		for j in range( i + 1, n ):  # compare L[i] with L[i+1] ... n-1
			if l[i] > l[j]:	# if i > j, swap them
				l[i], l[j] = l[j], l[i]

	return


#
# func: shell_sort( list )
# desc: generate random number of list with Shell algorithm
# para: number - how many numbers of random will be generated
#
def shell_sort( L ):
	return L


#
# func: insertion_sort( list )
# desc: generate random number of list with Insertion algorithm
# desc:    https://en.wikipedia.org/wiki/Insertion_sort
# para: number - how many numbers of random will be generated
#
def insertion_sort_v1( L ):
	n = len( L )
	if n < 2 :
		return L

	for i in range( 1, n ) :
		j = i
		while j > 0 and L[j - 1] > L[ j ] :
			L[j - 1], L[ j ] = L[j], L[j - 1]	# swap
			j = j - 1

	return L

#
# v2: more efficient, do not
#
def insertion_sort( L ):

	# check the parameter
	n = len( L )
	if n < 2 :
		return L

	for i in range( 1, n ) :
		x = L[ i ]
		j = i - 1
		while j >= 0 and L[ j ] > x:
			L[ j + 1 ] = L[ j ]				# move L[j] to upper position
			j = j - 1

		L[ j + 1 ] = x

	return L

#
# func: insertion_sort_R( list, numbers )
# desc: generate random number of list with Insertion algorithm in Recursvie way
# desc:    https://en.wikipedia.org/wiki/Insertion_sort
# para: L 		- the list to be sorted
#       numbers - how many numbers of random will be generated
#       
def insertion_sort_R( L, numbers ):

	# check the parameter
	if numbers < 2 :
		return L

	insertion_sort_R( L, numbers - 1 )

	# place L[numbers - 1] in the left sorted array/list
	x = L[ numbers - 1 ]
	i = numbers - 2
	while i >= 0 and L[ i ] > x :
		L[i + 1] = L[ i ]
		i = i - 1
	L[ i + 1 ] = x

	return L


#
# func: merge_sort( list, numbers )
# desc: generate random number of list with merge algorithm
# desc:    https://en.wikipedia.org/wiki/Merge_sort
# para: L 		- the list to be sorted
#       numbers - how many numbers of random will be generated
#       


# test program
if __name__ == '__main__':
	n = eval(input("input numbers of rand you want to generate:"))
	l = gen_rand_list(n)
	print(l)
	#bubble_sort( l )
	#insertion_sort( l )
	insertion_sort_R( l, l.count() )
	print(l)

