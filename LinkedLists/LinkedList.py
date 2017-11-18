#*************************NODE OF SINGLY LINKED LIST*******************#

class Node:
	def __init__(self,v=None,n=None):
		self.val=v
		self.next=n

#*************************SINGLY LINKED LIST*************************#

class LinkedList:

	def __init__(self):
		self.head=Node()

	# O(N)
	def insert(self,v):
		t=self.head
		while t.next is not None:
			t=t.next
		t.next=Node(v)
	
	# O(1)
	def insertAfterNode(self,v,n):
		if n is None:
			print("Error")
			return
		z=Node(v)
		z.next=n.next
		n.next=z
	
	# O(N)
	def delete(self,v):
		t=self.head
		if t.next is None:
			print("Empty List!")
			return
		flag=0
		while t.next is not None:
			if t.next.val==v:
				t.next=t.next.next
				flag=1
				break
			t=t.next
		if flag==0:
			print("Not found!")
			return

	# O(1)
	def deleteAfterNode(self,n):
		if n is None:
			print("Error")
			return
		n.next=n.next.next

	# O(N)
	def search(self,v):
		t=self.head.next
		while t is not None:
			if t.val==v:
				print("Found!")
				return
			t=t.next
		print("Not Found!")

	# O(i)
	def insertAtIndex(self,v,i):
		if i<=0:
			print("Error")
			return
		t=self.head
		j=1
		while j<i:
			j+=1
			if t.next is None:
				print("Index too high!")
				return
			t=t.next
		self.insertAfterNode(v,t)

	def deleteAtIndex(self,i):
		if i<=0:
			print("Error")
			return
		t=self.head
		j=1
		while j<i:
			j+=1
			if t.next is None:
				print("Index too high!")
				return
			t=t.next
		self.deleteAfterNode(t)

	def __str__(self):
		t=self.head.next
		x=str()
		while t is not None:
			x+=str(t.val)+" "
			t=t.next
		return x

	def reverse(self):
		current=self.head.next
		prev=None
		while current is not None:
			next=current.next
			current.next=prev
			prev=current
			current=next
		self.head.next=prev

#******************************TESTER PROGRAM*********************************#

def main():
	L=LinkedList()
	L.insert(1)
	L.insertAtIndex(2,1)
	L.insertAtIndex(3,1)
	L.insertAtIndex(4,1)
	print(L)
	L.search(4)
	L.deleteAtIndex(1)
	print(L)
	L.search(4)
	print(L)
	L.reverse()
	print(L)

if __name__=='__main__':
	main()