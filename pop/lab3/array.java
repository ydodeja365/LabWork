import java.util.Scanner;
class common
{
	public static void main(String args[])
	{
		Scanner s = new Scanner(System.in);
		System.out.println("Enter size of first array:");
		int n1 = s.nextInt();
		System.out.println("Enter first array:");
		int a[] = new int[n1];
		for(int i=0;i<n1;i++)
			a[i] = s.nextInt();
		System.out.println("Enter size of second array:");
		int n2 = s.nextInt();
		System.out.println("Enter second array:");
		int b[] = new int[n2];
		for(int i=0;i<n2;i++)
			b[i] = s.nextInt();
		for(int i=0;i<n1;i++)
		{
			int cur = a[i];
			for(int j=0;j<n2;j++)
				if(cur==b[j])
				{
					System.out.println("Common element "+cur+" found at position "+i+" and position "+j);
					break;
				}
		}
	}
}