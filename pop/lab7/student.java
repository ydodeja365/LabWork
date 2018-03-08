import yash.java.Attendance;
import java.util.Scanner;
class student
{
	public static void main(String args[])
	{
		Scanner s = new Scanner(System.in);
		System.out.println("Enter number of students:");
		int n=s.nextInt();
		Attendance a[] = new Attendance[n];
		System.out.println("Enter Attendance of each member:");
		for(int i=0;i<n;i++)
		{
			a[i]=new Attendance();
			int num=s.nextInt();
			a[i].giveAttendance(num);
		}
		for(int i=0;i<n;i++)
		{
			a[i].display();
		}
	}
}