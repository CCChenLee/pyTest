#! /usr/bin/python3
#-*- coding:UTF-8 -*-

def quicksort(L):
	qsort(L,0,len(L)-1)

def qsort(L,first,last):
	if first<last:
		split=partition(L,first,last)
		qsort(L,first,split-1)
		qsort(L,split+1,last)

def partition(L,first,last):
	pivot=L[first]
	leftmark=first+1
	rightmark=last
	while True:
		while L[leftmark]<=pivot:
			if leftmark==rightmark:
				break
			leftmark+=1
		while L[rightmark]>pivot:
			rightmark-=1
		if leftmark<rightmark:
			L[leftmark],L[rightmark]=L[rightmark],L[leftmark]
		else:
			break
	L[first],L[rightmark]=L[rightmark],L[first]
	return rightmark
num_list=[-4,5,6,3,7,11,1,2]
print('排序前：'+str(num_list))
quicksort(num_list)
print('排序后：'+str(num_list))