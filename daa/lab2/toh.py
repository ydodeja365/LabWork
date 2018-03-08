def toh(n,s,i,t):
	if(n>=1):
		toh(n-1,s,t,i)
		print("Move disc",n,"from",s,"to",t)
		toh(n-1,i,s,t)
def main():
	n=int(input("Enter number of discs:"))
	toh(n,'S','I','T')
if __name__=='__main__':
	main()
