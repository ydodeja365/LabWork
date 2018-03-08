#include <stdio.h>
void main()
{
	int n,i=0;
	printf("Enter length of array:");
	scanf("%d",&n);
	int a[n];
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	int *p=a;
	for(i=0;i<n;i++)
		printf("%d - %p\n",*(p+i),p+i);
}
