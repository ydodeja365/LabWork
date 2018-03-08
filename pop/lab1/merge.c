#include <stdio.h>
int * sort(int *a,int n)
{
	int i,j,t;
	for(i=0;i<n;i++)
	{
		for(j=i;j<n;j++)
		{
			if(*(a+i)<*(a+j))
			{
				t=*(a+i);
				*(a+i)=*(a+j);
				*(a+j)=t;
			}
		}
	}
	return a;
}
void merge(int *a1, int *a2,int l1,int l2)
{
	int i=0,j=0,k=0;
	int final[l1+l2];
	while(i<l1||j<l2)
	{
		if(i<l1&&j<l2)
		{
			if(*(a1+i)>*(a2+j))
			{
				final[k]=*(a1+i);
				i++;k++;
			}
			else if(*(a2+j)>=*(a1+i))
			{
				final[k]=*(a2+j);
				j++;k++;
			}
		}
		else if(i==l1)
		{
			final[k]=*(a2+j);
			j++;k++;
		}
		else
		{
			final[k]=*(a1+i);
			i++;k++;
		}
	}
	printf("Merged array =\n");
	for(i=0;i<l1+l2;i++)
		printf("%d ",final[i]);
	printf("\n");
}
void main()
{
	int l1,l2,i;
	printf("Enter length of first array:");
	scanf("%d",&l1);
	printf("Enter length of second array:");
	scanf("%d",&l2);
	int a[l1],b[l2];
	printf("Enter first array:\n");
	for(i=0;i<l1;i++)
		scanf("%d",&a[i]);
	printf("Enter second array:\n");
	for(i=0;i<l2;i++)
		scanf("%d",&b[i]);
	int *ap = a;
	int *bp = b;
	merge(sort(ap,l1),sort(bp,l2),l1,l2);	
}