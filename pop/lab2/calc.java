import java.util.Scanner;
import java.lang.System.*;
class calc{
	public static void main(String args[])
	{
		Scanner s = new Scanner(System.in);
		int ch;
		System.out.println("WELCOME TO CALCULATOR!");
		System.out.println("Choose your operation:\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n");
		System.out.println("Enter your choice:");
		ch = s.nextInt();
		System.out.println("Enter the two operands:");
		double a = s.nextDouble();
		double b = s.nextDouble();
		System.out.println("Answer:");
		switch(ch)
		{
			case 1:System.out.println(a+b);
					break;
			case 2:System.out.println(a-b);
					break;
			case 3:System.out.println(a*b);
					break;
			case 4:System.out.println(a/b);
					break;
			default:
				System.out.println("Invalid operator entered!");
		}
	}
}