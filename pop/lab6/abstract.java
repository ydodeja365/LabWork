import java.util.Scanner;
abstract class operations
{
	char bank;
	void Withdraw()
	{
		System.out.println("Withdrawn");
	}
	void Deposit()
	{
		System.out.println("Deposited");
	}
	abstract void calculate();
}
class banking extends operations
{
	void calculate()
	{
		if(this.bank=='A')
			System.out.println("Bank A");
		else if(this.bank=='B')
			System.out.println("Bank B");
		else
			System.out.println("Bank C");
	}
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		banking o1=new banking();
		o1.Withdraw();
		o1.Deposit();
		System.out.println("Enter Bank:");
		char ch=sc.next().charAt(0);
		o1.bank=Character.toUpperCase(ch);
		switch(ch)
		{
			case 'A':
			case 'a':o1.calculate();
					 break;
			case 'B':
			case 'b':o1.calculate();
					 break;
			case 'C':
			case 'c':o1.calculate();
					 break;
			default:System.out.println("No such bank!");
		}
	}
}