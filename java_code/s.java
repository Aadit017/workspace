/*import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;
public class Solution {
    // Complete the breakingRecords function below.
    static int[] breakingRecords(int[] scores) {
        int max=scores[0],min=scores[0]; 
        int countMin=-1,countMax=-1;
        int arr[]=new int[2];
        for(int i:scores){ 
            if(max>i){ 
                max=i;
                countMax+=1;
            }
            if(min<i){ 
                min=i;
                countMin+=1;
            }
        }
        arr[0]=countMax;
        arr[1]=countMin;
    return arr;
    }
public static void main(String[] args)  {
Scanner sc=new Scanner(System.in);
int n=sc.nextInt();
int arr[]=new int[n];
for(int i=0;i<n;i++){ 
    arr[i]=sc.nextInt();
}
int[] result= breakingRecords(arr);
System.out.println(result[0]+" "+result[1]);
    }
} 











*/






