#We have list of n coins and sum x: return length of smallest sum
# of coins that gives x
import math

def iter_solve(x,coins,first):
	value=[]
	value.append(0)
	for i in range(1,x):
		value.append(math.inf)
		for c in coins:
			if i-c>=0 and value[i-c]+1<value[i]:
				value[i]=value[i-c]+1
				first.append(c)
	while x>0:
		print(first[x])
		x=x-first[x]
def solve(x, coins,ready,value):
	if x<0: return math.inf
	if x==0: return 0
	if x in ready: return value[x]
	best=math.inf
	for c in coins:
		best=min(best,solve(x-c,coins,ready, value)+1)
	value[x]=best
	ready[x]=True
	return best
coins=[1,2,5,10,20,50,100,200]
x=100 
ready={}
value={}
first=[]
#print(solve(x,coins, ready, value))
print(iter_solve(x,coins,first))