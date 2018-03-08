package yash.java;
class newStudent
{
	int a=0;
}
public class Attendance extends newStudent
{
	public void giveAttendance(int n)
	{
		this.a=n;
	}
	public void display()
	{
		System.out.println("Your attendance:"+this.a);
	}
}