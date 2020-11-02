package java_code;
class series_1{ 
    public static void main(String args[]){
        int n =3;
        int fact=1;
        double sum=0.0;
        double flag=0.0;
        for( int i=1;i<=n;i++){ 
            fact=factorial(i);
            flag=(double)1/fact;
            sum=sum+flag ;
            System.out.println(sum);
        }
    }
    public static int factorial(int i){ 
        int fact=1;
        for( int o=1;o<=i;o++){ 
            fact=fact*o;
        }
    return fact;
    }
}