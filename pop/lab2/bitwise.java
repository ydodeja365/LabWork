import java.util.Scanner;
class bitwise
{
	public static void main(String args[])
	{
		Scanner s = new Scanner(System.in);
		System.out.println("Enter number to be shifted:");
		int n = s.nextInt();
		System.out.println("Enter number of bits:");
		int k = s.nextInt();
		int rus = n>>>k;
		int rs = n>>k;
		int ls = n<<k;
		System.out.println("Right Unsigned Shift -> " + Integer.toString(rus) + "\nRight Shift -> " + Integer.toString(rs) + "\nLeft Shift -> " + Integer.toString(ls));
	}
}