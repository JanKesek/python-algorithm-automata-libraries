

import math

def clearBoard(n):
	b=[]
	for i in range(n):
		t=[]
		for j in range(n):
			t.append(0)
		b.append(t)
	return b
def tryBacktrack(i,x,y,q,board,n):
	k=-1
	q1=False

	for t in board:
		if n**2 in t:
			print(board)
			return
	if i>(n**2):
		print("FUCK THAT")
		#print(board)
		return
	#print(board)
	while q1 is False and k<7:
		k+=1
		q1=False
		dx=[2,1,-1,-2,-2,-1,1,2]
		dy=[1,2,2,1,-1,-2,-2,-1]
		u=x+dx[k]
		v=y+dy[k]
		if u>=0 and u<n and v>=0 and v<n and board[u][v]==0:
			if board[u][v]==0:
				board[u][v]=i
				if i<=(n**2):
					tryBacktrack(i+1, u,v,q1,board,n)
					if not q1: board[u][v]=0
				else: 
					q1=True
	q=q1
	#return board
def knightTour(i,j,n,board,done=True):
	board[i][j]=1
	#return board
	tryBacktrack(2,i,j,done,board,n)
board=clearBoard(6)
board2=knightTour(0,0,6,board)
print(board2)