import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int T = scan.nextInt();
        int a = 0;
        
        for(int i=1;i<T+1;i++){
            a = a+i;
   
        }
        System.out.println(a);
    }
}