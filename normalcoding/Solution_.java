package normalcoding;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.*;
class Solution_{ 
    public static void main (String args []){ 
        Scanner sc=new Scanner(System.in);
        String to_be_searched=sc.nextLine();
        String from_being_searched=sc.nextLine();
        Pattern p=Pattern.compile(to_be_searched,Pattern.CASE_INSENSITIVE);
        Matcher m=p.matcher(from_being_searched);
        boolean found =m.find();
        if (found){ 
            System.out.println(" searched ..... found ");
        }else{
            System.out.println(" sorry ");
        }
  sc.close();
    }
    }