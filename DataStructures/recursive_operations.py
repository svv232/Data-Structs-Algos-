def max_min(sequence,_max=None,_min=None,i=0):
	if _max == _min == None:
		_max =_min = sequence[0]
	if i == len(sequence):
		return _min,_max
	x = sequence[i]
	if x > _max:
		_max = x
	if x < _min:
		_min = x
	return max_min(sequence,_max,_min,i+1)

#print(max_min([1,2,3,4,5,6,7,8,89,9]))
"""each recursive call takes constant time and there are N recursive calls therefore the 
runtime is O(N)"""

#-------------------------------------------------------
def base_two(n, c=0):
	if  n // 2 == 0:
		return c
	else:
		return base_two(n // 2,c+1)
		
#print(base_two(8))
#print(base_two(64))
#print(base_two(2))

#runtime is O(logN)
"""The runtime for this function is logN because
N /2^k = 1 ==> k  = logN"""

#-------------------------------------------------------
def uniqueness(lst):
    if len(lst) == 1:
        return True
    else:
        first = lst[0]
        rest = lst[1:]
        x = first not in rest
        r = uniqueness(rest)
        return x and r

#print(uniqueness([1,23,4,5,6,7]))
#runtime = N(O)^2
"""There are N recursive calls and each call takes N time"""
#-----------------------------------------------------
def subsets2(A):
	return [], list(subsets(A))

def subsets(A):
	if len(A) == 1:
		yield A
	else:
		yield [A[0]]
		for subset in subsets(A[1:]):
			yield subset
			yield [A[0]] + subset

#print(list(subsets2([1,2,3,4])))
#runtime = N(O)^2
"""There are N recursive calls and for each successive call is one input size
less therefore the sum of all the recursive calls in this function will be O(N^2)
"""
#-------------------------------------------------------
def palindrome (string, a=0,b=-1):
        if a == len(string)//2 and string[a - 1] == string[(len(string) //2) - 1]:
            return True
        elif string[a] != string[b]:
        	return False
        else:
        	return palindrome(string, a+1,b-1)
#print(palindrome('racecar'))
#print(palindrome('dcbewkice2'))
""" In this function there are N divided by 2 recursive calls each recursive
is in constant time"""
#-------------------------------------------------------

def sorting(A, pivot, l=0, r=None):
    if r == None:
        r = len(A) - 1
    if l < r:
        if A[l] < pivot:
            if A[r] > pivot:
                sorting(A, pivot, l + 1, r - 1)
            else:
                sorting(A, pivot, l + 1, r)
        else:
            if A[r] > pivot:
                sorting(A, pivot, l, r - 1)
            else:
                A[l], A[r] = A[r], A[l]
                sorting(A, pivot, l, r)


A = [3,56,3,2,56,2,2,67,2,12,3,7,4,8,6]
sorting(A, 7)
#print(A)

"""runtime is O(N) for each recursive call there is only one
successive recursive call and every recursive call is constant"""
