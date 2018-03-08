class personalDetails
{
	String name;
	int rating;
	double basicSal;
	personalDetails(String a,double sal,int b)
	{
		name=a;
		basicSal=sal;
		rating=b;
	}
	char evaluation()
	{
		if(rating>4)
			return 'A';
		else if(rating>3)
			return 'B';
		else if(rating>2)
			return 'C';
		return 'i';
	}
	double payroll()
	{
		char grade=evaluation();
		double payroll;
		if(grade=='A')
			payroll=1.3*basicSal;
		else if(grade=='B')
			payroll=1.2*basicSal;
		else
			payroll=1.1*basicSal;
		return payroll;
	}
}
class inheritance extends personalDetails
{
	inheritance(String a,double b,int c)
	{
		super(a,b,c);
	}
	public static void main(String args[])
	{
		inheritance o1 = new inheritance("Yash",10000,4);
		System.out.println(o1.evaluation()+" "+o1.payroll());
	}
}