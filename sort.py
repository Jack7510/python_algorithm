# author: Jack Lee
# samples of Python
# sort algorithm with Python

from random import randrange

#
# func: gen_rand_list(numbers of random )
# desc: generate random number of list
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

# test program
if __name__ == '__main__':
	n = eval(input("input numbers of rand you want to generate:"))
	l = gen_rand_list(n)
	print(l)
	bubble_sort( l )
	print(l)

