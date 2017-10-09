import random
class BST:
    class _Node:
        def __init__(self,parent,left,right,data):
            self._left=left
            self._right=right
            self._parent=parent
            self._data=data
    class Position:
        def __init__(self,node,bst):
            self._node = node
            self._bst = bst
        def element(self):
            return self._node._data

    def __init__(self):
        self._root=None
        self._size = 0

    def _make_position(self,node):
        return self.Position(node,self)

    def first(self):
        return self._make_position(self._min())

    def last(self):
        return self._make_position(self._max())

    def before(self,p):
        return self._make_position(p._node._left)

    def after(self,p):
        return self._make_position(p._node._right)

    def insert(self,x):
        if self._root == None:
            self._root=BST._Node(None,None,None,x)
        else:
            self._rec_insert(self._root,x)
        self._size += 1
    
    def _rec_insert(self,n,x):
        if x<n._data:
            if n._left == None:
                n._left=BST._Node(n,None,None,x)
            else:
                self._rec_insert(n._left,x)
        else:
            if n._right == None:
                n._right=BST._Node(n,None,None,x)
            else:
                self._rec_insert(n._right,x)
    
    def depth(self,x,n=None,depth=0):
        if n is None:
            n = self._root
        if x == n._data:
            return depth
        if n._left and x < n._data:
            return self.depth(x,n._left,depth+1)
        elif n._right and x > n._data:
            return self.depth(x,n._right,depth+1)

    def pos_le(self,x):
        node = self._rec_search_le(self._root,x)[1]
        if node:
            return self._make_position(node)
        return self._make_position(self._Node(None,None,None,None))

    def search_le(self,x):
        if self._root==None:
            return None
        else:
            le = self._rec_search_le(self._root,x)
            if le is None:
                return le
            return le[0]

    def _rec_search_le(self,n,x):
        if x<n._data:
            if n._left:
                return self._rec_search_le(n._left,x)
            else:
                return None,None
        else:
            if n._right:
                rv=self._rec_search_le(n._right,x)
                if rv:
                    return rv
                else:
                    return (n._data,n)
            else:
                return (n._data,n)

    def in_order(self,n=None):
        if n is None:
            n = self._root
        if n._left:
            yield from self.in_order(n._left)
        yield n._data,self.depth(n._data),n
        if n._right:
            yield from self.in_order(n._right)

    def __iter__(self):
        for i in self.in_order():
            yield i[0]

    def __len__(self): return self._size

    def _min(self,n=None):
        if n is None: n = self._root
        if n._left is None: return n
        else: return self._min(n._left)

    def _max(self,n=None):
        if n is None: n = self._root
        if n._right is None: return n
        else: return self._max(n._right)

    def _search_ge(self,n,x):
        if x > n._data:
            if n._right:
                return self._search_ge(n._right,x)
            else:
                return None,None
        else:
            if n._left:
                lv = self._search_ge(n._left,x)[1]
                if lv:
                    return lv,lv
                else:
                    return (n._data,n)
            else:
                return (n._data,n)

    def pos_ge(self,x):
        node  = self._search_ge(self._root,x)[1]
        if node:
            return self._make_position(node)
        return self._make_position(self._Node(None,None,None,None))
    
    def search_ge(self,x):
        if self._root is None:
            return None
        if isinstance(self._search_ge(self._root,x),tuple):
            return self._search_ge(self._root,x)[0]
        return self._search_ge(self._root,x)._data

    def range(self,x,y):
            for i in self.in_order():
                if i[0] >= x and i[0] <=y:
                    yield i[0]

    def pos_range(self,x,y):
        for i in self.in_order():
            if i[0] >= x and i[0] <=y:
                yield self._make_position(i[2])

    def print(self):
        ls = list(self.in_order()) 
        height = max(ls, key=lambda y:y[1])[1]
        for d in range(height + 1):
            print("".join(str(ls[i][0]) if ls[i][1] == d else "  " for i in range(len(ls))))

T=BST()
B=BST()
H=BST()

l = [32,16,48,8,24,40,56,4,12,20,28,36,44,52,60,2,6,10,14,18,22,26,30,34,38,42,46,50,54,58,62,1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63]
for i in l:
    B.insert(i)

for i in [0,20,1,19,2,18,3,17,4,16,5,15,6,14,7,13,8,12,9,11]:
    H.insert(i)

for i in [50,40,70,20,60,90,10,30,80]:
    T.insert(i)

print('\n')
T.print()
print("-------------------------------------------------------------------")
B.print()
print("-------------------------------------------------------------------")
H.print()
