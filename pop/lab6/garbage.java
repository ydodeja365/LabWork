class garbage
{
	int a;
	protected void finalize() throws Throwable
    {
        System.out.println("Garbage collector called");
        System.out.println("Object garbage collected : " + this);
    }
	public static void main(String args[])
	{
		garbage o1=new garbage();
		o1.a=2;
		garbage o2=new garbage();
		o2=o1;
		System.gc();
	}
}