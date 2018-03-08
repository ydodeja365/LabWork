class AVLTreeNode:				#class AVLTreeNode{
	def __init__(self,val=None):#int height;int key;AVLTreeNode left,right,parent;#AVLTreeNode(){
		self.key=val			#height=0;key=NULL;left=NULL;right=NULL;parent=NULL;
		self.left=None			#}
		self.right=None
		self.parent=None
	def prefix(root):
        if root is None:
            return
        print(root.value, end=' ')
        TreeNode.preorder(root.left)
        TreeNode.preorder(root.right)
def height(A):
	if A==None:
		return 0
	else:
		return max(height(A.left),height(A.right))+1
class AVLTree:
	def __init__(self):
		self.root=None
	def search(self,val):
		t=self.root
		while t!=None:
			if t.key<val:
				t=t.right
			elif t.key>val:
				t=t.left
			else:
				return t
		return t
	def insert(self,val):
		n=AVLTreeNode(val)
		t=self.root
		if t==None:
			self.root=n
			return
		else:
			while t.left!=None and t.right!=None:
				if t.key<val:
					t=t.right
				else:
					t=t.left
			if t.key<val:
				t.right=n
			else:
				t.left=n
			n.parent=t
			#print("Done",t.key,n.parent.key)
			while t!=None:
				print("Hi")
				while abs(height(t))<=1:
					t=t.parent
				if t==None:
					return
				else:
					z=t
					if val<z.key:
						y=z.left
					else:
						y=z.right
					if val<y.key:
						x=y.left
					else:
						x=y.right
					if y==z.left and x==y.left:
						rightRotate(z)
						break
					elif y==z.right and x==y.right:
						leftRotate(z)
						break
					elif y==z.left:
						leftRotate(y)
						rightRotate(z)
						continue
					else:
						rightRotate(y)
						leftRotate(z)
						continue
	def delete(self,n):
		n=self.search(n)
		if n==None:
			return "Error"
		else:
			if n.left==None and n.right==None:
				t=n.parent
				while t!=None:
					while abs(height(t))<=1:
						t=t.parent
					if t==None:
						return
					else:
						z=t
						if val<z.key:
							y=z.right
						else:
							y=z.left
						if height(y.right)>height(y.left):
							x=y.right
						else:
							x=y.left
						if y==z.left and x==y.left:
							rightRotate(z)
						elif y==z.right and x==y.right:
							leftRotate(z)
						elif y==z.left:
							leftRotate(y)
							rightRotate(z)
							continue
						else:
							rightRotate(y)
							leftRotate(z)
							continue
	def prefix(self):
		self.root.prefix()
		print()

def main():
	T=AVLTree()
	T.insert(5)
	T.insert(4)
	T.insert(3)
	T.insert(2)
	T.prefix()
	T.delete(2)
	T.prefix()

def rightRotate(n):
	x=n.left
	x.parent=n.parent
	n.left=x.right
	x.right=n
	n.parent=x
def leftRotate(n):
	x=n.right
	x.parent=n.parent
	n.right=x.left
	x.left=n
	n.parent=x
main()