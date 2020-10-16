package normalcoding;
import java.util.Scanner;
public class viral_advertisement{ 
    public static void main(String args[]){ 
        Scanner sc =new Scanner (System.in);
        int n=sc.nextInt();
        double share=5.0;
        int likes=0;
        int i=1;
        double s;
        while(i<n+1)
        { 
          s=Math.floor(share/2.0);
          likes+=Math.floor(share/2.0);
          share=s*3;
          i+=1;        
        }    
    System.out.println(likes);
    
}
}