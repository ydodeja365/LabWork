import java.util.Scanner;
class overload
{
	static double volume(double a)
	{
		return a*a*a;
	}
	static double volume(double l, double b, double h)
	{
		return l*b*h;
	}
	static double volume(double r,double h)
	{
		return Math.PI*Math.pow(r,2)*h;
	}
	static double volume(float r,float h)
	{
		return Math.PI*Math.pow(r,2)*h/3;
	}
	static double volume(float area,double height)
	{
		return area*height;
	}
	public static void main(String args[])
	{
		Scanner s = new Scanner(System.in);
		System.out.println("1.Cube\n2.Cuboid\n3.Cylinder\n4.Cone\n5.Rectangular Box");
		System.out.println("Enter choice:");
		int c = s.nextInt();
		double r,h;
		switch(c)
		{
			case 1: System.out.println("Enter side:");
					double a = s.nextDouble();
					System.out.println("Volume = "+volume(a));
					break;
			case 2: System.out.println("Enter l,b,h:");
					double l = s.nextDouble();
					double b = s.nextDouble();
					h = s.nextDouble();
					System.out.println("Volume = "+volume(l,b,h));
					break;
			case 3: System.out.println("Enter r,h:");
					r = s.nextDouble();
					h=s.nextDouble();
					System.out.println("Volume = "+volume(r,h));
					break;
			case 4: System.out.println("Enter r,h:");
					float rad = s.nextFloat();
					float hei = s.nextFloat();
					System.out.println("Volume = "+volume(rad,hei));
					break;
			case 5: System.out.println("Enter area and height:");
					float area = s.nextFloat();
					h = s.nextDouble();
					System.out.println("Volume = "+volume(area,h));
					break;
			default: System.out.println("Invalid choice!");
		}
	}
}