#MIT OpenCourseWare Program Ideas from class

#Dynamic Fibbs
def fibbs(n, D=None):
    if D is None: D = {}
    if n in D: return D[n]
    if n > 2:
        D[n] = fibbs(n-1,D) + fibbs(n-2,D)
        print(D[n])
        return D[n]
    return 1 if n == 1 else 0
        
#Simple Pythonic Sieve of Erasthothenes
def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n + 1, p)))
    return primes

#minimal path sum only going right and down

def get_matrix(): #can also use matrix.txt for a much biger example!
    with open('matrix2.txt','r') as matrix:
        return [[int(x) for x in i.split(',')] for i in matrix.readlines()]

def minimal_path_sum(matrix = None,D = {},i=0,j=0): #dynamic solution
    if matrix is None:
        matrix = get_matrix()
        D = {}
    if (i,j) in D: return D[(i,j)]
    if i > len(matrix)-1 or j > len(matrix[0])-1: return 9999999
    elif not (i == len(matrix)-1 and j == len(matrix[0])-1):
        right = matrix[i][j] + minimal_path_sum(matrix,D,i+1,j)
        down = matrix[i][j] + minimal_path_sum(matrix,D,i,j+1)
        D[(i,j)] = min(right,down)
        return D[(i,j)]
    return matrix[i][j]

print(minimal_path_sum())
