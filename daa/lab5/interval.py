def schedule(l,n):
	l.sort(key=lambda x:x.end)
	t=0
	s=[]
	for i in l:
		 if i[0]>t:
		 	t=i[1]
		 	s.append(i)
	print("Processes scheduled:")
	print("--------------------")
	for i in s:
		print("["+str(i[0])+","+str(i[1])+"]")
def main():
	n=int(input("Enter number of intervals:"))
	l=[]
	for i in range(n):
		s,e=input().split()
		s,e=int(s),int(e)
		l.append((s,e))
	schedule(l,n)
if __name__=='__main__':
	main()