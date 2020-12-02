package java_code;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
class basicArray{ 

    public static void main(String args[]) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        System.out.println("'ENTER'number of days in the month : -");
        int n=Integer.parseInt(br.readLine());
        int arr[]=new int[n];
        System.out.println("sales for each independent person-->");
        try{
        for(int i=0;i<n;i++){ 
            arr[i]=Integer.parseInt(br.readLine());
        }
    }
    catch(Exception e){ 
        System.out.println("ERROR! in the input task");
        System.out.println("Execution failed");
        System.exit(1);
    }
    long sum=0;
    for(int i:arr){ 
        sum+=sum+i;
    }
System.out.println("the total sum is --> "+sum);
System.out.println("the average is --> "+(sum/arr.length));    
}
}