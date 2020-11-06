/*
---------------------------------------------------------------------------------------------------------
code maintained by - @Aadit017
for any kind of changes , please make a pull requests with comments clearly stateing what they are doing 
--------------------------------------------------------------------------------------------------------- 
*/
import java.util.*;
class cipher{ 
    // {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
    // just for reference 
    public static void input(){ 
        Scanner sc=new Scanner(System.in);
        // input from the user 
        System.out.println("enter shift key");
        int key=sc.nextInt();// shift key 
        System.out.println("enter the text");
        String text=sc.next();// text 
        text=text.toUpperCase();
        System.out.println("encrypt or decrypt:'e' or 'd'");// if you want the text color to be changed add this 'ConsoleColors.GREEN+'
         /*  ----------------------------> */   // for the ConsoleClass fork this repo. https://github.com/Aadit017/workspace/blob/master/consolecolor.java
        char ch=sc.next().charAt(0);
        switch (ch){ 
            case 'e':  encryt(key,text);
                        break ;
            case 'd':  decrypt(key, text);
                        break;
            default: System.out.println(" 'e' or 'd' " );
    }
    } 


    public static void encryt(int key,String text){ 
        // encrypt 
        // convert a plain text into a *form 
        StringBuffer total=new StringBuffer();
        int n=0;
        char ch=' ';
        for( int i=0;i<text.length();i++){ 
            n=(int)(text.charAt(i))+key;
            if(n>90){
                n=(n-90)+64;
            }
            ch=(char)(n);
            total.append(ch);
        }
    
    System.out.println("your password"+" "+total);
    again();
    }
    public static void decrypt(int key,String text){ 
    // converting the password into normal text 
    StringBuffer total=new StringBuffer();
    int n=0;
    char ch=' ';
    for( int i=0;i<text.length();i++){ 
        n=((int)text.charAt(i)-key);
        if(n<65){ 
            n=n+90-65+1;
        }
    ch=(char)(n);
    total.append(ch);

    }
System.out.println("decrypt"+" "+total);   
again();
}
    public static void again(){ 
        //asking to run the program again 
        Scanner sc=new Scanner(System.in);
        System.out.println("wanna run again ?,'y':'n'");
        if(sc.next().charAt(0)=='y'){ 
            input();
        }else{ 
            System.out.println("01100111 01101111 01101111 01100100 00100000 01100010 01111001 01100101 ");
        }
       
    
 }
        public static void main(String args[]){ 
            // drivers code 
            input();
        }


}
