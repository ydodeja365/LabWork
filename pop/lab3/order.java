import java.util.Scanner;
class order
{
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the numbers:");
		int a[]=new int[3];
		for(int i=0;i<3;i++)
			a[i]=sc.nextInt();
		int inc=0,dec=0;
		for(int i=0;i<2;i++)
		{
			if (a[i]>=a[i+1])
				dec++;
			else if(a[i]<=a[i+1])
				inc++;
		}
		if(inc==2)
			System.out.println("Increasing order!");
		else if(dec==2)
			System.out.println("Decreasing order!");
		else
			System.out.println("Neither increasing nor decreasing!");
	}
}