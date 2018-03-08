import java.util.Scanner;
import java.lang.System.*;
class binary
{
	public static void main(String args[])
	{
		Scanner s = new Scanner(System.in);
		int num;
		System.out.println("Enter the decimal number:");
		num = s.nextInt();
		String bin = "";
		while(num>0)
		{
			if(num%2==1)
				bin = bin + "1";
			else
				bin = bin + "0";
			num/=2;
		}
		System.out.println("Binary value = ");
		for(int i=bin.length()-1;i>=0;i--)
			System.out.print(bin.charAt(i));
		System.out.println();
	}
}