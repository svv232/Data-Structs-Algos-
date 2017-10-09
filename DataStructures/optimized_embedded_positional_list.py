class PList:
    class _Node:
        __slots__='_data','_prev','_next'
        def __init__(self,data,prev,next):
            self._data=data
            self._prev=prev
            self._next=next
    class Position:
        def __init__(self,plist,node):
            self._plist=plist
            self._node=node
        def data(self):
            return self._node._data
        def __eq__(self,other):
            return type(other) is type(self) and other._node is self._node
        def __ne__(self,other):
            return not (self == other)
    def _validate(self,p):
        if not isinstance(p,self.Position):
            raise TypeError("p must be proper Position type")
        if p._plist is not self:
            raise ValueError('p does not belong to this PList')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node
    def _make_position(self,node):
        if node is self._head or node is self._tail:
            return None
        else:
            return self.Position(self,node)
    def __init__(self):
        self._head=self._Node(None,None,None)
        self._head._next=self._tail=self._Node(None,self._head,None)
        self._size=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def first(self):
        return self._make_position(self._head._next)
    def last(self):
        return self._make_position(self._tail._prev)
    def before(self,p):
        node=self._validate(p)
        return self._make_position(node._prev)
    def after(self,p):
        node=self._validate(p)
        return self._make_position(node._next)
    def __iter__(self):
        pos = self.first()
        while pos:
            yield pos.data()
            pos=self.after(pos)
    def _insert_after(self,data,node):
        newNode=self._Node(data,node,node._next)
        node._next._prev=newNode
        node._next=newNode
        self._size+=1
        return self._make_position(newNode)
    def add_first(self,data):
        return self._insert_after(data,self._head)
    def add_last(self,data):
        return self._insert_after(data,self._tail._prev)
    def add_before(self,p,data):
        node=self._validate(p)
        return self._insert_after(data,node._prev)
    def add_after(self,p,data):
        node=self._validate(p)
        return self._insert_after(data,node)
    def delete(self,p):
        node=self._validate(p)
        data=node._data
        node._prev._next=node._next
        node._next._prev=node._prev
        node._prev=node._next=node._data=None
        self._size-=1
        return data
    def replace(self,p,data):
        node=self._valdiate(p)
        olddata=node._data
        node._data=data
        return olddata
    def rev_itr(self):
        pos = self.last()
        while pos:
            yield pos.data()
            pos=self.before(pos)

class Counters:
    class _Item:
        def __init__(self,name):
            self._name=name
            self._count=0
    
    class Counter:
        def __init__(self,position,mc=None):
            self._position=position
            self._main_counter = mc
        def name(self):
            return self._position.data()._name
        def count(self):
            return self._position.data()._count 

    class Mini_Counters:
        def __init__(self):
            self._CPList = PList()
            self._L=PList() # serves as a separate plist that contains the size
            self._L._head._data = self._L._tail._data = 0
            self._L._head._prev = self._CPList._head
            self._L._tail._next = self._CPList._tail

        def new_mini_counter(self,name):
            self._CPList.add_last(Counters._Item(name))
            self._L._head._data += 1
            return Counters.Counter(self._CPList.last())

    def __init__(self):
        self._CPList = PList()
        self._L=PList() # serves as a separate plist that contains the size
        self._L._head._data = self._L._tail._data = 0
        self._L._head._prev = self._CPList._head
        self._L._tail._next = self._CPList._tail

    def new_counter(self,name):
        if self._CPList.last():
            self._CPList.last().data().new_mini_counter(name)
        else:
            self._CPList.add_last(Counters.Mini_Counters())
            self._CPList.last().data().new_mini_counter(name)
            self._L._head._data += 1
        return Counters.Counter(self._CPList.last().data()._CPList.last(),self._CPList.last())
        
    def _validateC(self,counter):
        if counter._main_counter._plist is not self._CPList:
            raise ValueError('counter does not belong to this Counter')
        return counter

    def delete_counter(self,counter):
        data = counter._position._plist.delete(counter._position)
        counter._main_counter.data()._L._head._data -= 1
        counter._position=None
        counter._main_counter=None
        return data

    def increment_counter(self,counter):
        counter = self._validateC(counter)
        counter._position._node._data._count += 1
        old_counter = counter._main_counter
        if counter._main_counter._node._prev is self._CPList._head:
            self._CPList.add_before(counter._main_counter,Counters.Mini_Counters())
            self._L._head._data += 1
        counter._position._plist = counter._main_counter._node._prev._data._CPList
        counter._main_counter._node._prev._data._L._head._data += 1
        new_position = counter._main_counter._node._prev._data._CPList.add_last(self.delete_counter(counter))  
        counter._main_counter = self._CPList.Position(self._CPList,old_counter._node._prev)
        counter._position = new_position

    def __iter__(self):
        position=self._CPList.first()
        while position:
            for i in position.data()._CPList:
                yield Counters.Counter(self._CPList.Position(self._CPList,self._CPList._Node(i,None,None)))
            position=self._CPList.after(position)

    def count_iter(self):
        position=self._CPList.first()
        yield self._L._head._data
        while position:
            yield position.data()._L._head._data
            position=self._CPList.after(position)

