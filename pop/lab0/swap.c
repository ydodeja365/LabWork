#include <stdio.h>
void callByVal(int a,int b)
{
	int t;
	t=a;
	a=b;
	b=t;
	printf("In callByVal a,b = %d,%d\n",a,b);
}
void callByRef(int *a,int *b)
{
	int t;
	t=*a;
	*a=*b;
	*b=t;
	printf("In callByRef a,b =%d,%d\n",*a,*b);
}
void main()
{
	int a,b;
	scanf("%d %d",&a,&b);
	printf("Before Swapping a,b = %d,%d\n",a,b);
	callByVal(a,b);
	printf("After call by value a,b = %d,%d\n",a,b);
	callByRef(&a,&b);
	printf("After call by reference a,b = %d,%d\n",a,b);
}

