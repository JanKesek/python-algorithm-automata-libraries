f = {}
def fib(n):
	if f[n] is None:
		f[n]=fib(n-1)+fib(n-2)
	return f[n]
def worstFib(n):
	if n==1: return 1
	if n==2: return 1
	else: return worstFib(n-1)+worstFib(n-2)
def fibDriver(n):
	f[1]=0
	f[2]=1
	for i in range(3, n+1): 
		f[i]=None
	return fib(n)
def iteratFib(n):
	t=[]
	t.append(0)
	t.append(1)
	for i in range(2,n):
		t.append(t[i-1]+t[i-2])
	return t[n-1]
	
#for i in range(4,200):
#	print(fibDriver(i))
for i in range(1,50):
	print(worstFib(i))
#for i in range(1,200):
#	print(iteratFib(i))