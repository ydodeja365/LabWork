from MinHeap import MinHeap
import math
class GraphNode:
	def __init__(self):
		self.adj=[]
		self.dist=math.inf
		self.color="white"
		self.pred=None
	def __lt__(self,other):
		return self.dist<other
	def __gt__(self,other):
		return self.dist>other
class Graph:
	def __init__(self,n):
		self.V=[GraphNode() for i in range(n)]
def update(H):
	for i in range(H.last//2,-1,-1):
		H.heapify(i)
def Dijkstra(G,s):
	G.V[s].dist=0
	H=MinHeap()
	for i in G.V:
		H.insert(i)
	while not H.isEmpty():
		u=H.extractMin()
		for v in u.adj:
			if G.V[v[0]]>u.dist+v[1]:
				G.V[v[0]].dist=u.dist+v[1]
				G.V[v[0]].pred=u
				update(H)
	j=0
	for i in G.V:
		print("Vertex",j,":",i.dist)
		j+=1

def main():
	n=int(input("Enter number of vertices:"))
	G=Graph(n)
	m=int(input("Enter number of edges:"))
	for i in range(m):
		a,b,c=input().split()
		a,b,c=int(a),int(b),int(c)
		G.V[a].adj.append((b,c))
		G.V[b].adj.append((a,c))
	x=int(input("Enter source vertex:"))
	print("\n------------Dijkstra's Algorithm------------\n")
	Dijkstra(G,x)
	print("\n--------------------------------------------")

if __name__=='__main__':
	main()


