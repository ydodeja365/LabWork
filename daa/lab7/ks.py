def ks(c_max,v,w):
	n=len(v)
	t=[[None for i in range(n+1)] for j in range(c_max)]
	for i in range(c_max):
		t[i][n]=0
	for i in range(n-1,-1,-1):
		for c in range(c_max):
			if w[i]>c:
				t[c][i]=t[c][i+1]
			else:
				t[c][i]=max(t[c][i+1],t[c-w[i]][i+1]+v[i])
	return t[c_max-1][0]

def main():
	c=int(input("Enter capacity:"))
	print("Enter values of items:")
	v=[int(i) for i in input().split()]
	print("Enter weights of items:")
	w=[int(i) for i in input().split()]
	print("Value of items picked= "+str(ks(c,v,w)))

if __name__ == '__main__':
	main()