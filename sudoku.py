import queue

class BoardType:
	class Point:
		def __init__(self,x,y):
			self.x=x
			self.y=y
			self.element
	def __init__(self,dimension,matrix,openSqCount, move):
		self.dimension=dimension
		self.matrix=matrix
		self.openSqCount=openSqCount
		self.move=move

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
	def construct_candidates(self,lst,k,c,ncandidates):
		possible=[]
		x,y=next_square()
		self.move[k].x=x
		self.move[k].y=y
		ncandidates=0
		if x<0 and y<0: return
		possible=possible_values(x,y)
		for i in range(self.dimension):
			if possible[i] == True:
				c.append(i)
	def next_square(self):
		bestSqCount=self.dimension+1
		doomed=False
		x=y=-1
		for i in range(self.dimension):
			for j in range(self.dimension):
				newSqCount = self.possible_count(i,j)
				if newSqCount == 0 and self.matrix[i][j]==0:
					doomed=True
				if newSqCount< bestSqCount and newSqCount >=1:
					bestSqCount=newSqCount
					x=i
					y=j
		return x,y
	def possible_count(self,x,y):
		cnt=0
		for i in range(self.dimension):
			print("DODAj POSSIBLE VALUES")
		return cnt
#g1 = Graph(False)
#make graph by input:numbOfEdges,numbOfVertices, [v[0][0],v[0][1]...],[v[1][0], v[1][1]...]
#g1.read_graph(3,4,[1,1,2],[2,3,4], False)
#g1.print_graph()
#g1.init_search(1)
#parents =[]
#parents.append(g1.parent[4])
#g1.find_path(1,4,g1.parent)