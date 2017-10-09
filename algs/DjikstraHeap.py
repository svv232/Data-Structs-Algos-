#An imlementation of djiktra's algorithm with a personalized graph class and 
#the python heapq module
class Graph:
	class Vertex:
		def __init__(self,label=None):
			self._label = label

		def label(self):
			return self._label

	class Edge:
		def __init__(self,origin,destination,distance):
			self._origin, self._destination,self._distance = origin,destination,distance

		def distance(self):
			return self._distance

	def __init__(self):
		self._graph = {}

	def add_vertex(self,label):
		v = self.Vertex(label)
		self._graph[v] = {}
		return v

	def add_edge(self,v1,v2,distance):
		e = self.Edge(v1,v2,distance)
		self._graph[v1][v2] = e
		self._graph[v2][v1] = e

	def vertices(self):
		yield from self._graph.keys()

	def incident_vertices(self,v):
		yield from self._graph[v].keys()

	def incident_edges(self,v):
		yield from self._graph[v].values()

	def get_edge(self,u,v):
		return self._graph[u][v]

import heapq
def djikstra(graph,start):
	heap = [(0,start)]
	visited = {start:0,}
	path = {}
	while heap:
		d,v = heapq.heappop(heap)
		
		for i in graph.incident_vertices(v):
			
			weight = d+graph.get_edge(v,i).distance()
			
			if i not in visited:
				visited[i] = weight
				heapq.heappush(heap,(weight,i))
				path[i] = v
			
			elif weight < visited[i]:
					visited[i] = weight
					path[i] = v

	return visited,path

def shortest_path(graph,start,end):
	v,p = djikstra(graph,start)
	while start != end:
		yield (end.label(),v[end])
		end = p[end]
	yield (start.label(),v[start])

g = Graph()
A  = ['A','B','C','D','E','F']
verts = {}

for i in A:
	verts[i] = g.add_vertex(i)

g.add_edge(verts['A'],verts['B'],3)
g.add_edge(verts['A'],verts['C'],5)
g.add_edge(verts['B'],verts['D'],7)
g.add_edge(verts['C'],verts['E'],8)
g.add_edge(verts['D'],verts['F'],1)
g.add_edge(verts['E'],verts['F'],2)
