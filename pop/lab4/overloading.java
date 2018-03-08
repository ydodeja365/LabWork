import java.util.Scanner;
class overloading
{
	double area(double r,double h)
	{
		return Math.PI*r*(r+Math.sqrt(Math.pow(h,2)+Math.pow(r,2)));
	}
	double area(float r,double h)
	{
		return (2*Math.PI*r*h+2*Math.PI*Math.pow(r,2));
	}
	double area(double l,double w,double h)
	{
		return 2*(w*l+h*l+h*w);
	}
	double area(double l,float w,double h)
	{
		return l*w+l*Math.sqrt(Math.pow(w/2,2)+Math.pow(h,2))+w*Math.sqrt(Math.pow(l/2,2)+Math.pow(h,2));
	}
	double area(double r)
	{
		return 2*Math.PI*Math.pow(r,2);
	}
	
	public static void main(String args[])
	{
		Scanner s = new Scanner(System.in);
		System.out.println("1.Cone\n2.Cylinder\n3.Prism\n4.Pyramid\n5.Hemisphere");
		System.out.println("Enter your choice:");
		char ch = s.nextChar();
		double r,h,w;float r1;
		switch(ch)
		{
			case '1': System.out.println("r,h:");
					  r=s.nextDouble();
					  h=s.nextDouble();
					  System.out.println("Area = "+area(r,h));
					  break;
			case '2': System.out.println("r,h:");
					  r1=s.nextFloat();
					  h=s.nextDouble();
					  System.out.println("Area = "+area(r1,h));
					  break;
			case '3': System.out.println("l,w,h:");
					  r=s.nextDouble();
					  h=s.nextDouble();
					  w=s.nextDouble();
					  System.out.println("Area = "+area(r,h,w));
					  break;
			case '4': System.out.println("l,w,h:");
					  r=s.nextDouble();
					  r1=s.nextFloat();
					  h=s.nextDouble();
					  System.out.println("Area = "+area(r,r1,h));
					  break;
			case '5': System.out.println("r:");
					  r=s.nextDouble();
					  System.out.println("Area = "+area(r));
					  break;
		}
	}
}