package normalcoding;
import java.util.Scanner;

public class Solution {
    public static void main (String args []) { 
        Scanner sc=new Scanner(System.in);
        int x1=sc.nextInt();
        int v1=sc.nextInt();
        int x2=sc.nextInt();
        int v2=sc.nextInt();
        if (x2>x1) { 
            if (v2>v1){ 
System.out.println("NO");
System.exit(0);
            }
        }
        if(x1>x2){ 
            if(v1>v2){
                System.out.println("NO");
                System.exit(0);
            }
        }
        while(true){ 
            if (x1==x2){ 
               System.out.println("YES");
                System.exit(0);
            }
            x1=x1+v1;
            x2=x2+v2;
        }
    
   
    }

}