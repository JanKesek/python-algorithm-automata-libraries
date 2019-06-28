import math

def partition(s, n,k):
	m,d,p = []
	p.append(0)
	for i in range(1,n): p.append(p[i-1]+s[i])
	for i in range(1,n): 
		t=[]
		t.append(p[i])
		m.append(t)
	for i in range(1,k):
		m[1].append(s[1])
	for i in range(2,n):
		for j in range(2,k):
			m[i][j]=math.inf
			for k in range(1,i-1):
				cost=max(m[k][j-1],p[i]-[x])
				if m[i][j]>cost:
					m[i][j]=cost
					d[i][j]=k