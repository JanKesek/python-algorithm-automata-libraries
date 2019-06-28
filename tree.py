import queue
import random
import math
class Node:
	def __init__(self, data):
		self.data=data
		self.children=[]
		self.weight={}
	def insert_child(self, children):
		self.children.append(children)
		self.weight[self.data, children.data]=random.randint(0,500)
		
def dfs(curr, prev,weightList):
	#subtreeNodes[curr.data]=0
	print("Node: ", curr.data)
	for node in curr.children:
		#weightList[curr.data, node.data]=curr.weight[curr.data, node.data]
		if node.data is not prev: 
			dfs(node, curr.data, subtreeNodes)
			#subtreeNodes[node.data]=len(node.children)
			#subtreeNodes[curr.data]+=subtreeNodes[node.data]
	#return weightList
def linearSearch(lst,n):
	i=0
	while i<len(lst):
		if lst[i]==n: return i
		i+=1
	return False
def insertionSort(lst):
	for i in range(len(lst)):
		key=lst[i]
		j=i-1
		while j>=0 and lst[j]>key:
			lst[j+1]=lst[j]
			j-=1
		lst[j+1]=key
	return lst
def iterFib(n):
	i=1
	x=1
	y=0
	while i<n:
		z=x
		x+=y
		y=z
		i+=1
	return x


listOfNodes=[]
for i in range(1,8):
	listOfNodes.append(Node(i))
root=listOfNodes[0]
root.insert_child(listOfNodes[1])
root.insert_child(listOfNodes[2])
second=listOfNodes[1]
second.insert_child(listOfNodes[3])
second.insert_child(listOfNodes[4])
fifth=listOfNodes[4]
fifth.insert_child(listOfNodes[5])
third=listOfNodes[2]
third.insert_child(listOfNodes[6])


subtreeNodes={}
subtreeNodes[0]=0
sN=dfs(root, 0,subtreeNodes)
print(sN)
#for node in listOfNodes:
#	print(node.weight)
t=[]
w=[]
for i in range(100000):
	w.append(random.randint(0,2000000000))
for i in range(0,10000):
	t.append(w[random.randint(0,len(w)-1)])

#print(linearSearch(t,32))
#print(t)
#st=insertionSort(t)
#print(st)
#for i in range(0,1000):
#	print(iterFib(i))