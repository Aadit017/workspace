package normalcoding;
import java.util.*;
public class WordWise{ 
    String str;
    WordWise(){ 
        str="";
    }
     void readsent(){ 
        WordWise obj=new WordWise();
        Scanner sc=new Scanner(System.in);
        String w=sc.nextLine();
        obj.frequency_counter(w);
        sc.close();
        
    }
    int frequency_counter(String w){ 
        int counter=0;
        for (int i=0;i<w.length();i++){
            if (w.charAt(i)=='a'|| w.charAt(i)=='e'||w.charAt(i)=='i'||w.charAt(i)=='o'||w.charAt(i)=='u'){ 
                counter+=1;
            }
        }
        WordWise obj=new WordWise();
        obj.arrange(w,counter);
        return counter;
    }
    void arrange(String w, int counter){ 
       // using array because list are not in syllabus    List<String> list=new ArrayList<String>();
        String[] arrofstr=w.split(" ",0);
        for ( int i=0;i<arrofstr.length;i++){ 
            System.out.println(arrofstr[i]);
        }
    System.out.println(" vowel counter:-"+ counter);
    }
    public static void main (String args[]){ 
        WordWise obj=new WordWise();
       obj.readsent();

    }
}
