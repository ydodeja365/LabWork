import java.util.Scanner;
class ci
{
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter investment amount:");
		float P = sc.nextFloat();
		System.out.println("Enter rate of interest:");
		float R = sc.nextFloat();
		R/=12;
		System.out.println("Enter number of years:");
		float T = sc.nextFloat(),A=P;
		System.out.println("Years\tFutureValue");
		for(int i=1;i<=T;i++)
		{
			A*=Math.pow(1+(R/100),12);
			System.out.println(i+"\t"+A);
		}
	}
}