#include <stdio.h>
void main()
{
	int n,i,j;
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		for(j=n-i;j>0;j--)
			printf(" ");
		for(j=1;j<=2*i-1;j++)
			printf("%d",j);
		printf("\n");
	}
	for(i=1;i<n;i++)
	{
		for(j=1;j<=i;j++)
			printf(" ");
		for(j=1;j<=(2*(n-i)-1);j++)
			printf("%d",j);
		printf("\n");
	}
}