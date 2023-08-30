import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int a = scanner.nextInt();

        for (int i = 0; i < a; i++) {
            String[] b = scanner.next().split("");
            System.out.print(b[0]+""+b[b.length-1]+"\n");
        }

    }
}