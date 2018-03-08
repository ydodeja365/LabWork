import java.util.Scanner;
class search
{
	public static void main(String[] args)
	{
		Scanner s = new Scanner(System.in);
		System.out.println("Enter size of array:");
		int n1 = s.nextInt();
		int a[] = new int[n1];
		System.out.println("Enter the array:");
		for(int i=0;i<n1;i++)	
			a[i] = s.nextInt();
		System.out.println("Enter element whose index is to be found:");
		int x = s.nextInt();
		for(int i=0;i<n1;i++)
			if(x==a[i])
				System.out.println("Element found at position "+(i+1));
	}
}