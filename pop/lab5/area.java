import java.util.Scanner;
class P
{
	static double area;
	P()
	{
		area=0;
	}
	P(int a)
	{
		area=a*a;
	}
	P(float a)
	{
		area=Math.pow(a,3);
	}
	P(float l,float b)
	{
		area=l*b;
	}
	P(double r)
	{
		area=4*Math.PI*Math.pow(r,2);
	}
	P(double r,double h)
	{
		area=2*Math.PI*r*(h+r);
	}
}
class area extends P
{
	area()
	{
		super();
	}
	area(int a)
	{
		super(a);
	}
	area(float a)
	{
		super(a);
	}
	area(float l,float b)
	{
		super(l,b);
	}
	area(double r)
	{
		super(r);
	}
	area(double r,double h)
	{
		super(r,h);
	}
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		System.out.println("1.Square\n2.Cube\n3.Rectangle\n4.Sphere\n5.Cylinder");
		System.out.println("Enter your choice:");
		int ch = sc.nextInt();
		area o1=new area();double r;
		switch(ch)
		{
			case 1:
			System.out.println("Enter a:");
			int a = sc.nextInt();
			o1=new area(a);
			break;
			case 2:
			System.out.println("Enter a:");
			float a1 = sc.nextFloat();
			o1=new area(a1);
			break;
			case 4:
			System.out.println("Enter r:");
			r = sc.nextDouble();
			o1=new area(r);
			break;
			case 3:
			System.out.println("Enter l and b:");
			float l = sc.nextFloat();
			float b = sc.nextFloat();
			o1=new area(l,b);
			break;
			case 5:
			System.out.println("Enter r and h:");
			r = sc.nextDouble();
			double h=sc.nextDouble();
			o1=new area(r,h);
			break;
			default:System.out.println("Invalid!");
		}
		if(ch>0&&ch<6)
		System.out.println(o1.area);
		}
	}