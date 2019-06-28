weight=0.1
weight2=-8.9
weights3 = [0.1, 0.2, 0] 
number_of_toes = [8.5, 9.5, 10, 9]
currentGamesWon = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]     
def n(input, weight):
	prediction=input*weight
	return prediction
def wSum(a,b):
	r=0
	for i in range(0,len(a)):
		r+=a[i]*b[i]
	return r
def shouldIWearCoat(temperature, weight2):
	return temperature*weight2
def willTheyWin(inpts, weight3):
	pred=0
	for i in range(0,3):
		pred=pred+(inpts[i]*weight3[i])
	return pred
def autom(string):
	i=0
	a=False
	while i<len(string):
		if string[i]=='a':
			a=True
			i+=1
		elif string[i]=='b':
			a=True
			i+=1
			if i<len(string):
				if string[i]=='c':
					a=True
					i+=1
		else: i+=1
	return a
	
print(n(number_of_toes[0],weight))
print(shouldIWearCoat(-10, weight2))
print(willTheyWin([number_of_toes[0],currentGamesWon[0],nfans[0]], weights3))
print(autom("gjccccchgh"))
a=[.5,0,1,1]
b=[0,.5,.5,.5]
print(wSum(a,b))
