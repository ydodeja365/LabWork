MAX=100000
class Stack:
	def __init__(self):
		self.top=-1
		self.arr=[None]*MAX
	def pop(self):
		if self.top==-1:
			return "Underflow!"
		self.top-=1
		return self.arr[self.top+1]
	def push(self,v):
		if self.top==(MAX-1):
			print("Overflow!")
			return
		self.top+=1
		self.arr[self.top]=v
	def top(self):
		return self.arr[self.top]
	def isEmpty(self):
		return self.top==-1
	def __str__(self):
		print(self.arr[:self.top+1])

def main():
	S=Stack()
	for i in range(MAX+2):
		S.push(i)
	print(S.pop())
	print(S.pop())
	print(S.pop())
if __name__=='__main__':
	main()