package rth;
import java.util.*;
public class Solution {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println(" please enter 2 numbers ");
        int n1 = sc.nextInt();
        int n2 = sc.nextInt();
        int lcm = 0;
        lcm:
         for (int i = 2; i <= n2 * n1; i++)// lcm {
            if (i % n1 == 0) {
                if (i % n2 == 0) {
                    lcm = i;
                    break lcm;
                }
            }
        int gcd = 0;
        gcd:
        for (int i = 2; i <= n1 * n2; i++) {
            if (n1 % i == 0) {
                if (n2 % i == 0) {
                    gcd = i;
                    break gcd;
                }
            }
        }
        System.out.println(" the lcm " + lcm + " the greatest common divisor " + gcd);
    sc.close();
    }

}