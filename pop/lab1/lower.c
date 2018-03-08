#include <stdio.h>
void main()
{
	int m,n,i,j;
	printf("Enter m and n:\n");
	scanf("%d %d",&m,&n);
	int a[m][n];
	printf("Enter the elements:\n");
	for(i=0;i<m;i++)
		for(j=0;j<n;j++)
			scanf("%d",&a[i][j]);
	for(i=0;i<m;i++)
		{
			for(j=0;j<=i;j++)
				printf("%d ",a[i][j]);
			printf("\n");
		}
}