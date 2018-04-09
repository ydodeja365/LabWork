def editDistance(s1,s2):
	n1=len(s1)
	n2=len(s2)
	t=[[0 for i in range(n2)] for j in range(n1)]
	if s1[0]!=s2[0]:
		t[0][0]=1
	for i in range(n1):
		for j in range(n2):
			a=0
			updated=False
			if (j-1)>=0:
				a=t[i][j-1]+1
				if (i-1)>=0:
					b=1
					if s1[i]==s2[i]:
						b=0
					a=min(a,t[i-1][j-1]+b)
				updated=True
			if (i-1)>=0:
				if not updated:
					a=t[i-1][j]+1
				else:
					a=min(a,t[i-1][j]+1)
			t[i][j]=a
	print("Table is:\n",t)
	return t[n1-1][n2-1]


def main():
	s1=str(input("Enter first string:"))
	s2=str(input("Enter second string:"))
	print(editDistance(s1,s2))

if __name__ == '__main__':
	main()