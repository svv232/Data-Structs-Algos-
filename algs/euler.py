#First Page of Prject Euler Solutions
#1
print(sum([x for x in range(1000) if x%3 == 0 or x%5 == 0])) 
#-------------------------------------------------------------------
#2
def fibb(n):
	a = 1
	b = 2
	c = a + b
	total = 2
	while (a + b) < n:
		if (a + b) % 2 == 0:
			total += a + b
		a = b
		b = c
		c = a + b
	return total

#-------------------------------------------------------------------

#4
def largest_palindrome():
	for i in range(999,99,-1):
		for j in range(999,99,-1):
			p = i * j
			print(j)
			if str(p)[::] == str(p)[::-1]:
				return p

#-------------------------------------------------------------------
def small_divisible():
		count = 20
		while count != 0:
			if len([count%x for x in range(1,21) if count%x == 0]) == 20:
				return count
			count += 1
print(small_divisible())

#-------------------------------------------------------------------
#6
print((sum([x for x in range(1,101)])**2) - sum([x**2 for x in range(1, 101)]))

#-------------------------------------------------------------------
#7
def prime_num(n):
	count = 1
	counter = 2
	while count < n:
		counter += 1
		if len([(counter % x) for x in range(2,counter) if counter % x == 0]) <= 0:
			count += 1
	return counter

#-------------------------------------------------------------------
#8
def multiplier(string):
	product = 1
	for i in string:
		product *= int(i)
	return product

#-------------------------------------------------------------------
def adjacent_product(number, filename):
	maximum = 0
	with open(filename,'r') as numberf:
		line = numberf.readlines()[0]
	for i in range(len(line)):
		if i + number < 999:
			if multiplier(line[i:i + number]) > maximum:
				maximum = multiplier(line[i:i + number])
	return maximum


#-------------------------------------------------------------------
#9
def triplet():
	a = 1
	c = 0
	d = [x for x in range(2,1000) if x > a]
	b = d[c]
	while a > 0:
		while c < len(d) - 1:
			if (a**2 + b**2)**.5 == int((a**2 + b**2)**.5):
				if a + b + (a**2 + b**2)**.5 == 1000:
					return a * b * (a**2 + b**2)**.5
			c += 1
			b = d[c]
		a += 1
		d = [x for x in range(2,1000) if x > a]
		c = -1

#-------------------------------------------------------------------
def get_primes_sum(n):
	numbers = set(range(n, 1, -1))
	primes = []
	while numbers:
		#print(numbers)
		#print(primes)
		p = numbers.pop()
		primes.append(p)
		numbers.difference_update(set(range(p*2, n + 1, p)))
		#print(p)
		#print(set(range(p*2, n + 1, p)))
		#print(numbers)
	return (primes)

print(get_primes_sum(10))

#-------------------------------------------------------------------

#12

def sum_calc(filename):
	with open(filename, 'r') as file:
		f = file.readlines()
	total = 0
	for i in range(len(f)):
		total += int(f[i].strip())
	return str(total)[0:10]

print(sum_calc("thenum.txt"))

#-------------------------------------------------------------------
#print(sum(map(int, (list(str(2 ** 1000))))))

def triangle(filename):
	with open(filename, 'r') as file:
		ls = file.readlines()
	print(ls)

triangle("triangle.txt")


class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance

