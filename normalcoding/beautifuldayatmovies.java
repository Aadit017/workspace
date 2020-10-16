package normalcoding;

import java.util.Scanner;

public class beautifuldayatmovies {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        long i = sc.nextInt();
        long j = sc.nextInt();
        long k = sc.nextInt();
        int check;
        int counter = 0;
        for (long o = i; o <= j; o++) {
            check = if_divisible(o, k);
            if (check != 0) {
                counter++;
            }else{ 
                continue;
            }
        }
    System.out.println(counter);
    
    }

    static int if_divisible(long o, long  k) {
        long reverse = chech_reverse(o);
        long difference = o - reverse;
        if (difference % k == 0) {
            return 1;
        }
        return 0;

    }

    static long chech_reverse(long o) {
        long returned = 0;
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