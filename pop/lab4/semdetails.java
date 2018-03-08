import java.util.Scanner;
class semdetails
{
	float GPA;
	public static void main(String args[])
	{
		Scanner s = new Scanner(System.in);
		semdetails obj[] = new semdetails[8];
		System.out.println("Enter all 8 sems GPA:");
		float sum = 0;
		for(int i=0;i<8;i++)
		{
			obj[i] = new semdetails();
			obj[i].GPA = s.nextFloat();
			sum+=obj[i].GPA;
		}
		float CGPA = sum/8;
		System.out.println("Your CGPA is:"+ CGPA);
	}
}