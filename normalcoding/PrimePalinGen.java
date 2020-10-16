package normalcoding;
import java.util.*;
public class PrimePalinGen {
   int start,end ;
    PrimePalinGen(int a,int b){ 
        this.start=a;
        this.end=b;
    } 
    int isPrime(int i){ 
        for(int o=2;o<i;o++){ 
            if (i%o==0){ 
                return 0;
            }else{ 
                continue;
            }
        }
        return 1;
    }
    int isPalin(int i){ 
       int i_1=0;
       int s=0;
        while(i_1>-1){ 
        s=i_1%10;
        s=s*10;
        i_1=i_1/10;
        }
        if (i_1==i){ 
            return 1;
        }
    return 0;
    }
    void generate(){ 
        int i=start;
        int cond=0;
        int cond_1=0;
        if (i<=end){
            cond=isPrime(i);
            cond_1=isPalin(i);
            if (cond==1){ 
                if (cond_1==1){ 
                    System.out.println(i);
                }
            }
        i++;
        }
    }
    public static void main (String args[]){
        Scanner sc =new Scanner(System.in);
        int a=sc.nextInt();
        int b=sc.nextInt();
        PrimePalinGen obj=new PrimePalinGen(a, b);
        obj.generate();
        sc.close();
    }
}