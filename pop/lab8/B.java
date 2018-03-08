package yash.test;
class p3{
	static int a=5;
}
public class B extends p3{
	public void print()
	{
		System.out.println("Internal class B's member:"+B.a);
	}
}