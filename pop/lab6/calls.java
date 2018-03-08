class calls
{
	int var1,var2;
	void swapByValue(int a,int b)
	{
		a+=b;
		b=a-b;
		a-=b;
		System.out.println("a:"+a+" b:"+b);
	}
	void swapByRef()
	{
		this.var1+=this.var2;
		this.var2=this.var1-this.var2;
		this.var1-=this.var2;
		System.out.println("a:"+this.var1+" b:"+this.var2);
	}
	public static void main(String args[])
	{
		calls o1=new calls();
		o1.var1=3;o1.var2=2;
		System.out.println("a:3 b:2");
		System.out.println("In callByValue:");
		o1.swapByValue(o1.var1,o1.var2);
		System.out.println("After callByValue:");
		System.out.println("a:"+o1.var1+" b:"+o1.var2);
		System.out.println("In callByRef:");
		o1.swapByRef();
		System.out.println("After callByRef:");
		System.out.println("a:"+o1.var1+" b:"+o1.var2);
	}
}