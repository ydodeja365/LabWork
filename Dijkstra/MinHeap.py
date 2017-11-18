class MinHeap:
	def __init__(self):
		self.elements=[None]*10000
		self.last=-1
	def left(self,i):
		return 2*i+1
	def right(self,i):
		return 2*i+2
	def parent(self,i):
		return (i-1)//2
	def insert(self,v):
		self.last=self.last+1
		self.elements[self.last]=v
		p=self.parent(self.last)
		t=self.last
		while p>=0:
			if self.elements[p]>v:
				self.swap(t,p)
				t=p
				p=self.parent(p)
				#print("p:",p,self.elements[:self.last+1])
			else:
				break

	def swap(self,i1,i2):
		self.elements[i1],self.elements[i2]=self.elements[i2],self.elements[i1]
	def heapify(self,i):
		if self.left(i)>self.last:
			return
		if self.right(i)>self.last:
			m=self.elements[self.left(i)]
		else:
			m=min(self.elements[self.left(i)],self.elements[self.right(i)])
		if m<self.elements[i]:
			if self.elements[self.left(i)]==m:
				self.swap(self.left(i),i)
				self.heapify(self.left(i))
			else:
				self.swap(self.right(i),i)
				self.heapify(self.right(i))
	def min(self):
		if self.last!=-1:
			return self.elements[0]
		else:
			return "Empty!"
	def extractMin(self):
		if self.last!=-1:
			self.swap(0,self.last)
			self.last-=1
			self.heapify(0)
			return self.elements[self.last+1]
		else:
			return "Empty!"
	def __str__(self):
		return str(self.elements[:self.last+1])
	def isEmpty(self):
		return self.last==-1

def main():
	H=MinHeap()
	H.insert(1)
	print(H)
	H.insert(-2)
	print(H)
	H.insert(0)
	print(H)
	H.insert(-3)
	print(H)
	print(H.extractMin())
	print(H)
if __name__=='__main__':
	main()



