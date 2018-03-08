def main():
	a=[int(i) for i in input("Enter sequence:").split()]
	b=[0]*len(a)
	# print(b)
	for i in range(len(a)):
		for j in range(i,len(a)):
			if a[i]>a[j]:
				b[i]+=1
	print("Inversions=",sum(b))
if __name__=='__main__':
	main()