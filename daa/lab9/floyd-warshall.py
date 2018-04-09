import sys
class matrix:
	def __init__(self,n,def_val=sys.maxsize):
		self.m=[[def_val for i in range(n)] for _ in range(n)]
	def __str__(self):
		n=len(self.m)
		x=""
		for i in range(n):
			for j in range(n):
				if self.m[i][j]>sys.maxsize-10000000:
					x+="inf "
				else:
					x+=str(self.m[i][j])+" "
			x+="\n"
		return x
# list representation memory O(n^3)
def floydWarshall(n,E):
	D=[matrix(n) for i in range(n+1)]
	D[0]=E
	for k in range(n):
		for i in range(n):
			for j in range(n):
				D[k+1].m[i][j]=min(D[k].m[i][j],D[k].m[i][k]+D[k].m[k][j])
	return D[n]
# 2 matrices memory O(n^2)
def floydWarshall1(n,E):
	prev=E
	new=matrix(n)
	for k in range(n):
		for i in range(n):
			for j in range(n):
				new.m[i][j]=min(prev.m[i][j],prev.m[i][k]+prev.m[k][j])
		prev=new
	return new
# path printing
def floydWarshall2(n,E,a,b):
	prev=E
	new=matrix(n)
	PI=[matrix(n) for i in range(n+1)]
	for i in range(n):
		PI[0].m[i][i]=i
	for k in range(n):
		for i in range(n):
			for j in range(n):
				if prev.m[i][j]<=prev.m[i][k]+prev.m[k][j]:
					new.m[i][j]=prev.m[i][j]
					PI[k].m[i][j]=PI[k-1].m[i][j]
				else:
					new.m[i][j]=prev.m[i][k]+prev.m[k][j]
					PI[k].m[i][j]=PI[k-1].m[k][j]
		prev=new
	k=n
	a=PI[n].m[i][j]
	x=""
	while a!=i:
		k-=1
		x+="<-"+str(a)
		a=PI[k].m[i][a]
	return x

def main():
	f=open("input.txt")
	n=int(f.readline())
	E=matrix(n)
	while(True):
		l=f.readline().split()
		if len(l)!=3:
			break
		E.m[int(l[0])-1][int(l[1])-1]=int(l[2])
	for i in range(n):
		E.m[i][i]=0
	result=floydWarshall(n,E)
	print(result)
	print("Enter any 2 vertices:")
	a,b=input().split()
	a,b=int(a),int(b)
	print(floydWarshall2(n,E,a-1,b-1))
	#print("E=",E.m)

if __name__ == '__main__':
	main()