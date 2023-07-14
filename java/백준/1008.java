import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        
        Double A = scan.nextDouble();
        Double B = scan.nextDouble();
        
        System.out.println(A/B);
        
        scan.close();
    }
}
