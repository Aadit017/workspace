package java_code;
import java.util.*;
public class skull{
    public static void main(String args[]){ 
        Scanner sc=new Scanner(System.in);
        System.out.println(" enter the value of n ");
        int n=sc.nextInt();
        int fact=0;
        double sth=0.0;
        double total_sum=0.0;
        for ( int i=1;i<=n;i++){ 
            fact=factorial(i);
            sth=1/fact;
            total_sum=total_sum+sth;
        }
        sc.close();
System.out.println("total sum"+total_sum);
}
    public static int factorial(int fact ){ 
        int sum=1;
        if (fact==0){ 
            return 0;
        }else if(fact==1){ 
            return 1;
        }else{ 
            for ( int i=fact;i>0;i--){ 
                sum=sum+(sum*i);
            }

        }
        return sum;
    }
}
