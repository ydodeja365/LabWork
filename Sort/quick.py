def quicksort(l,s,e):
	if s<e:
		ind=partition(l,s,e)
		quicksort(l,s,ind-1)
		quicksort(l,ind+1,e)
	return
	if s==e:
		return e

def partition(l,s,e):
	pivot=l[e]
	index=s-1
	for i in range(s,e):
		if l[i]<=pivot:
			l[i],l[index+1]=l[index+1],l[i]
			index+=1
	l[e],l[index+1]=l[index+1],l[e]
	return index+1

def main():
	l=[int(i) for i in input().split()]
	quicksort(l,0,len(l)-1)
	print(l)

if __name__=='__main__':
	main()