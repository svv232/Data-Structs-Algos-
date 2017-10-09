class PQ:
    class _Node: 
        def __init__(self,left,right,data): self._left, self._right, self._data = left,right,data
    
    def __init__(self,n=None): self._root = n
    
    def flip(self,node): node._left,node._right = node._right,node._left
    
    def _merge_left(self,node1,node2):
        if node1 is None: return node2
        if node2 is None: return node1
        if node1._data < node2._data:
            node1._left = self._merge_left(node2,node1._left)
            self.flip(node1)
            return node1
        else:
            node2._left = self._merge_left(node1,node2._left)
            self.flip(node2)
            return node2
    
    def merge(self,heap): self._root = self._merge_left(self._root,heap._root)
    
    def insert(self,v): self.merge(PQ(self._Node(None,None,v)))
    
    def extractMin(self):
        minimum = self._root._data
        self._root = self._merge_left(self._root._left,self._root._right)
        return minimum
