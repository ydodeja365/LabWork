#****************************AVL TREE NODE************************#
class Node:
	def __init__(self,v=None):
		self.left=None
		self.right=None
		self.val=v
		self.height=1
		self.parent=None

	def isBalanced(self):
		m=self.left.height if self.left is not None else 0
		n=self.right.height if self.right is not None else 0
		return abs(m-n)<=1

	def preorder(self):
		if self==None:
			return print("",end="")
		print(self.val,end=" ")
		if self.left!=None:
			self.left.preorder()
		if self.right!=None:
			self.right.preorder()

	def hasOne(self):
		m=self.right is None and self.left is not None
		n=self.left is None and self.right is not None
		return m or n

	def isLeaf(self):
		return self.left is None and self.right is None

#*****************************AVL TREE*****************************#
def height(node):
	if node==None:
		return 0
	if node.isLeaf():
		return 1
	else:
		return max(height(node.left),height(node.right))+1


class AVL:
	def __init__(self):
		self.root=None

	def insert(self,v):
		if self.root is None:
			self.root=Node(v)
			return
		n=Node(v)
		t=self.root
		parent=None
		while t is not None:
			parent=t
			if t.val<v:
				t=t.right
			else:
				t=t.left
		if parent.val<v:
			parent.right=n
		else:
			parent.left=n
		n.parent=parent
		while parent is not None:
			parent.height=height(parent)
			if not parent.isBalanced():
				z=parent
				if z.val<v:
					y=z.right
				else:
					y=z.left
				if y.val<v:
					x=y.right
				else:
					x=y.left
				if z.right==y:
					if y.right==x:
						return self.leftR(z)
					else:
						rightR(y)
						return self.leftR(z)
				else:
					if y.left==x:
						return self.rightR(z)
					else:
						leftR(y)
						return self.rightR(z)
			parent=parent.parent

	def search(self,v):
		t=self.root
		while t is not None:
			if t.val<v:
				t=t.right
			elif t.val>v:
				t=t.left
			else:
				return t
		return None
	
	def delete(self,v):
		t=self.search(v)
		if t is None:
			print("Not found!")
			return
		self.deleteNode(t)

	def deleteNode(self,t):
		v=t.val
		print("Deleting",v)
		if t.hasOne():
			if t.left is not None:
				print("Left")
				t.val=t.left.val
				self.deleteNode(t.left)
			else:
				t.val=t.right.val
				self.deleteNode(t.right)
		elif t.isLeaf():
			print("Leaf")
			if t.parent is None:
				self.root=None
				return
			parent=t.parent
			if parent.left==t:
				parent.left=None
			else:
				parent.right=None
			while parent is not None:
				print("Parent:",parent.val)
				parent.height=height(parent)
				if not parent.isBalanced():
					print("Unbalnaced")
					z=parent
					if z.val<v:
						#print("Here z=",z.val,",z.height=",z.height,z.left.height,z.right)
						y=z.left
					else:
						y=z.right
					print(z.val,y.val,t.val)
					if y.left.height<y.right.height:
						x=y.right
					else:
						x=y.left
					if z.right==y:
						if y.right==x:
							self.leftR(z)
						else:
							self.rightR(y)
							self.leftR(z)
					else:
						if y.left==x:
							print("RR")
							self.rightR(z)
						else:
							self.leftR(y)
							self.rightR(z)
				parent=parent.parent
		else:
			s=self.successorNode(t)
			self.deleteNode(s)
		#print("Final:",t.val)

	def successorNode(self,n):
		t=n.right
		while t is not None:
			y=t
			t=t.left
		return y

	def preorder(self):
		if self.root is not None:
			self.root.preorder()
		print()

	def leftR(self,node):
		n1=node.right
		node.right=n1.left
		n1.left=node
		n1.parent=node.parent
		node.parent=n1
		if n1.parent is not None:
			if n1.parent.left==node:
				n1.parent.left=n1
			else:
				n1.parent.right=n1
		else:
			self.root=n1
		node.height=height(node)
		n1.height=height(n1)

	def rightR(self,node):
		n=node.left
		node.left=n.right
		n.parent=node.parent
		n.right=node
		if node.parent!=None:
			if node.parent.left==node:
				node.parent.left=n
			else:
				node.parent.right=n
		else:
			self.root=n
		node.parent=n
		node.height=height(node)
		n.height=height(n)

def main():
	T=AVL()
	l=[7,3,1,0,2]
	for i in l:
		T.insert(i)
	T.preorder()
	for i in l:
		print(i,":")
		T.delete(i)
		T.preorder()

if __name__=='__main__':
	main()