import java.util.Scanner;

interface Main {
    public static void main (String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int[] arr = new int[201];

        for(int i=0; i<N; i++) {
            arr[scan.nextInt()+100]++;
        }
        int v = scan.nextInt();

        System.out.println(arr[v+100]);
    }
}