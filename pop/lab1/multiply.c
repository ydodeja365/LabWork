#include <stdio.h>
int main()
{
	int m1,n1,m2,n2,i,j,k;
	printf("Enter m1 and n1:");
	scanf("%d %d",&m1,&n1);
	printf("Enter m2 and n2:");
	scanf("%d %d",&m2,&n2);
	if(n1!=m2)
	{
		printf("Cannot multiply! Invalid!\n");
		return 0;
	}
	else
	{
		int a[m1][n1],b[m2][n2],ans[m1][n2];
		printf("Enter elements of first matrix:\n");
		for(i=0;i<m1;i++)
			for(j=0;j<n1;j++)
				scanf("%d",&a[i][j]);
		printf("Enter elements of second matrix:\n");
		for(i=0;i<m2;i++)
			for(j=0;j<n2;j++)
				scanf("%d",&b[i][j]);
		for(i=0;i<m1;i++)
			for(j=0;j<n2;j++)
				ans[i][j] = 0;
		for(i=0;i<m1;i++)
			for(j=0;j<n2;j++)
				for(k=0;k<m2;k++)
					ans[i][j]+=a[i][k]*b[k][j];
		printf("Multiplied matrix is:\n");
		for(i=0;i<m1;i++)
		{
			for(j=0;j<n2;j++)
				printf("%d ",ans[i][j]);
			printf("\n");
		}
	}
}