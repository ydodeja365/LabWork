#include <stdio.h>
void main()
{
	int n,i,t;
	printf("Enter length of array:");
	scanf("%d",&n);
	printf("Enter the array:\n");
	int a[n];
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	int max = a[0], max_index = 0;
	int min = a[0], min_index = 0;
	for(i=0;i<n;i++)
	{
		if(a[i]>max)
		{
			max = a[i];
			max_index = i;
		}
		if(a[i]<min)
		{
			min = a[i];
			min_index = i;
		}
	}
	t = a[max_index];
	a[max_index] = a[min_index];
	a[min_index] = t;
	printf("Interchanged array:\n");
	for(i=0;i<n;i++)
		printf("%d ",a[i]);
	printf("\n");
}