#--------TIME_CODE----------------------------------------------


import time
start_time = time.time()

D = Counters()

alphabet = { 
    "a":1,"b":2,"c":3,"d":4,"e":5,
    "f":6,"g":7,"h":8,"i":9,"j":10,
    "k":11,"l":12,"m":13,"n":14,"o":15,
    "p":16,"q":17,"r":18,"s":19,"t":20,
    "u":21,"v":22,"w":23,"x":24,"y":25,
    "z":26,"ab":12,'ac':45,'ad':13,'ae':34,
    'af':23,'ag':20,'ah':12,'ai':15,'aj':22,
    'ak':34,'al':24,'am':34,'an':21,'aa':2,
    'aaa':8,'aaaa':13,'bb':2,'bbb':2,"bj":2,
    'cc':2,'dd':2,'ee':2,'ff':2,'gg':2,'hh':2,
    'ii':2,'jj':2,'kk':2,'ll':2,'mm':2,'nn':2,
    'oo':2,'qq':2,'qa':31,'qb':11,'qc':2,'qd':2,
    'qq':3,"qqq":3,"qqqq":3,'qqqqq':3,"qqqqqq":3,
    'ff':3,'fff':3,'ffff':3,'ww':3,'www':3,'sai':3,
    'A':3,'B':3,'C':4,"D":4,"E":4,"F":4,"G":4,"H":4,
    "J":4,"K":4,"L":4,"M":4,"N":4,"O":4,"P":4,"Q":4,
    "R":4,"S":4,"T":4,"W":4,"U":4,"V":4,"X":4,"Y":4,
    "AA":12,"AAA":12,'AAAA':12,"BB":12,"BBB":12
}

counters = [D.new_counter(i) for i in alphabet.keys()]

for i in range(len(alphabet)):
    for cp in counters:
        if alphabet[cp.name()] > cp.count():
            D.increment_counter(cp)


print("IMPROVED--- %s seconds ---" % (time.time() - start_time))


for i in D:
    print(i.name(),i.count())


#-----------------------------------------------------------------------------------------
class Counters:
    class _Item:
        def __init__(self,name):
            self._name=name
            self._count=0
    class Counter:
        def __init__(self,position):
            self._position=position
        def name(self):
            return self._position.data()._name
        def count(self):
            return self._position.data()._count            
    def __init__(self):
        self._L=PList()
    def new_counter(self,name):
        self._L.add_last(Counters._Item(name))
        return Counters.Counter(self._L.last())
    def delete_counter(self,counter):
        self._L.delete(counter._position)
        counter._position=None
    def increment_counter(self,counter):
        counter._position.data()._count+=1
        before_position=self._L.before(counter._position)
        while (before_position and 
              before_position.data()._count
              < counter.count()):
            new_position=self._L.add_before(before_position,counter._position.data())
            self._L.delete(counter._position)
            counter._position=new_position
            before_position=self._L.before(counter._position)
    def __iter__(self):
        position=self._L.first()
        while position:
            yield Counters.Counter(position)
            position=self._L.after(position)

#-------------------------------------------------------------------------------------------
import time
start_time = time.time()

D = Counters()

alphabet = { 
    "a":1,"b":2,"c":3,"d":4,"e":5,
    "f":6,"g":7,"h":8,"i":9,"j":10,
    "k":11,"l":12,"m":13,"n":14,"o":15,
    "p":16,"q":17,"r":18,"s":19,"t":20,
    "u":21,"v":22,"w":23,"x":24,"y":25,
    "z":26,"ab":12,'ac':45,'ad':13,'ae':34,
    'af':23,'ag':20,'ah':12,'ai':15,'aj':22,
    'ak':34,'al':24,'am':34,'an':21,'aa':2,
    'aaa':8,'aaaa':13,'bb':2,'bbb':2,"bj":2,
    'cc':2,'dd':2,'ee':2,'ff':2,'gg':2,'hh':2,
    'ii':2,'jj':2,'kk':2,'ll':2,'mm':2,'nn':2,
    'oo':2,'qq':2,'qa':31,'qb':11,'qc':2,'qd':2,
    'qq':3,"qqq":3,"qqqq":3,'qqqqq':3,"qqqqqq":3,
    'ff':3,'fff':3,'ffff':3,'ww':3,'www':3,'sai':3,
    'A':3,'B':3,'C':4,"D":4,"E":4,"F":4,"G":4,"H":4,
    "J":4,"K":4,"L":4,"M":4,"N":4,"O":4,"P":4,"Q":4,
    "R":4,"S":4,"T":4,"W":4,"U":4,"V":4,"X":4,"Y":4,
    "AA":12,"AAA":12,'AAAA':12,"BB":12,"BBB":12
}



counters = [D.new_counter(i) for i in alphabet.keys()]

for i in range(len(alphabet)):
    for cp in counters:
        if alphabet[cp.name()] > cp.count():
            D.increment_counter(cp)

print("__________________________________________________________________________________________________________")
print("OIGINAL--- %s seconds ---" % (time.time() - start_time))
print("___________________________________________________________________________________________________________")
for i in D:
    print(i.name(),i.count())
