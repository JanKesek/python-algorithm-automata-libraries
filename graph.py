import queue
import random
import math
class Graph:
	class Edge:
		def __init__(self):
			self.y=0
			self.weight=0
			next = None
	def __init__(self, directed):
		self.numbVertices=0
		self.numbEdges=0
		self.directed=directed
		degs=[]
		edges=[]
		for i in range(0,1000):
			degs.append(0)
			edges.append(None)
		self.degree=degs
		self.edges=edges
		self.finished=False
	def backtrack(self, lst, k, input):
		c=[]
		if isSolution(lst,k,input):
			process_solution(lst,k,input)
		else:
			k=k+1
			ncandidates,c=construct_candidates(lst,input,c,ncandidates)
			for i in range(0,ncandidates):
				lst[k]=c[i]
				make_move(lst,k,input)
				backtrack(lst,k,input)
				unmake_move(lst,k,input)
				if finished: return
	def isSolution(self,lst,k,n):
		return k==n
	def construct_candidates(self,lst,input,c,ncandidates):
		c.append(True)
		c.append(False)
		ncandidates=2
		return ncandidates,c
	def read_graph(self, nOfEdges, nOfVertices, xVertInEdge,yVertInEdge,directed):
		self.numbVertices=nOfVertices
		for i in range(0,nOfEdges):
			self.insert_edge(xVertInEdge[i],yVertInEdge[i],directed)
	def insert_edge(self, x,y,directed):
		p = self.Edge()
		p.weight=random.randint(0,1000)
		p.y=y
		p.next=self.edges[x]
		self.edges[x]=p
		self.degree[x]+=1
		if directed is False: self.insert_edge(y,x,True)
		else: self.numbEdges+=1
	def print_graph(self):
		for i in range(1, self.numbVertices+1):
			print("Node ", i,": ")
			p=self.edges[i]
			while p is not None:
				print(p.y)
				p=p.next
	def init_search(self, start, method):
		p = []
		d =[]
		pr=[]
		for i in range(0, 500):
			p.append(False)
			d.append(False)
			pr.append(-1)
		self.processed=p
		self.discovered=d
		self.parent=pr
	
		if method=="bfs": self.bfs(start)
		else: self.dfs(start)
	def bfs(self, start):
		q1 = queue.Queue()
		q1.put(start)
		self.discovered[start]=True
		while q1.empty() is False:
			v=q1.get()
			self.process_vertex_early(v)
			self.processed[v]=True
			p=self.edges[v]
			while p is not None:
				y=p.y
				if (self.processed[y] is False) or (self.directed):
					self.process_edge(v,y)
				if not self.discovered[y]:
					q1.put(y)
					self.discovered[y]=True
					self.parent[y]=v
				p=p.next
			self.process_vertex_late(v)
	def dfs(self, start):
		if self.processed[start]: return;
		self.processed[start]=True
		print("Node: ")
		print(start)
		p=self.edges[start]
		u=p.y
		n=p.next.y
		print("Edges of this node:")
		print(u, n)
		self.dfs(u)
	def treeDFS(self, currentNode,previousNode):
		print("Node: ", currentNode)
		u=self.edges[currentNode]
		if u is not None: print(u.y)
		if u.next is not None: print(u.next.y)
		if previousNode !=0:
			t=self.edges[previousNode]
			print(previousNode, t.y, t.next.y)
		for e in self.edges:
			if e is not None:
				if e.y == currentNode and e.next is not None:
					self.treeDFS(e.next.y, currentNode)
		#if u.y != previousNode: 
		#	self.treeDFS(u.y, currentNode)
		#	self.treeDFS(u.next.y, currentNode)
	def hasCycle(self):
		return self.numbEdges!=self.numbVertices-1
	def isBipartite(self, start, colors, color):
		if start in colors: return False
		colors[start]=color
		edges=self.edges[start]
		p= edges.y
		pNext=edges.next.y
		currentColor=colors[start]
		if p in colors:
			if colors[p]==colors[start] or colors[pNext]==colors[start]:
				return False
		if colors[start]=="blue": 
			colors[p]="red"
			colors[pNext]="red"
		if colors[start]=="red": 
			colors[p]="blue"
			colors[pNext]="blue"
		self.isBipartite(p, colors, colors[p])
		if len(colors)==self.numbVertices: return True
		else: return False
	def process_vertex_late(self,v):
		return
	def process_vertex_early(self,v):
		print("Processed vertex: ", v)
	def process_edge(self,x,y):
		print("Processed edge: ", x,y)
	def find_path(self, start,end, parents):
		if start is end or end==-1:
			print(start)
		else:
			self.find_path(start, self.parent[end], self.parent)
			print(end)
	def bellManFord(self,start):
		e=[]
		for i in range(self.numbVertices+1): e.append(math.inf)
		e[start]=0
		for i in range(1,self.numbVertices):
			for vertice in range(1,self.numbVertices):
				edge=self.edges[vertice]
				if edge is not None:
					e[edge.y]=min(e[edge.y],e[vertice]+edge.weight)
		return e
g1 = Graph(False)
#make graph by input:numbOfEdges,numbOfVertices, [v[0][0],v[0][1]...],[v[1][0], v[1][1]...]
g1.read_graph(6,5,[1,1,4,2,2,5],[4,2,5,5,3,3], False)
#g1.print_graph()
#g1.init_search(1, "dfs")
print(g1.hasCycle())
#parents =[]
#parents.append(g1.parent[4])
#g1.find_path(1,4,g1.parent)
colors={}
colors[1]="blue"
#print(g1.isBipartite(1, colors,"blue"))
print(g1.bellManFord(1))
tree1= Graph(False)
tree1.read_graph(6,7,[1,1,1,4,4,2],[4,5,2,3,7,6], False)
edges= tree1.edges
for e in edges:
	if e is not None:
		print(e.y,e.next.y,e.weight)

tree1.treeDFS(1,0)