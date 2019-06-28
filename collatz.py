def collatz(n):
	i=0
	while n!=1:
		if n%2==0: 
			n=n/2
			i+=1	
		else:
			n=3*n+1
			i+=1
	return i
def collatzN(i, j):
	t=[]
	for k in range(i,j):
		t.append(collatz(k))
	return t
	
	
print(collatzN(32,3223100))