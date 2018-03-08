#include <stdio.h>
struct prod
{
	char name[25];
	float price;
};
void main()
{
	struct prod arr[5];
	arr[0].name = "Detergent";
	arr[0].price = 58;
	struct prod * list = arr;
}