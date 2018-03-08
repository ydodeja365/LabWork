#include <stdio.h>
#include <ctype.h>
void main()
{
	char ch;
	FILE *fp =fopen("yash.txt","rw+");
	while((ch = fgetc(fp))!=EOF)
	{
		ch = toupper(ch);
		fputc(ch,fp);
	}

}