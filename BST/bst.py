class Node:
	def __init__(self,v=None):
		self.val=v
		self.left=None
		self.right=None
		self.parent=None
class BST:
	def __init__(self):
		self.root=None
	def insert(self,v):
		if self.root is None:
			self.root=Node(v)
			return
		t=self.root
		n=Node(v)
		while t is not None:
			y=t
			if t.val<v:
				t=t.right
			else:
				t=t.left
		if y.val<v:
			y.right=n
		else:
			y.left=n
		n.parent=y
	def search(self,v):
		t=self.root
		while t is not None:
			y=t
			if t.val<v:
				t=t.right
			elif t.val>v:
				t=t.left
			else:
				return True
		return False
	def searchNode(self,v):
		t=self.root
		while t is not None:
			y=t
			if t.val<v:
				t=t.right
			elif t.val>v:
				t=t.left
			else:
				break
		return t
	def delete(self,v):
		t=self.searchNode(v)
		if t is None:
			print("Error! Not Found..")
			return
		if t.isLeaf():
			if t.parent is None:
				self.root=None
				return
			if t.parent.left==t:
				t.parent.left=None
			else:
				t.parent.right=None
			return
		elif t.hasOne():
			if t.parent is None:
				if t.right is None:
					self.root=t.left
				else:
					self.root=t.right
				return
			if t.right is None:
				t.left.parent=t.parent
				if t.parent.left==t:
					t.parent.left=t.left
				else:
					t.parent.right=t.left
			else:
				
