def dfs(G,s,time,tree=[],back=[],forward=[],cross=[]):
	print(s,end=' ')
	G.V[s].visited="grey"
	for v in G.V[s].adj:
		if G.V[v].visited=="white":
			time+=1
			G.V[v].start=time
			tree.append([s,v])
			dfs(G,v,time,tree,back,forward,cross)
		elif G.V[v].visited=="grey":
			back.append([s,v])
		else:
			if G.V[v].end>G.V[s].start:
				forward.append([v,s])
			else:
				cross.append([v,s])
	G.V[s].visited="black"
	time+=1
	G.V[s].end=time

class GraphNode:
	def __init__(self):
		self.adj=[]
		self.start=1
		self.end=1
		self.visited="white"

class Graph:
	def __init__(self,n):
		self.V=[GraphNode() for i in range(n)]

def main():
	n=int(input("Enter number of vertices:"))
	G=Graph(n)
	m=int(input("Enter number of edges:"))
	for i in range(m):
		a,b=input().split()
		a,b=int(a),int(b)
		G.V[a].adj.append(b)
		G.V[b].adj.append(a)
	x=int(input("Enter source vertex:"))
	print("Order of vertices in DFS:")
	t=[]
	b=[]
	f=[]
	c=[]
	dfs(G,x,1,t,b,f,c)
	print(t,"\n",b,"\n",f,"\n",c)

if __name__=='__main__':
	main()