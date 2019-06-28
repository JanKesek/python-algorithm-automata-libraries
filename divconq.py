import queue
import random
import math
import statistics
import sys
sys.setrecursionlimit(12000)
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

def binSearch(sortedList, left,right,s):
	if left==right:
		if sortedList[left]==s: return left
		else: return None
	q=(left+right)//2
	ret = binSearch(sortedList, left, q, s)
	if ret==None: return binSearch(sortedList,q+1,right,s)
	else: return ret
def betterBinSearch(sortedList,l,r,s):
	if l==r:
		if sortedList[l]==s: return l
		else: return None
	q=(l+r)//2
	if sortedList[q]<=s: return betterBinSearch(sortedList,l,q,s)
	else: return betterBinSearch(sortedList,q+1,r,s)
def selectionSort(lst):
	for i in range(len(lst)):
		min=i
		for j in range(i+1,len(lst)):
			if lst[j]<lst[min]: min=j
		lst[min],lst[i]=lst[i],lst[min]
	return lst
def bubbleSort(lst, count=0):
	for i in range(len(lst)):
		for j in range(len(lst)-1,i,-1):
			if lst[j]<lst[j-1]:
				tmp=lst[j]
				lst[j]=lst[j-1]
				lst[j-1]=tmp
				count+=1
	return lst
def combSort(lst,count=0):
	step=len(lst)
	swap=True
	while step>1 or swap:
		step=step*10//13
		if step==0:step=1
		swap=False
		for i in range(len(lst)-step):
			if lst[i+step]<lst[i]:
				lst[i], lst[i+step]=lst[i+step], lst[i]
				swap=True
				count+=1
	return lst
def mergeSort(list):
	if len(list)>1:
		mid=len(list)//2
		l=list[:mid]
		r=list[mid:]
		mergeSort(l)
		mergeSort(r)
		i=j=k=0
		while i<len(l) and j<len(r):
			if l[i]<r[j]:
				list[k]=l[i]
				i+=1
			else:
				list[k]=r[j]
				j+=1
			k+=1
		while i<len(l):
			list[k]=l[i]
			i+=1
			k+=1
		while j<len(r):
			list[k]=r[j]
			j+=1
			k+=1
def shellSort(lst,l,r, count=0):
	incs = [ 1391376, 463792, 198768,
	86961, 33936, 13776, 4592, 1968,
	861, 336,  112, 48, 21, 7, 3, 1 ] 
	
	for i in range(len(incs)):
		h=incs[i]
		#petla for wykonuje sie TYLKO gdy a<b dla range(a,b)
		for j in range(l+h,r+1):
			v=lst[j]
			k=j
			while k>=h and lst[k-h]>v:
				lst[k]=lst[k-h]
				k-=h
			lst[k]=v
			count+=1
	return lst
def quickSort(lst,l,r):
	if l<r:
		q = part(lst,l,r)
		print("Stan listy po partycji: ", lst)
		print("Pivot: ", lst[q])
		quickSort(lst,l,q-1)
		quickSort(lst,q,r)
def part(lst,l,r):
	if len(lst)<3: q=lst[0]
	else: q=lst[r]
	j=l-1
	for i in range(l,r):
		if lst[i]<=q:
			j+=1
			lst[j],lst[i]=lst[i],lst[j]
	lst[j+1],lst[r]=lst[r],lst[j+1]
	return j+1
	
def countingSort(lst,k=20000):
	c=[]
	for i in range(k):
		c.append(0)
	for i in range(len(lst)):
		c[lst[i]]=c[lst[i]]+1
	for i in range(1,k):
		c[i]=c[i]+c[i-1]
	b=[]
	for i in range(len(lst)+4):
		b.append(None)
	for i in range(len(lst2)-1,-1,-1):
		b[c[lst[i]]]=lst[i]
		c[lst[i]]=c[lst[i]]-1
	return b
	
def heapSort(lst):
	for i in range(len(lst)-1,0,-1):
		m=lst[0]
		lst[0]=lst[i]
		lst[i]=m
		if i>2: heapify(lst,len(lst),i-1)
	return lst
def heapSort2(lst,t):
	if len(lst)==1:
		t.append(lst[0])
		return
	t.append(lst[0])
	del lst[0]
	for k in range(len(lst)-1,-1,-1):
		heapify(lst, len(lst),k)
	heapSort2(lst,t)
def heapSort2Iter(lst,t):
	while len(lst)!=1:
		t.append(lst[0])
		del lst[0]
		for k in range(len(lst)-1,-1,-1):
			heapify(lst, len(lst),k)
	return 
def heapify(lst, n,i):
	largest=i
	l=2*largest+1
	r=2*largest+2
	if l<n and lst[i]<lst[l]:
		largest=l
	if r<n and lst[largest]<lst[r]:
		largest=r
	if largest!= i:
		lst[i], lst[largest] = lst[largest], lst[i]
		heapify(lst,n,largest)


	#return lst
tw=[]
w=[]
for i in range(100000):
	w.append(random.randint(1,8000))
for i in range(0,500):
	tw.append(w[random.randint(0,len(w)-1)])

#print(linearSearch(t,32))
print(tw)
#st=insertionSort(t)
#print(st)
#print("Metoda O(n): ",binSearch(st, 0,len(st),3))
#print("Metoda O(lgn): ", betterBinSearch(st,0,len(st)-1,3))
wynik=[]
#mergeSort(t)
#st=selectionSort(t)
#st2=bubbleSort(t)
#st3=shellSort(t, 0 , len(t)-1)
#quickSort(t, 0, len(t)-1)
#print("Quicksort: ", t)
#heapify(t)
#print(heapSort(t))
#st3=radixSort(t, len(str(t[0]))-1)
#print(st3)
#print("Bubble: ",st2)
testDH=[7, 6,5,6,6,4,6,6,3,4,3,6,5]
for i in range(len(testDH)-1,0,-1):
	heapify(testDH, len(testDH),i)
for i in range(len(tw)-1,-1,-1):
	heapify(tw,len(tw),i)
print(tw)
t=[]
#heapSort2Iter(tw, t)
#print(list(reversed(t)))
#quickSort(tw,0,len(tw)-1)
print(combSort(tw))
