import java.util.Scanner;
class eq1
{
	public static void main(String args[])
	{
		System.out.println("Enter a,b,c:");
		Scanner sc = new Scanner(System.in);
		float a = sc.nextFloat(),b = sc.nextFloat(),c = sc.nextFloat();
		System.out.println("Enter p,q,r:");
		float p = sc.nextFloat(),q = sc.nextFloat(),r = sc.nextFloat();
		float d = a*q-b*p, d1 = c*q-b*r, d2 = a*r-c*p;
		System.out.println("Result is "+d1/d + " "+d2/d);
	}
}