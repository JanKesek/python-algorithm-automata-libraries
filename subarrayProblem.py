#We have list of n coins and sum x: return length of smallest sum
# of coins that gives x
import math

def twoSum(x, array):
	i=0
	j=len(array)-1
	p=0
	helper=1
	while p<=x:
		print("i: ", i, "j: ", j)
		if array[i]+array[j]<=x:
			p=array[i]+array[j]
			i+=1
			j-=1
		else:
			for h in range(1, len(array)):
				if array[i]+array[j-h]<=x:
					j-=1
					h=len(array)
				elif array[i+h]+array[j]<=x:
					i+=1
					h=len(array)
		if i==len(array)-1 and j==0: return False
	if p==x: return i,j
	else: return False
def subarr(x,array):
	i=0
	j=0
	p=0
	while p<=x:
		if p+array[j]<=x: 
			p+=array[j]
			j=j+1
	if p==x: return p
	while p<=x:
		if p+array[i+1]<=x: i=i+1
		if p+array[j+1]<=x: j=j+1
		p=0
		for k in range(i,j):
			p+=array[k]	
	if p==x: return p
	else: return False
array=[1,4,5,6,7,9,9,10]
x=12
#print(subarr(x,array))
print(twoSum(x,array))