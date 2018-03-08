interface base
{
	public void display();
	public void add(int a,int b);	
}
class adapter implements base
{
	@Override
	public void display(){}
	@Override
	public void add(int a,int b){}
}
class User1 extends adapter
{
	@Override
	public void add(int a,int b)
	{
		System.out.println(a+b);
	}
}
class User2 extends adapter
{
	@Override
	public void display()
	{
		System.out.println("Adapter classes!!");
	}
}
class Printer
{
	public static void main(String args[])
	{
		User1 o1=new User1();
		o1.add(2,3);
		User2 o2=new User2();
		o2.display();
	}
}