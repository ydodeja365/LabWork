import java.util.Scanner;
class tens
{
	public static void main(String[] args)
	{
		Scanner s = new Scanner(System.in);
		System.out.println("Enter size of array:");
		int n1 = s.nextInt();
		int a[] = new int[n1];
		System.out.println("Enter the array:");
		int sum = 0;
		for(int i=0;i<n1;i++)
		{	
			a[i] = s.nextInt();
			if(a[i]>=10 && a[i]<=99)
				sum+=a[i];
		}
		if(sum==30)
			System.out.println("True");
		else
			System.out.println("False");

	}
}