#include <stdio.h>
#include <limits.h>

int max(int a,int b,int c)
{
	int r=a>b?a:b;
	int s=r>c?r:c;
	return s;
}
int maxCrossingSum(int a[],int l,int m,int h)
{
	int i,ls=INT_MIN,rs=INT_MIN,s=0;
	for(i=m;i>=0;i--)
		s+=a[i];
	if(s>ls)
		ls=s;
	s=0;
	for(i=m+1;i<=h;i++)
		s+=a[i];
	if(s>rs)
		rs=s;
	return ls+rs;
}
int maxSubArray(int a[],int l,int r)
{
	int n=l-r+1;
	if(n==0)
		return 0;
	else if(n==1)
		return a[l];
	else
	{
		int m=(l+r)/2;
		return max(maxSubArray(a,l,m),maxSubArray(a,m+1,r),maxCrossingSum(a,l,m,r));
	}
}
int main()
{
	int n,i;
	printf("Enter n:");
	scanf("%d",&n);
	int a[n];
	printf("Enter array:\n");
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	printf("Max Sum of any subarray=%d\n",maxSubArray(a,0,n-1));
	return 0;
}