#---------------
'''
Sai Vegasena
svv232
'''

#1
'''
Examples
1. O(N)
2. O(N)
3. O(N^2)
4. O(N)
5. O(N^3)
'''
#2
def merge(l1, l2):
	for i in range(min(len(l1), len(l2))):
		yield l1[i]
		yield l2[i]
	if len(l1) < len(l2):
		for i in l2[1:len(l2) - len(l1) + 1]:
			yield i
	else:
		for i in l1[1:len(l1) - len(l2) + 1]:
			yield i
#3
class polynomial():
	def __init__(self, coefficients):
		self.coefficients = coefficients
	def __str__(self):
		return "".join([str(self.coefficients[x])+"x^"+str(len(self.coefficients) - x - 1)+"+"for x in range(len(self.coefficients) - 1)]) + str(self.coefficients[-1])
	def evaluate(self,n):
		return sum([n**x*self.coefficients[len(self.coefficients) - x - 1] for x in range(len(self.coefficients))])

#4
def sigma(f,i,b):
	return sum([f(i + x) for x in range(b - i + 1)])
