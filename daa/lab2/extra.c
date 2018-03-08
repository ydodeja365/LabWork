#include <stdio.h>
int main()
{
	int n,i;
	printf("Enter n:");
	scanf("%d",&n);
	int a[n],sum[n];
	printf("Enter the sequence:");
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
		sum[i]=a[i];
	}
	int max=a[0],max_i=0;
	for(i=0;i<n;i++)
	{
		if(i>=1)
		{
			sum[i]+=sum[i-1];
		}
		if(a[i]<0||sum[i]<0)
		{
			sum[i]=0;
		}
		if(sum[i]>=max)
		{
				max=sum[i];
				max_i=i;
		}
	}
	for(i=0;i<n;i++)
	{
		printf("%d,",sum[i]);
	}
	int x=max_i;
	while(x>=0)
	{
		if(sum[x]>0&&max!=0)
		{
			printf("\nmax=%d\n",max);
			max-=a[x];
			printf("\n%d,x=%d\n",max,x);
			x--;
		}
		else
			break;
	}
	printf("Subsequence with largest sum is:\n");
	for(i=x+1;i<=max_i;i++)
		printf("%d ",a[i]);
	printf("\n");
	return 0;
}