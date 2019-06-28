import queue
import random
import collections
import math
class Node:
	def __init__(self, data):
		self.data=data
		self.children=[]
		self.weight={}
	def insert_child(self, children, data):
		self.children.append(children)
		self.weight[self.data, children.data]=data
		
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
#for i in range(1,8):
#	listOfNodes.append(Node(i))

stateA=Node('A')
stateB=Node('B')
stateC=Node('C')
stateA.insert_child(stateB,1)
stateA.insert_child(stateC,1)
stateB.insert_child(stateB,[1,0])
#stateB.insert_child(stateB,0)
stateB.insert_child(stateC,1)
listOfNodes.append(stateA)
listOfNodes.append(stateB)
listOfNodes.append(stateC)


subtreeNodes={}
subtreeNodes[0]='A'
sN=dfs(stateA, 0,subtreeNodes)
print(sN)
for node in listOfNodes:
	print [item for item, count in collections.Counter(node.weight.values()).items() if count > 1]
	#print(node.weight)

#print(linearSearch(t,32))
#print(t)
#st=insertionSort(t)
#print(st)
#for i in range(0,1000):
#	print(iterFib(i))