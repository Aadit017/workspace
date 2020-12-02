package java_code;
import java.util.*;
public class square_triangular {
    public static void main(String args[]){ 
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        System.out.println("the statement that "+n+" is a triangular number is "+func(n));
        System.out.println("the statement that "+n+" is a sqaure number is "+func_2(n));
        sc.close();
    }
public static boolean func(int n ){ 
    double value=8*(n)+1;
    double sq = Math.sqrt(value); 
	return ((sq - Math.floor(sq)) == 0); 
    } 
public static boolean func_2(int n ){ 
    double sq=Math.sqrt(n);
    return ((sq- Math.floor(sq))==0);
}
}
