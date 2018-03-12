class interval:
	def __init__(self,s,e):
		self.start=s
		self.end=e

def schedule(l,n):
	l.sort(key=lambda x:x.end)
	available=[True for i in range(n)]
	scheduleCount=n
	rnum=0
	while scheduleCount>0:
		rnum+=1
		s=[]
		t=0
		for i in range(n):
			 if l[i].start>t and available[i]:
			 	t=l[i].end
			 	s.append(l[i])
			 	available[i]=False
			 	scheduleCount-=1
		print("\nResource",rnum,"jobs:")
		print("--------------------")
		for i in s:
			print("["+str(i.start)+","+str(i.end)+"]")
def main():
	n=int(input("Enter number of intervals:"))
	l=[]
	for i in range(n):
		s,e=input().split()
		s,e=int(s),int(e)
		l.append(interval(s,e))
	schedule(l,n)
if __name__=='__main__':
	main()