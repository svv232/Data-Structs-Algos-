class Heap: #implementation for a max binomial heap within a list log(n) operations
    def __init__(self):
        self._h = [] #heap array

    def p(self,n): #parent
        return (n-1)//2

    def _bubble_up(self,n):
        if not (n == 0) and self._h[n] > self._h[self.p(n)]:
            self._h[n],self._h[self.p(n)] = self._h[self.p(n)],self._h[n]
            self._bubble_up(self.p(n))
            return

    def insert(self,e):
        self._h.append(e)
        self._bubble_up(len(self._h)-1)

    def c(self,n):  #children
        if 2*n +1 < len(self._h)-1:
            yield 2*n +1
        if 2*n +2 < len(self._h)-1:
            yield 2*n+2

    def _bubble_down(self,n=0):
        try:big = max(self.c(n),key=lambda x: self._h[x])
        except: return self._h.sort(),self._h.reverse() 
        if self._h[n] < self._h[big]:
            self._h[n],self._h[big] = self._h[big],self._h[n]
            self._bubble_down(big)


    def _remove_max(self):
        self._h[0] = self._h.pop()
        self._bubble_down()


    def max(self):
        if len(self._h) > 0:
            maximum = self._h[0]
            self._remove_max() if len(self._h)>1 else self._h.pop()
            return maximum

    def heap_sort(self):
        while self._h: yield self.max()

        
from random import shuffle

ls = [x for x in range(99)]
shuffle(ls)
h = Heap()
[h.insert(i) for i in ls]
print([x for x in h.heap_sort()])
