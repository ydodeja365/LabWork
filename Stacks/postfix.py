from stack import Stack
def solvePostfix(expr):
	S=Stack()
	arr=expr.split()
	for i in arr:
		if isOperator(i):
			u=S.pop()
			v=S.pop()
			S.push(evaluate(v,u,i))
		else:
			S.push(i)
	return S.pop()
def isOperator(i):
	return i in "*/-+"
def evaluate(a,b,op):
	a=int(a)
	b=int(b)
	if op=="+":
		return a+b
	elif op=="*":
		return a*b
	elif op=="/":
		return a/b
	elif op=="-":
		return a-b
	print("Invalid")
	return
def main():
	ex=input("Enter expression:")
	print(solvePostfix(ex))
if __name__=='__main__':
	main()