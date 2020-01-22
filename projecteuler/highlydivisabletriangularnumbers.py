import math

def triangularNumber(n):
	return sum(range(1,n+1))
def factors(n):
	lst=[]
	for i in range(1,n+1):
		if n%i==0: lst.append(i)
	return lst
def findNumber():
	for i in range(1,5000):
		t=factors(triangularNumber(i))
		print(len(t))
		if len(t)>500:
			return i
		#print(t)
		#exit(1)
	#print(triangularNumber(i))

#print(factors(28))
print("ZNALEZIONO", findNumber())