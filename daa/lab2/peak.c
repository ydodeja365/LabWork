#include <stdio.h>
int peak(int a[],int l,int r)
{
	if(l<r)
	{
		int m=(l+r)/2;
		if(a[m]>a[m+1])
			r=m;
		else
			l=m+1;
		return peak(a,l,r);
	}
	else
		return a[l];
}
int main()
{
	int n,i;
	printf("Enter number of elements:");
	scanf("%d",&n);
	int a[n];
	printf("Enter array elements:");
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	printf("Peak is:%d\n",peak(a,0,n-1));
	return 0;
}