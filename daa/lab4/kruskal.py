class Graph:
	def __init__(self,n):
		self.V=DSet(n)
		self.edges=[]

class SetNode:
	def __init__(self,n):
		self.parent=self
		self.value=n
		self.rank=0

class DSet:
	def __init__(self,n):
		self.N=n
		self.l=[self.makeSet(i) for i in range(n)]
	
	def makeSet(self,i):
		return SetNode(i)

	def findSet(self,i):
		if i.parent is not i:
			i.parent=self.findSet(i.parent)
		return i.parent

	def union(self,x,y):
		s1=self.findSet(x)
		s2=self.findSet(y)
		if s1 is s2:
			return
		if s1.rank>s2.rank:
			s2.parent=s1
		elif s2.rank>s1.rank:
			s1.parent=s2
		else:
			s2.parent=s1
			s1.rank+=1

	def printsets(self):
		ans=[[] for i in range(self.N)]
		for i in self.l:
			x=self.findSet(i)
			ans[x.value].append(i.value)
		print("Disjoint Set List:")
		for i in ans:
			if i!=[]:
				print(i)

def Kruskal(G):
	G.edges.sort(key=lambda x:x[2])
	for i in G.edges:
		x=G.V.findSet(G.V.l[i[0]])
		y=G.V.findSet(G.V.l[i[1]])
		if x==y:
			continue
		print(i[0],'-',i[1])
		G.V.union(x,y)
	G.V.printsets()

def main():
	n=int(input("Enter number of vertices:"))
	G=Graph(n)
	a=0
	print("Enter edges(u,v,cost(u,v)):")
	while a!=-1:
		l=input().split()
		if len(l)<3:
			break
		a,b,c=int(l[0]),int(l[1]),int(l[2])
		G.edges.append((a,b,c))
	print("\n\t\tOUTPUT\n\t\t------")
	print("Edges in MST are:")
	Kruskal(G)

if __name__=='__main__':
	main()