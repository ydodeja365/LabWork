import java.util.Scanner;
class marks
{
		String name;
		float s1,s2,s3,s4,s5;
}
class student
{
	public static void main(String args[])
	{
		Scanner s =new Scanner(System.in);
		System.out.println("Enter number of students:");
		int n = s.nextInt();
		marks obj[] = new marks[n];
		for(int i=0;i<n;i++)
		{
			obj[i] = new marks();
			System.out.println("Enter name:");
			obj[i].name = s.next();
			System.out.println("Enter marks in 5 subjects:");
			obj[i].s1 = s.nextFloat();
			obj[i].s2 = s.nextFloat();
			obj[i].s3 = s.nextFloat();
			obj[i].s4 = s.nextFloat();
			obj[i].s5 = s.nextFloat();
		}
		for(int i=0;i<n;i++)
		{
			System.out.println("Name: "+obj[i].name+"\nSum: "+sum(obj[i]));
		}
	}
	static float sum(marks obj)
		{
			return obj.s1+obj.s2+obj.s3+obj.s4+obj.s5;
		}
}