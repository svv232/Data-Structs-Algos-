def insomewhere(ihatemylife,s):
	for i in ihatemylife:
		if isinstance(i,list):
			if insomewhere(i,s): return True
		else:
			if i == s: return True
	return False

def unnest(A):
	if not A:
		return A
	result = [A[0]] if type(A[0]) is int else unnest(A[0])
	return result + unnest(A[1:])

def triangle(n): return [[i for i in range(n,x,-1)] for x in range(n-1,-1,-1)]

def print2d(AA): print('['),[print(" "+str(i)) for i in AA],print(']')

def table(f,xrange,yrange): return [[f(i,x) for i in xrange] for x in yrange]

def nest(x,n): return x if n == 0 else nest([x],abs(n)-1)

A = [[1],[1]] * 5 
