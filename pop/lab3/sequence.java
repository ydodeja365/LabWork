import java.util.Scanner;
class sequence
{
	public static void main(String args[])
	{
		System.out.println("Enter length of array:");
		Scanner sc = new Scanner(System.in);
		int l = sc.nextInt();
		int a[] = new int[l];
		System.out.println("Enter the array:");
		for(int i=0;i<l;i++)
			a[i]=sc.nextInt();
		int leng = 1;
		int max = 1;
		for(int i=0;i<l;i++)
		{
			leng = 1;
			int cur = a[i];
			for(int j=0;j<l;j++)
			{
				if(a[j]==(cur+1))
				{
					cur = a[j];
					leng++;
					j=0;
					if(leng>max)
						max = leng;
				}
			}
		}
		System.out.println("Length of longest subsequence = "+max);
	}
}