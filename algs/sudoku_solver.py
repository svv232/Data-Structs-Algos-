import sys
sys.setrecursionlimit(15000)

#Can Solve Sudoku Boards of Expert Difficulty if input is in the format of a 2d array
#Made with no external theorem provers or z3
#solvs board from 0-2 seconds depending on difficulty

class Board:
	class _item:
		def __init__(self,f):
			self._p = set(range(1,10))
			self._f = f

		def p(self):
			return self._p

		def f(self):
			return self._f

	def __init__(self,A):
		self._grid = {}
		self._board = [list(map(self._item,i)) for i in A]
		self._scount = 0
		for box in range(9):
			for row in range(9):
				if isinstance(self._board[box][row]._f,int):
					self._scount += 1
				self._grid[self._board[box][row]] = (box,row)

	def item_override(self,item,data):
		if isinstance(data,int) and isinstance(item._f,str):
			self._scount += 1
		elif isinstance(data,str) and isinstance(item._f,int):
			self._scount -= 1
		x,y = self._grid[item]
		self._board[x][y] = self._item(data)
		self._grid[self._board[x][y]] = (x,y)

	def row_valid(self):
		c = lambda x: x[0] == x[1]
		board = self.board()
		rc = zip([sum([1 for i in x if isinstance(i,int)]) for x in board],[len(set([x for x in i if isinstance(x,int)])) for i in board])
		return all(map(c,rc))

	def square_valid(self): #fix this
		c = lambda x: x[0] == x[1]
		usets = map(len,[self._square_collect(i,j) for i in range(0,7,3) for j in range(0,7,3)])
		ulists = map(len,[[self._board[y+i][x+j]._f for i in range(3) for j in range(3) if
		isinstance(self._board[y+i][x+j]._f,int)] for x in range(0,7,3) for y in range(0,7,3)])
		return all(map(c,zip(usets,ulists)))
        
        def column_valid(self):
                space_remove = lambda x: (x.difference_update(' '),x)[1]
                remake = lambda x: len([i for i in x if isinstance(i,int)])
                c = lambda x: x[0] == x[1]
                col = map(remake,zip(*self.board()))
                colsets = map(len,map(space_remove,map(set,zip(*self.board()))))
                return all(map(c,zip(col,colsets)))

	def is_valid(self):
		return self.column_valid() and self.row_valid() and self.square_valid()

	def is_solved(self):
		return self._scount == 81 and self.is_valid()

	def _remove(self,i,uset):
		if isinstance(i._f,str):
			i._p.difference_update(uset)
			if len(i._p) == 1:
				i._f = i._p.pop()
				self._scount += 1
				self.x_solve(i)

	def print(self):
		for i in self._board:
			print([x._f for x in i])

	def board(self):
		return [[i._f for i in x] for x in self._board]
	
	def x_solve(self,i):
		self.row_update(self._grid[i][0])
		self.column_update(self._grid[i][1])

	def _square_collect(self,cols=0,rows=0):
		uset = {self._board[rows+i][cols+j]._f for i in range(3) for j in range(3) if
		isinstance(self._board[rows+i][cols+j]._f,int)}
		return uset

	def _row_collect(self,rows=0):
		return {i._f for i in self._board[rows] if i._f != " "}

	def _column_collect(self,cols=0):
		return {self._board[i][cols]._f for i in range(9) if self._board[i][cols]._f != " "}

	def square_update(self,cols=0,rows=0):
		uset = self._square_collect(cols,rows)
		[self._remove(self._board[rows+i][cols+j],uset) for i in range(3) for j in range(3)]

	def row_update(self,rows=0):
		uset = self._row_collect(rows)
		[self._remove(i,uset) for i in self._board[rows]]

	def column_update(self,cols=0):
		uset = self._column_collect(cols)
		[self._remove(self._board[i][cols],uset) for i in range(9)]

	def __iter__(self):
		for i in self._board:
			for j in i:
				if len(j.p()) > 0:
					yield j
