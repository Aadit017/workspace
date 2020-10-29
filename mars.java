package hackerrank;
import java.util.Scanner ;
public class mars{ 
    public static void main (String args[]){ 
        Scanner sc=new Scanner(System.in);
        String s=sc.next();
        String flag="";
        int n=s.length()/3;
        for(int i=0;i<n;i++){ 
            flag=flag+"SOS";
        }
        int counter=0;
        char ch=' ';
        char ch_1=' ';
        for (int i=0;i<s.length();i++){ 
            ch=s.charAt(i);
            ch_1=flag.charAt(i);
            if(ch!=ch_1){ 
                counter++;
            }
        }
    System.out.println(counter);
    sc.close();
    }
}