def dijsktra(graph, initial):
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes: 
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph.edges[min_node]:
      weight = current_weight + graph.distance[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

  return visited, path

#-------------------------------------------------------------------
def series(x):
	return str(sum(x**x for x in range(1, x + 1)))[-10:]

print(series(1000))

#-------------------------------------------------------------------
def get_primes(n):
	numbers = set(range(n, 1, -1))
	primes = []
	while numbers:
		p = numbers.pop()
		primes.append(p)
		numbers.difference_update(set(range(p*2, n + 1, p)))
	return primes


#-------------------------------------------------------------------
def consecutive_prime_sum(y):
	x = get_primes(1000000)
	maximum = 0
	i = 0
	while sum(x[0:i]) <= y:
		if sum(x[0:i]) in x and sum(x[0:i]) > maximum:
			maximum = sum(x[0:i])
			print(maximum)
		i += 1
	return maximum

print(consecutive_prime_sum(100000000))

#-------------------------------------------------------------------
def not_palins(l):
	return [x for x in l if x != x[::-1]]

def dub_palindrome():
	total = 0
	x = list(str(i) for i in range(1000000) if (str(i)[::-1] == str(i)))
	print(x)
	x2 = map(int, (x))
	y = list(str(bin(i))[2:] for i in x2 if str(bin(i))[2:] == str(bin(i))[2:][::-1])
	print(y)
	for i in x2:
		if str(bin(i))[2:] in y:
			total += i
	return total

print(dub_palindrome())

#-------------------------------------------------------------------
def sum_factorial(i):
	p = 1
	for j in range(1, i + 1):
		p *= j
	return sum(map(int, (list(str(p)))))

print(sum_factorial(100))

#-------------------------------------------------------------------
def name_scores(filename):
	score = 0
	name = 0
	alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
	with open(filename, "r") as file:
		x = file.readline().split(",")
		y = [i[1:-1] for i in x]
	for i in range(len(y)):
		for j in y[i]:
			if j in alpha:
				name += alpha.index(j) + 1
		score += name * (i + 1)
		name = 0
	print(y)
	return y.index("DELBERT")



print(name_scores("name.csv"))

#-------------------------------------------------------------------
line(self.t[n - 1] * 30, self.t[n - 1], (self.t[n] * 30, self.t[n])

#24
def partitions(numbers, spaces,lp):
	product = 1
	for i in range(1, spaces):
		product *= i
	return [numbers[lp // product], lp % product]

#-------------------------------------------------------------------
def main():
	string = ""
	x,y,z = [0,1,2,3,4,5,6,7,8,9],10, 1000000
	for i in range(10):
		print(x)
		f = partitions(x,y,z)
		string += str(f[0])
		z = f[1]
		x.remove(f[0])
		y -= 1
	return string

print(main())

#-------------------------------------------------------------------
def triangle(file):
	checkers = [((.5 * n) * (n + 1)) for n in range(10000)]
	ls = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
	triangles = 0
	with open(file, 'r') as file:
		x = str(file.readlines()).split(',')[1:-2]
		y = [i[1:-1] for i in x] + ["A"] + ["YOURSELF"] +["YOUTH"]
	count = 0
	for i in y:
		count = 0
		for j in i:
			count += ls.index(j) + 1
		if count in checkers:
			triangles += 1
	return triangles
print(triangle('name.csv'))


#-------------------------------------------------------------------
#24
def partitions(numbers, spaces,lp):
	product = 1
	for i in range(1, spaces):
		product *= i
	return [numbers[lp // product], lp % product]

#-------------------------------------------------------------------
def main():
	string = ""
	x,y,z = [0,1,2,3,4,5,6,7,8,9],10, 999999
	for i in range(10):
		f = partitions(x,y,z)
		string += str(f[0])
		z = f[1]
		x.remove(f[0])
		y -= 1
	return int(string)

print(main())

#-------------------------------------------------------------------
y = ""
x = [str(x) for x in range(1,1000001)]
for i in x:
	y += i
print(y[0],y[9], y[99], y[999],y[9999],y[99999],y[999999])

def get_primes(n):
	numbers = set(range(n, 1, -1))
	primes = []
	while numbers:
		p = numbers.pop()
		primes.append(p)
		numbers.difference_update(set(range(p*2, n + 1, p)))
	return (primes)

y2 = [x for x in get_primes(7654321) if sorted(list(str(x))) == [str(i) for i in range(1, len(str(x))+1)]]
print(max(y2))

#-------------------------------------------------------------------
#2
def fibb(n):
	a = 1
	b = 2
	c = a + b
	count = 4
	while len(str((a + b))) != n:
		count += 1
		a = b
		b = c
		c = a + b
	return count

#-------------------------------------------------------------------
def get_primes(n):
	numbers = set(range(n, 1, -1))
	primes = []
	while numbers:
		p = numbers.pop()
		primes.append(p)
		numbers.difference_update(set(range(p*2, n + 1, p)))
	return (primes)

#-------------------------------------------------------------------
import itertools

def circular prime(n):
	count = 0
	ls = get_primes(10000000)
	for i in ls:

def get_primes(n):
	numbers = set(range(n, 1, -1))
	primes = []
	while numbers:
		p = numbers.pop()
		primes.append(p)
		numbers.difference_update(set(range(p*2, n + 1, p)))
	return (primes)

#-------------------------------------------------------------------
import itertools
o = get_primes(1000001)
print(sum([1 for z in [[i for i in [int("".join(x)) for x in itertools.permutations(str(y), len(str(y)))] if i not in o] for y in o] if z == []]))

def get_primes(n):
	numbers = set(range(n, 1, -1))
	primes = []
	while numbers:
		p = numbers.pop()
		primes.append(p)
		numbers.difference_update(set(range(p*2, n + 1, p)))
	return (primes)


def largest_prime_sum():
	y,x= get_primes(100000),get_primes(10000)
	while sum(x) not in y:
		x.pop()
	return sum(x)

print(largest_prime_sum())

#-------------------------------------------------------------------
y=set(range(1000000,2,-1))
def str_5(n):
	product = 0
	for i in str(n):
		product += int(i)**5
	if product == n:
		return True

print((sum([x for x in y if str_5(x)])))

#-------------------------------------------------------------------
import itertools

def checker(n):
	if int(n[1:4])%2:
		return False
	if int(n[2:5])%3:
		return False
	if int(n[3:6])%5:
		return False
	if int(n[4:7])%7:
		return False
	if int(n[5:8])%11:
		return False
	if int(n[6:9])%13:
		return False
	if int(n[7:10])%17:
		return False
	return True

#-------------------------------------------------------------------
x = sum(map(int,["".join(x) for x in itertools.permutations("0123456789",10) if checker("".join(x))]))
print(x)

import itertools

def get_primes(n):
	numbers = set(range(n, 1, -1))
	primes = []
	while numbers:
		p = numbers.pop()
		primes.append(p)
		numbers.difference_update(set(range(p*2, n + 1, p)))
	return (primes)

z = get_primes(10000)

#-------------------------------------------------------------------
def checker(n):
	if len(["".join(x) for x in itertools.permutations(str(n),len(str(n))) if int("".join(x)) in z ]) >= 4:
		return True
b = [i for i in z[999:] if checker(i)]

d = [["".join(x) for x in itertools.permutations(str(x),len(str(x))) if int("".join(x)) in z] for x in b]
for i in d:
	print(i)

def sorting(filename,filename2):
	file2 =  open(filename2, 'w') 
	with open(filename, 'r') as file:
		x = file.readlines()
		y = x[0].split(",")
	for i in y:
		file2.write("".join(i)[1:-1]+"\n")
	file2.close()

#-------------------------------------------------------------------
def points(filename):
	total = 0
	alpha = ["\n","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	with open(filename,"r") as afile:
		x = afile.readlines()
	for i in range(len(x)):
		total += sum([alpha.index(b) for b in x[i]]) * (i+1)
	return total

print(points("alpha.txt"))

def unique():
	ls = []
	for i in range(2,101):
		for j in range(2,101):
			ls.append(i**j)
	print(len(set(ls)))

unique()

#-------------------------------------------------------------------
