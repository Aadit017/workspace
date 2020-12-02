package java_code;
import java.util.*;
class idk{ 
    public static void main(String args[]){ 
      //  Scanner sc=new Scanner(System.in);
        Map<String,String> map=new HashMap<String,String>();
        // hash map are similar to the python dictionary
        map.put("father","rob");
        map.put("mother","kristena");
        System.out.println(map.get("father")+" & "+map.get("mother"));
        map.remove("mother");
        System.out.println(map.toString());
} 
} 