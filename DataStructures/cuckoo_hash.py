import random 
class HT:
	def __init__(self):
		self._A = [[(None,) for x in range(10)],[(None,) for x in range(10)]]
		self._size = 0
		self._hash = random.random()

	def hash0(self,x,r=None):
		if r is None: r = self._hash
		return hash((x,0,r))

	def hash1(self,x,r=None):
		if r is None: r = self._hash
		return hash((x,1,r))

	def __getitem__(self,key):
		if key in self:
			if self._A[0][self.hash0(key)%len(self._A[0])][0] == key:
				return self._A[0][self.hash0(key)%len(self._A[0])][1]
			return self._A[1][self.hash1(key)%len(self._A[1])][1]
		raise KeyError("Value not in hash")

	def __setitem__(self,k,v):
		original = self.hash0(k)
		if k not in self:
			self._size += 1
			while True:
				hash0 = self.hash0(k)%len(self._A[0])
				k_prime = self._A[0][hash0]
				k_d_prime = self._A[1][self.hash1(k_prime[0])%len(self._A[1])]
				if self._A[0][hash0][0] is None:
					self._A[0][hash0] = (k,v)
					return 
				else:
					if self._A[1][self.hash1(k_prime[0])%len(self._A[1])][0] is None:
						self._A[0][hash0] = (k,v)
						self._A[1][self.hash1(k_prime[0])%len(self._A[1])] = k_prime
						return 
					else:
						if self._A[0][self.hash0(k_d_prime[0])%len(self._A[0])][0] is None:
							self._A[0][hash0] = (k,v)
							self._A[1][self.hash1(k_prime[0])%len(self._A[1])] = k_prime
							self._A[0][self.hash0(k_d_prime[0])%len(self._A[0])] = k_d_prime
							return 
						else:
							self._A[0][hash0] = (k,v)
							self._A[1][self.hash1(k_prime[0])%len(self._A[1])] = k_prime
							k,v = k_d_prime
				if self.hash0(k) == original:
					break			
			old,old1 = self._A		
			self._A = [[(None,) for x in range(self._size*2)],[(None,) for x in range(self._size*2)]]
			self._hash = random.random()
			for x in old:
				if x[0] is not None:
					self.__setitem__(x[0],x[1])
			for x in old1:
				if x[0] is not None:
					self.__setitem__(x[0],x[1])
		else:
			if self._A[0][self.hash0(k)%len(self._A[0])][0] == k:
				self._A[0][self.hash0(k)%len(self._A[0])] = (k,v)
			else:
				self._A[1][self.hash1(k)%len(self._A[1])] = (k,v)

	def __delitem__(self,k):
		if k not in self:
			raise KeyError("Stop trying to be smart")
		else:
			if self._A[0][self.hash0(k)%len(self._A[0])][0] == k:
				self._A[0][self.hash0(k)%len(self._A[0])] = (None,)
			else:
				self._A[1][self.hash1(k)%len(self._A[1])] = (None,)
			self._size -=1 

	def __len__(self): return self._size

	def __contains__(self,key):
		if self._A[0][self.hash0(key)%len(self._A[0])][0] == key:
			return True
		if self._A[1][self.hash1(key)%len(self._A[1])][0] == key:
			return True
		return False

	def __iter__(self): yield from self.keys()

	def keys(self): yield from [i[0] for i in self.items()]

	def values(self): yield from [i[1] for i in self.items()]

	def items(self):
		for i in range(len(self._A[1])):
			if self._A[0][i][0] is not None: yield self._A[0][i]
			if self._A[1][i][0] is not None: yield self._A[1][i]


T=HT()

for i in range(200):
	T[i]=i*i

for i in T.keys():
	T[i]=T[i]+1

for i in range(5,400):
	if i in T:
		del T[i]

K=list(T.items())
K.sort()
print(K)
print(len(K))