import ctypes

class aList:
	
	def __init__(self,*args):
		self.args = (args)
		self._n = len(args)
		self._c = self._n+1
		self._A = self._make_array(self._c)
		for i in range(len(self.args)):
			self._A[i] = self.args[i]
	
	
	def __len__(self):
		return self._n
	
	def _make_array(self,c):
		return (c* ctypes.py_object)()

	def __getitem__(self,k):
		if not 0 <= k <=self._n:
			return self._A[k%self._n]
		return self._A[k]
	
	def __str__(self):
		x = "[ "
		for i in range(self._n-1):
			x += str(self._A[i])+', '
		return x + str(self._A[self._n-1])+" ]"

	def is_empty(self):
		return self._n == 0

	def __iter__(self):
		for i in range(self._n):
			yield self._A[i]

	def append(self, obj):
		if self._n == self._c:
			self._resize(2 * self._c)
		self._A[self._n] = obj
		self._n += 1

	def __add__(self,b):
		if self._n < len(b):
			y = b 
			x = aList(*self.args)
		else:
			y = aList(*self.args)
			x = b
		for i in range(len(x)):
			y[i] += x[i]
		return y

	def __sub__(self,b):
		if self._n < len(b):
			y = b 
			x = aList(*self.args)
		else:
			y = aList(*self.args)
			x = b
		for i in range(len(x)):
			y[i] -= x[i]
		return y

	def __iadd__(self,b):
		if self._n < len(b):
			y = b 
			x = aList(*self.args)
		else:
			y = aList(*self.args)
			x = b
		for i in range(len(x)):
			y[i] += x[i]



	def __isub__(self,b):
		if self._n < len(b):
			y = b 
			x = self._A
		else:
			y = self._A
			x = b
		for i in range(len(x)):
			y[i] -= x[i]

		
	def _resize(self, c):
		B = self._make_array(c)
		for k in range(self._n):
			B[k] = self._A[k]
		self._A = B
		self._c = c


	def __mul__(self,i):
		B = aList()
		for j in range(self._n):
			for k in range(i):
				B.append(self._A[j])
		return B

	def __rmul__(self, i):
		B = aList()
		for item in range(self._n):
			B.append(self._A[item] * i)
		return B

	def revitr(self):
		count = -1
		for i in range(self._n):
			yield self.args[count]
			count -=1 

	def select(self,ls):
		B = aList()
		for i in range(len(ls)):
			B.append(self._A[ls[i]%self._n])
		return B

	def __setitem__(self,k,x):
		self._A[k] = x

c = aList(1,2,3,4,5)
b = aList(2,2,2,3,8)
x = c[9999]
print(c)
