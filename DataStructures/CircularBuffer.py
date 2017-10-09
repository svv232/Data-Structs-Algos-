class CircularBuffer:   
	def __init__(self,maxsize):
		self.len,self.data,self._finger,self.maxsize, = 0,[None for x in range(maxsize)],0,maxsize

	def is_empty(self):
		return self.len == 0

	def push(self,x):
			self.data[self._finger] = x
			self._finger = (self._finger+1) % self.maxsize 
			if self.len <= self.maxsize: self.len += 1

	def pop(self):
		if self.len == 0: return 
		self.data[self._finger-1] = None
		self._finger = (self._finger-1) % self.maxsize
		self.len -= 1

	def __str__(self):
		print(str(self.data))
		return "["+",".join([str(self.data[i]) for i in range(self.maxsize) if self.data[i] != None]) + ']'

	def __len__(self): return self.len
