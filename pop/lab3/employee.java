import java.util.Scanner;
class employee
{
	String name;
	double BP;
	double Bonus;
	double HRA;
	double PF;
	double result;
	public static void main(String args[])
	{
		Scanner s = new Scanner(System.in);
		System.out.println("Enter number of employees:");
		int n = s.nextInt();
		employee Obj[] = new employee[n];
		for(int i=0;i<n;i++)
		{
			Obj[i] = new employee();
			System.out.println("Enter name and basic pay:");
			Obj[i].name = s.next();
			Obj[i].BP = s.nextDouble();
			Obj[i].Bonus = 0.2*Obj[i].BP;
			Obj[i].HRA = 0.3*Obj[i].BP;
			Obj[i].PF = 0.1*Obj[i].BP;
			Obj[i].result = Obj[i].BP+Obj[i].Bonus+Obj[i].HRA-Obj[i].PF;
		}
		System.out.println("\nOutput:\n");
		for(int i=0;i<n;i++)
		{
			System.out.println("Name: "+Obj[i].name);
			System.out.println("Final Pay: "+Obj[i].result);
		}
	}
}