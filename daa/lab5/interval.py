class interval:
	def __init__(self,s,e):
		self.start=s
		self.end=e

def schedule(l,n):
	l.sort(key=lambda x:x.end)
	t=0
	s=[]
	for i in l:
		 if i.start>t:
		 	t=i.end
		 	s.append(i)
	print("Processes scheduled:")
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