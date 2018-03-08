    public class userdef{  
       static void validate(int age){  
         if(age<18)  
          throw new ArithmeticException("Not valid, too young to vote!");  
         else  
          System.out.println("welcome to vote");  
       }  
       public static void main(String args[]){  
          validate(13);  
      }  
    }  