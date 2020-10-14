package normalcoding;

import java.util.Scanner;

public class beautifuldayatmovies {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int i = sc.nextInt();
        int j = sc.nextInt();
        int k = sc.nextInt();
        int check;
        int counter = 0;
        for (int o = i; o <= j; o++) {
            check = if_divisible(o, k);
            if (check != 0) {
                counter++;
            }else{ 
                continue;
            }
        }
    System.out.println(counter);
    
    }

    static int if_divisible(int o, int k) {
        int reverse = chech_reverse(o);
        int difference = o - reverse;
        if (difference % k == 0) {
            return 1;
        }
        return 0;

    }

    static int chech_reverse(int o) {
        int returned = 0;
        boolean cond = true;
        if (cond) {
            if (o % 10 == 0) {
                o = o / 10;
            } else {
                cond = false;
            }
        }
        while (o> 0) {
            returned = (o % 10) * 10 + returned;
            o = o / 10;
        }
        return returned;
    }

}