import heapq
from random import shuffle

#nlog(n)
def mergesort(A):
	if len(A) > 1:
		return heapq.merge(mergesort(A[:len(A)//2]),mergesort(A[len(A)//2:]))
	return A

#nlog(n)
def heapsort(A):
	heapq.heapify(A)
	return [heapq.heappop(A) for x in range(len(A))]

#nlog(n) most of the time
from random import shuffle
A = [1,2,3,4,5,6,7]
shuffle(A)
#print(A)

def pivot(A,l,r,mid):
	while l<r:
		while A[l] < mid:
			l += 1
		while A[r] > mid:
			r -= 1
		A[r],A[l] = A[l],A[r]
	return r


def quicksort(A,l,r):
	if l<r:
		p = pivot(A,l,r,A[l]); quicksort(A,l,p-1),quicksort(A,p+1,r)

#finding nth largest item in O(n) time with quicksort pivot ideas
def quickselect(A,i=0,l= 0,r=None):
    	if r is None:
		r = len(A)-1
	p = pivot(A,l,r,A[l])
	if i == p:
		return A[i]
	if i < p:
		return quickselect(A,i,l,p-1)
	if i > p:
		return quickselect(A,i,p+1,r)

