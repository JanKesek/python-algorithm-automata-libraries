stack=[]
g1=g2=g3={}
n=4
#global c
def gen(n):
	#a<<b is the same as 1*(2**b)
	for i in range(1<<n):
		list=[]
		for j in range(n):
			#bitwise and: 
			#output: 1 if kth bit of a and kth bit of b is 1
			if i&(1<<j): list.append(j+1)
		stack.append(list)
	return stack
def generateSubsets(k,n):
	if k==n+1: return stack
	else:
		generateSubsets(k+1,n)
		stack.append(k)
		generateSubsets(k+1,n)
		stack.pop()

def search(y, c=0):
	if y==n: 
		c+=1
		return
	for i in range(n):
		if g1[i] or g2[i+y] or g3[i-y+n-1]: continue
		g1[i]=g2[i+y]=g3[i-y+n-1]=1
		search(y+1)
		g1[i]=g2[i+y]=g3[i-y+n-1]=0
	return c
def queenSearch(queens, dimmension, iter, r1,r2,r3):
	if queens==dimmension:
		iter+=1
	for i in range(dimmension):
		if (i in r1 or i+queens in r2 or i-queens+dimmension-1 in r3): continue
		r1[i]=r2[i+queens]=r3[i-queens+dimmension-1]=1
		queenSearch(queens+1,dimmension,iter,r1,r2,r3)
		r1[i]=r2[i+queens]=r3[i-queens+dimmension-1]=0
	return iter
#n=15 means set={1,2,3,...,15}
#print(generateSubsets(1,15))
#print(gen(5))

basic=[0,1,2,3]
r1=[]
r2=[]
r3=[]
j=0
for i in range(4):
	r1.append(basic)
	temp=[basic[0]+j,basic[1]+j,basic[2]+j,basic[3]+j]
	r2.append(temp)
	r3.append(temp)
	j+=1
r3.reverse()
#print(r1, r2, r3)
t1=t2=t3={}
c=search(4)
print(c)
#print(queenSearch(16,1,0,t1,t2,t3))