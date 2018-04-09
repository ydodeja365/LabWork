n=int(input("Enter n:"))
print("Enter array:")
a=[int(i) for i in input().split()]
memo=[None for i in range(n)]
memo[0]=0
for i in range(2,n):
	max=0
	for k in range(i):
		if a[k]<a[i] and memo[k]+1>max:
			max=memo[k]+1
	memo[i]=max
print("Length of longest increasing subsequence:"+str(max(memo)))