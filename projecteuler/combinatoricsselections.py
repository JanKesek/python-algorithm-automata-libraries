import math

limit = 1000000
count=0
fact = lambda a : math.factorial(a)
for i in range(21,101):
	for j in range(1,i):
		comb = fact(i)//(fact(j)*fact(i-j))
		if comb>=limit: count+=1
print(count)