/*
import java.util.*; 
public class Solution{ 
    public static void main(String args[]){ 
        Scanner sc=new Scanner(System.in);
        List<Integer> list=new ArrayList<Integer>();
        Map<Integer,Integer> map=new HashMap<Integer,Integer>();
       int n=sc.nextInt();
       int arr[]=new int[n];
       for( int i=0;i<n;i++){ 
           arr[i]=sc.nextInt();
       }
      for( int i:arr){ 
          list.add(i);
      }
      int res=0;
        List<Integer> list_1=new ArrayList<Integer>();
        for(int i:list){
            res=Collections.frequency(list,i);
            list_1.add(res);
        } 
              int max=Collections.max(list_1);
            System.out.println(n-max);
            sc.close();
            }
} 

*/