import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        int t = scan.nextInt();
        if(t>=90) System.out.print("A");
        else if(t>=80) System.out.print("B");
        else if(t>=70) System.out.print("C");
        else if(t>=60) System.out.print("D");
        else System.out.print("F");
        
        
    }
}