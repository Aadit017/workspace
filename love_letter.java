// nothing works in coding 
/*package java_code;
import java.util.*;
public class love_letter{ 
    public static void main(String args[]){ 
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        String arr[]=new String[n];
        for(int i=0;i<n;i++){ 
            arr[i]=sc.next();
        }
        int count=0;
           for (String word:arr){ 
               count=check_function(word);
               System.out.println(count);
           }
       }
    }
        static int check_function(String word){ 
            char arr[]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};

            String word_1="";
            int index=0;
            int index_1=0;
            char flag;
            String word_2="";
            for ( int i=word.length()-1;i>=0;i--){ // have to come out of here
                word_1+=word.charAt(i);
            }
            if (word.equals(word_1)){
            return 0;
        }else{ 
            if (word.length()%2==0){ 
                for(int i=word.length()-1;i>=0;i--){
                    if (word.charAt(i)!='a'){
                    if (word.charAt(i)!==word.charAt(index)){ 
                        flag=word.charAt(i);
                        for(int p=0;p<26;p++){ 
                            if (flag==arr[p]){ 
                                    flag=arr[p-1];
                            }
                        }
                    }
                    for( int l=0;l<word.length();l++){
                        if (l==i){
                        word_2+=flag;
                }else{ 
                    word_2+=word.charAt(l);
                }
            }else{ 

            }
        }
    }
}
}
*/