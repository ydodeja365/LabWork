#include <stdio.h>
int cmp(char *a,char *b)
{
	int r,s;
	for(;*a;a++)
		r+=*a;
	for(;*b;b++)
		s+=*b;
	return r-s;
}
void concat(char *a,char *b)
{
	int i;
	for(i=0;*a;a++,i++);
	for(;*b;b++)
		*(a+i)=*b;
}
void cpy(char *a,char *b)
{
	*a='\0';
	for(;*b;b++)
		*a=*b;
}
int len(char *a)
{
	int l=0;
	for(;*a;a++)
		l++;
	return l;
}
		
void main()
{
	char s1[200],s2[100];
	scanf("%s",s1);
	printf("Length = %d\n",len(s1));
	printf("Enter another string:");
	scanf("%s",s2);
	printf("strcmp(s1,s2) = %d\n",cmp(s1,s2));
	concat(s1,s2);
	printf("strcat(s1,s2);\ns1 = %s\ns2 = %s\n",s1,s2);
	cpy(s1,s2);
	printf("strcpy(s1,s2);\ns1 = %s\ns2 = %s\n",s1,s2);
}
