import java.util.Scanner;
class details
{
	float cost;
	String name;
	void print()
	{
		System.out.println("Name: "+name+"\nCost: "+cost);
	}
}
class product
{
	public static void main(String args[])
	{
		Scanner s = new Scanner(System.in);
		System.out.println("Enter number of products:");
		int n = s.nextInt();
		details x[] = new details[n];
		System.out.println("Enter list of products:");
		//Making user enter product list 
		for(int i=0;i<n;i++)
		{
			System.out.println("Enter name:");
			x[i] = new details();
			x[i].name = s.next();
			System.out.println("Enter cost:");
			x[i].cost = s.nextFloat();
		}
		//Display product list
		System.out.println("\nSuccess! Your product list is:");
		for(int i=0;i<n;i++)
		{
			System.out.println((i+1)+".  ");
			x[i].print();
		}
		double total = 0;
		//Selecting product list
		while(1<2)
		{
			System.out.println("Enter the product number you want to select:");
			int num = s.nextInt();
			int quantity = 1;
			System.out.println("Enter quantity:");
			while(1<2)
			{
				int q1 = s.nextInt();
				if(q1>=quantity)
				{
					quantity =q1;
					break;
				}
				else
					System.out.println("Invalid..Enter again...");
			}
			if(num<=n)
				total+=x[num-1].cost*quantity;
			else
			{	System.out.println("Invalid! Enter again..");
				continue;
			}
			System.out.println("Want to quit?(Y/N)?");
			int flag=0;
			while(1<2)
			{
				char ch = s.next().charAt(0);
				if(ch=='Y'||ch=='y')
				{
					flag = 1;
					break;
				}
				else if(ch=='N'||ch=='n')
				{
					break;
				}
				else
					System.out.println("Enter again! Invalid!");
			}
			if(flag==1)
				break;
		}
		System.out.println("Total = "+total);
		System.out.println("Thank You for shopping with us!");
	}
}