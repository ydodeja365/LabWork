class A
{
	interface show
	{
		void display();
	}
}
class subinterface implements A.show
{
	int a=3;
	@Override
	public void Hey()
	{
		System.out.println("Hey");
	}
	public void display()
	{
		System.out.println(this.a);
	}
	public static void main(String args[])
	{
		A.show o1=new subinterface();
		o1.display();
		//o1.Hey(); Cannot be implemented!!
	}
}