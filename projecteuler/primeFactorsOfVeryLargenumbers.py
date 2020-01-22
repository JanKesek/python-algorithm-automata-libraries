def divideIntoSmallerRange(number):
	i=50
	p=50
	while i<12000:
		if number%i==0:
			p=i
		i+=1
	#print(p)
	ceil=number/p
	t=[]
	while ceil<=number:
		t.append(ceil)
		ceil+=ceil
	return t
def primeFactor(number,lst,p=2,pfArr=[], iter=0):
	print("How many iterations: ", iter)
	if number>=pow(p,2):
		for n in lst:
			if p<n:
				for j in range(p,int(n)):
					if number%j==0:
						pfArr.append(j)
						iter+=1
						return primeFactor(number/j,lst,j,pfArr, iter)
	else:
		pfArr.append(number)
		return pfArr
lstOfRanges=divideIntoSmallerRange(600851475143)
print("Factors found: ", primeFactor(600851475143, lstOfRanges))
print("Factors found: ", primeFactor(600851475143, lstOfRanges))
