import random, queue

def quicksort(s, low, high):
	if low<high:
		p=partition(s,low,high)
		quicksort(s,low,p-1)
		quicksort(s,p+1,high)
	return s
def swap(lst, indx1, indx2):	
	temp=lst[indx1]
	lst[indx1]=lst[indx2]
	lst[indx2]=temp
	return lst
def partition(s,low,high):
	p=high
	fh=low
	x=s[fh]
	for i in range(low+1,high+1):
		if s[i]<=x:
			fh=fh+1
			s= swap(s,i,fh)
	s = swap(s,low,fh)
	return fh
	

def mergesort(lst, low, high):
	if low<high:
		middle=(low+high)//2
		mergesort(lst,low, middle)
		mergesort(lst,middle+1,high)
		lst = merge(lst, low, middle, high)
	return lst	
def merge(lst, low, middle, high):
	fBuffer = queue.Queue(len(lst)+1)
	sBuffer = queue.Queue(len(lst)+1)
	for i in range(low, middle):
		fBuffer.put(lst[i])
	for i in range(middle+1,high):
		sBuffer.put(lst[i])
	i=low
	while (fBuffer.empty() or sBuffer.empty())!=True:
		#w ifie moze fbuff.head()?
		if list(fBuffer.queue)[0] <= list(sBuffer.queue)[0]:
			i=i+1
			lst[i] = fBuffer.get()
		else:
			i=i+1
			lst[i]=sBuffer.get()
	while fBuffer.empty() is False: 
		i=i+1
		lst[i]=fBuffer.get()
	while sBuffer.empty() is False: 
		i=i+1
		lst[i]=sBuffer.get()
	return lst
	
def makeRandomSetOfValues(t, n):
	for i in range(1,n):
		t.append(random.randint(1,100000))
	return t

t=[]
t = makeRandomSetOfValues(t,400)
#print(t)
#sortedT = mergesort(t, 0, len(t)-1)
#print(sortedT)
#print(len(t), len(sortedT))
print(quicksort(t, 0, len(t)-1))