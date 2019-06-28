import queue
import random
import math
class NodeList:
	def __init__(self, data):
		self.data=data
		self.prev=None
		self.next=None
	def getList(self,t=[]):
		if self.prev is not None: self.prev.getList()
		else:
			if self.next is not None: self.next.getList() 
		t.append(self.data)
		return t
	def insertPrevious(self,oldNode, newNode):
		if oldNode.prev!=None: 
			self.insertPrevious(oldNode.prev, newNode)
		else: oldNode.prev=newNode
	def insertNext(self,oldNode,newNode):
		if oldNode.next!=None:
			self.insertNext(oldNode.next,newNode)
		else: oldNode.next=newNode
def recurMultiplic(n,k):
	while k>0 and n>0:
		if k==1: return n
		else: 
			w= n+recurMultiplic(n,k-1)
			return w
	return 0
n1=NodeList(15)
n2=NodeList(42)
n3=NodeList("dsad")
n1.insertPrevious(n1,n2)
n1.insertPrevious(n2,n3)
n1.insertNext(n3,n1)
#print(n1.getList())
print(recurMultiplic(443,32))