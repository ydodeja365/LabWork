interface Stacks
{
	int pop();
	void push(int item);
	boolean isEmpty();
	int top();
}
class Stack implements Stacks
{
	int topIndex,arr[];
	Stack(int size)
	{
		arr=new int[size];
		topIndex=-1;
	}
	public boolean isEmpty()
	{
		return this.topIndex==-1;
	}
	public int pop()
	{
		if(this.isEmpty()){
			IndexOutOfBoundsException e=new IndexOutOfBoundsException("Stack Underflow!");
			throw e;
		}
	
			return this.arr[this.topIndex--];
	}
	public int top()
	{
		if(this.isEmpty()){
			IndexOutOfBoundsException e=new IndexOutOfBoundsException("Stack Overflow!");
			throw e;
		}
	
			return this.arr[this.topIndex];
	}
	public void push(int item)
	{
		if(this.topIndex==this.arr.length-1){
			IndexOutOfBoundsException e=new IndexOutOfBoundsException("Stack Underflow!");
			throw e;
		}
		this.arr[++this.topIndex]=item;
	}
	void print()
	{
		if(this.isEmpty())
			System.out.println("Empty!");
		else{
			for(int i=0;i<=this.topIndex;i++)
				System.out.print(this.arr[i]+" ");
			System.out.println();
		}
	}
}
class p7{
	public static void main(String args[])
	{
		Stack s=new Stack(5);
		s.print();
		s.push(1);
		s.print();
		s.push(2);
		s.push(3);
		s.push(2);
		s.push(5);
	
		System.out.println(s.pop());
		s.print();
	}
}