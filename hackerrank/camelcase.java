package hackerrank;
import java.util.Scanner;
public class camelcase {
    public static void main(String args[]){ 
        Scanner sc=new Scanner(System.in);
        String s=sc.next();
        char c=' ';
        int count=1;
        for( int i=0;i<s.length();i++){ 
            c=s.charAt(i);
            if(Character.isUpperCase(c)){
                count++;
            }else{
                continue;
            }

            }
        System.out.println(count);
        sc.close();
        }
    }

