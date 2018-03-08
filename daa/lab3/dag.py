class Node:
	def __init__(self):
		self.adjacent=[]
		self.incoming=0
		self.active=True
		
class Graph:
	def __init__(self,n):
		self.V=[Node() for i in range(n)]
		self.sources=[]
	def findSourceInit(self):
		for i in range(len(self.V)):
			if self.V[i].incoming==0:
				self.sources.append(i)
	def countSems(self):
		sems=0
		self.findSourceInit()
		while self.sources!=[]:
			V1=[]
			for i in self.sources:
				self.V[i].active=False
				for j in self.V[i].adjacent:
					self.V[j].incoming-=1
					if self.V[j].incoming==0 and self.V[j].active:
						V1.append(j)
			#print(self.sources)
			self.sources=V1
			sems+=1
		return sems	

def main():
	n=int(input("Enter number of vertices:"))
	print("Enter edges:")
	a=0
	G=Graph(n)
	while a!=-1:
		l=input().split()
		if(len(l)==2):
			a,b=int(l[0]),int(l[1])
			G.V[a].adjacent.append(b)
			G.V[b].incoming+=1
		else:
			a=-1
	print("Number of sems required=" +str(G.countSems()))

if __name__=='__main__':
	main()