def _solve(B):
	for i in range(0,7,3): 
		for j in range(0,7,3):
			B.square_update(i,j)
	for i in range(9):
		B.row_update(i)
		B.column_update(i)


def DTS(B,prev=None):
	_solve(B)
	if not B.is_solved():
		if not B.is_valid():
			return prev
		item = min(B.__iter__(),key = lambda x: len(x.p()))
		prev = B
		while item.p():
			i = item.p().pop()
			B.item_override(item,i)
			board = DTS(Board(B.board()),prev)
			if board.is_solved():
				return board
	return B





A = [[5,' ',' ',' ',' ',4,' ',' ',6],
	[' ',' ',' ',5,7,' ',' ',' ',' '],
	[2,' ',7,' ',' ',' ',' ',' ',' '],
	[' ',9,5,' ',2,1,' ',' ',3],
	[' ',' ',6,3,' ',8,' ',5,9],
	[' ',7,' ',' ',' ',' ',' ',' ',4],
	[6,' ',' ',' ',3,' ',8,' ',' '],
	[8,' ',' ',4,1,' ',' ',' ',5],
	[' ',5,4,8,6,' ',' ',' ',' ',]]

C = [[' ',' ',' ',2,' ',' ',' ',6,3],
[3,' ',' ',' ',' ',5,4,' ',1],
[' ',' ',1,' ',' ',3,9,8,' '],
[' ',' ',' ',' ',' ', ' ',' ',9,' '],
[' ',' ',' ',5,3,8,' ',' ',' '],
[' ',3,' ',' ',' ',' ',' ',' ',' '],
[' ',2,6,3,' ',' ',5,' ',' '],
[5,' ',3,7,' ',' ',' ',' ',8],
[4,7,' ',' ',' ',1,' ',' ',' ']]

D = [[' ',' ',' ',2,4,' ',' ',' ',' '],
[6,' ',' ',' ',3,9,' ',8,2],
[' ',' ',' ',6,' ',' ',7,' ',' '],
[8,7,' ',' ',' ',' ',5,' ',6],
[' ',' ',1,' ',2,' ',9,' ',' '],
[3,' ',2,' ',' ',' ',' ',4,1],
[' ',' ',5,' ',' ',2,' ',' ',' '],
[2,8,' ',5,9,' ',' ',' ',3],
[' ',' ',' ',' ',6,3,' ',' ',' ']]

E = [[' ',' ',' ',7,' ',9,' ',4,1],
[' ',4,7,' ',6,1,8,2,' '],
[1,' ',' ',' ',' ',2,7,' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',4],
[9,3,4,' ',8,' ',' ',' ',' '],
[' ',8,6,2,' ',' ',' ',' ',' '],
[' ',' ',' ',6,' ',' ',2,' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',2,' ',' ',' ',9,6,' ']]


E =[[' ',' ',' ',7,' ',9,' ',4,1],
[' ',4,7,' ',6,1,8,2,' '],
[1,' ',' ',' ',' ',2,7,' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',4],
[9,3,4,' ',8,' ',' ',' ',' '],
[' ',8,6,2,' ',' ',' ',' ',' '],
[' ',' ',' ',6,' ',' ',2,' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',2,' ',' ',' ',9,6,' ']]


F = [[ 2 ,' ',1,' ',' ',7,' ',5,' '],
[' ',7,4,1,' ',5,3,' ',' '],
[' ',' ',' ',' ',2,6,' ',' ',' '],
[3,' ',' ',' ',' ',' ',2,' ',' '],
[8,' ',5,' ',7,2,' ',4,' '],
[' ',' ',7,' ',' ',4,' ',1,' '],
[' ',' ',3,' ',' ',' ',' ',' ',' '],
[' ',5,' ',' ',4,1,' ',' ',' '],
[' ',' ',2,' ',' ',' ',4,' ',' ']]


a = Board(A)
b = Board(B)
c = Board(C)
d = Board(D)
e = Board(E)
f = Board(F)



A = [b]

for j in A:
	DTS(j).print()
	print('------------------------')
