package normalcoding;
import java.util.Arrays;
import java.util.Scanner;
public class hackerrank {
    public static void main (String args[]){ 
        Scanner sc =new Scanner(System.in);
        int b=sc.nextInt();
        int m=sc.nextInt();
        int n=sc.nextInt();
        int keyboard[]=new int[m];
        int drives[]=new int[n];
        for ( int i=0;i<m;i++){ 
            keyboard[i]=sc.nextInt();
        }
        for ( int i=0;i<n;i++){
            drives[i]=sc.nextInt();
        }
        Arrays.sort(keyboard);
        Arrays.sort(drives);
        int final_keybaord=0;
        int final_drive=0;
        int sample=0;
        int r=0;
        int add=0;
        int sample_1=0;
        boolean cond=true ;
        for ( int i=keyboard.length-1;i>=0;i--){ 
            for (int j=drives.length-1;j>=0;j--){ 
                sample=keyboard[i];
                sample_1=drives[j];
                 if(sample+sample_1<=b){ 
                    final_drive=sample_1;
                    final_keybaord=sample;
                    if (sample>=final_keybaord && sample_1>=final_drive){
                        add=sample+sample_1;
                        if (add>r){ 
                            r=add;
                        }
                                            }
                 }
                 else{ 
                     continue;
                 }

                }
            }
            if (r>0){ 
            System.out.println(r);
            cond=false;
            }
            if (cond){ 
                System.out.println("-1");
            }
       sc.close();
        }

    }

