import java.util.Scanner;
class hexadecimal
{
	public static void main(String args[])
	{
		Scanner s = new Scanner(System.in);
		System.out.println("Enter number to be converted:");
		int num = s.nextInt();
		String ans="";
		while(num>0)
		{
			int rem = num%16;
			if(rem<10)
				ans=Integer.toString(rem)+ans;
			else
			{
				char ch_val = (char)(rem-10+97);
				ans=Character.toString(ch_val)+ans;
			}
			num/=16;
		}
		System.out.println("Answer = "+ans);
	}
}