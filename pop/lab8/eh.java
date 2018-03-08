    public class eh{  
      public static void main(String args[]){  
       try{  
        int a[]=new int[5];  
        a[3]=30/0;  
       }  
       catch(ArithmeticException e){System.out.println("Arithmetic Exception");}  
       catch(ArrayIndexOutOfBoundsException e){System.out.println("Out of Bounds");}  
       catch(Exception e){System.out.println("Another exception");}    
     }  
    }  