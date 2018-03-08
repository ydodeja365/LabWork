#include <stdio.h>
#include <stdlib.h>
int merge(int a[],int b[],int l,int m,int r)
{
	int inv_count=0,i=l,j=m,k=l;
	while(i<=(m-1)&&j<=r)
	{
		if(a[i]>a[j])
		{
			b[k++]=a[j++];
			inv_count+=(m-i);
		}
		else
			b[k++]=a[i++];
	}
	while(i<=(m-1))
		b[k++]=a[i++];
	while(j<=r)
		b[k++]=a[j++];
	return inv_count;
}
int mergesort(int a[],int t[],int l,int r)
{
	int inv_count=0;
	if(l<r)
	{
		int m=(l+r)/2;
		inv_count=mergesort(a,t,l,m);
		inv_count+=mergesort(a,t,m+1,r);
		inv_count+=merge(a,t,l,m+1,r);
	}
	return inv_count;
}
int mergesort1(int a[],int n)
{
	int *tmp=(int *)malloc(sizeof(int)*n);
	return mergesort(a,tmp,0,n-1);
}
int main()
{
	printf("Enter number of elements:");
	int n,i;
	scanf("%d",&n);
	int a[n];
	printf("Enter the elements:\n");
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	int inv_count=mergesort1(a,n);
	printf("Number of inversions=%d\n",inv_count);
	return 0;
}