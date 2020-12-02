package java_code;
public class code{ 
    public static void main(String args[]){ 
        int a=5,b=7;
        a=b++;
        a=a+b;
        b=a-b;
        a=a-b;
        System.out.println("guess what will a+b be---->"+ (a+b));
        }
}