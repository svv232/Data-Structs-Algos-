# log(n)
def binary_searchi(A,data): #iterative binary search
	end = len(A)-1
	start = 0
	while start <= end:
		mid = start + ((end - start)//2)
		if A[mid] < data:
			start = mid+1
		if A[mid] > data:
			end = mid-1
		if A[mid] == data:
			return True
	return False

#log(n)
def binary_search(A,key,start=0,end=None): #recursive binary search
	if end is None:
		end = len(A)-1
	mid = (start+end)//2
	if start <= end:
		if key > A[mid]:
			return binary_search(A,key,mid+1,end)
		if key < A[mid]:
			return binary_search(A,key,start,mid-1)
	return key == A[mid]


