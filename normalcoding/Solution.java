package normalcoding;

import java.util.Scanner;

public class Solution {
    public static void main (String args []) { 
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int arr[]=new int[n];
        int min =0,max=0;
        for (int i =0;i<n;i++){ 
            arr[i]=sc.nextInt();
        }
        for (int i=0;i<n;i++){ 
    if (min<arr[i]){ 
    min=arr[i];
    System.out.println(min);
    }
    if  (max>arr[i]){ 
     max=arr[i];
     System.out.println(max);
    }
    continue ;
}
System.out.println(min+' '+max);
sc.close();
} 
} 

