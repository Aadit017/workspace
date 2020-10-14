package normalcoding;
import java.util.Scanner;
import java.util.Arrays;
class angryprofessor{ 
    public static void main (String args[]){
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        
        for ( int counter=0;counter<t;counter++){ 
            int n=sc.nextInt();
            int k=sc.nextInt();
            int count=0;
            int a[]=new int[n];
            for (int i=0;i<n;i++){ 
                a[i]=sc.nextInt();
                if (a[i]<=0){ 
                    count++;
                }
            }
            if (count>=k){ 
                System.out.println("NO");
            }else{ 
                System.out.println("YES");
        }

        }
    }
}