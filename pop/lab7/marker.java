
import java.io.Serializable;

class A implements Cloneable
{
	int i;
	String s;

	// A class constructor
	public A(int i,String s)
	{
		this.i = i;
		this.s = s;
	}

	@Override
	protected Object clone()
	throws CloneNotSupportedException
	{
		return super.clone();
	}
}

public class marker
{
	public static void main(String[] args)
		throws CloneNotSupportedException
	{
		A a = new A(20, "Yash");

		A b = (A)a.clone();
		a.i=4;

		System.out.println(b.i);
		System.out.println(b.s);
	}
}