package rth;
import java.util.*;
import java.util.Scanner;
//import java.util.Arrays;
public class Solution { 
    public static void main(String args[]){ 
        Scanner sc =new Scanner(System.in);
        int x1=sc.nextInt();
        int v1=sc.nextInt();
        int x2=sc.nextInt();
        int v2=sc.nextInt();
        int jump_1=0,jump_2=0;
       String answer="no";
       int j=10;
         for(int i=0;i<=j;i++)
         jump_1=x1+v1;
         jump_2=x2+v2;
         if (jump_1==jump_2){ 
            answer="yes";
            j=0;
         }
         x1=x1+v1;
         x2=x2+v2;
        System.out.println(answer);
    }
}

        