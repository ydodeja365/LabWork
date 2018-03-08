#include <stdio.h>
struct student
{
	int roll;
	char name[25];
};
void main()
{
	int n,i;
	printf("Enter number of students:");
	scanf("%d",&n);
	printf("Enter student details:\n");
	struct student a[n];
	for(i=0;i<n;i++)
	{
		printf("Student %d:\n",i+1);
		printf("Enter name:");
		scanf("%s",a[i].name);
		printf("Enter roll no:");
		scanf("%d",&a[i].roll);
	}
	printf("Printing details...\n");
	for(i=0;i<n;i++)
	{
		printf("Student %d\n",i+1);
		printf("Name = %s\nRoll no = %d\n",a[i].name,a[i].roll);
	}
}
