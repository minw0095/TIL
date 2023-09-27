import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        
        long A = scan.nextLong();
        long B = scan.nextLong();
        long C = scan.nextLong();
        
        scan.close();
        
        System.out.print(A+B+C);
        
    }
}