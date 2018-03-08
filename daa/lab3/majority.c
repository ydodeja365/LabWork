#include <stdio.h>
int countGTnby2(char e,char a[],int n)
{
	int i,c=0;
	for(i=0;i<n;i++)
		if(a[i]==e)
			c++;
	return c>(n/2);
}
int equivalent(char a,char b)
{
	//printf("%d",a==b);
	return a==b;
}
char findMajority(char* a,int s,int e,int n)
{
	if(s==e)
		return *(a+s);
	else if(e-s==1)
	{
		if(equivalent(*(a+s),*(a+e)))
			return *(a+s);
		else
			return '!';
	}
	else
	{
		int m=(s+e)/2;
		char x=findMajority(a,s,m,n);
		if(countGTnby2(x,a,n))
			return x;
		char y=findMajority(a,m+1,e,n);
		if(countGTnby2(y,a,n))
			return y;
		else
			return '!';
	}
}
int main()
{
	int n,i;
	printf("Enter n:");
	scanf("%d",&n);
	char a[n];
	printf("Enter array:");
	for(i=0;i<n;i++)
		scanf(" %c",&a[i]);
	char m=findMajority(a,0,n-1,n);
	if(m=='!')
		printf("No majority element!\n");
	else
		printf("Majority element=%c\n",m);
	return 0;
}