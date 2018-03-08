#include <stdio.h>
void toh(int n,char s,char i,char t)
{
	if(n>=1)
	{
		toh(n-1,s,t,i);
		printf("Move disc %d from %c to %c\n",n,s,t);
		toh(n-1,i,s,t);
	}
}
int main()
{
	int n;
	printf("Enter number of discs:");
	scanf("%d",&n);
	toh(n,'S','I','T');
	return 0;
}