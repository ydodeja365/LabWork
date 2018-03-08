#include <stdio.h>
void revnum(int *a)
{
	int ans = 0;
	while(*a)
	{
		ans*=10;
		ans+=(*a)%10;
		*a/=10;
	}
	*a=ans;
}
void main()
{
	int n;
	printf("Input any number:");
	scanf("%d",&n);
	revnum(&n);
	printf("Reversed number = %d\n",n);
}
