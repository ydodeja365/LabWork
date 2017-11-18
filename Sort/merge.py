def mergesort(l,start,end):
	if start<end:
		mid=(start+end)//2
		left=[]
		right=[]
		left=l[:mid+1]
		right=l[mid+1:]
		mergesort(left,0,mid-start)
		mergesort(right,0,end-mid-1)
		merge(left,right,l)
	return l

def merge(l,r,a):
	i=0
	j=0
	k=0
	while i<len(l) or j<len(r):
		if i==len(l):
			a[k]=r[j]
			j+=1
			k+=1
		elif j==len(r):
			a[k]=l[i]
			k+=1
			i+=1
		elif l[i]<r[j]:
			a[k]=l[i]
			i+=1
			k+=1
		else:
			a[k]=r[j]
			j+=1
			k+=1
	return a

def main():
	l=[1,2,3,4]
	l=mergesort(l,0,5)
	print(l)
if __name__=='__main__':
	main()