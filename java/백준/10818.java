import java.util.Scanner;
import java.util.Arrays;

interface Main {
    public static void main (String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int arr[] = new int[N];

		for (int i = 0; i < N; i++) {
			arr[i] = scan.nextInt();
		}
        
        scan.close();
        
 		Arrays.sort(arr);
        System.out.print(arr[0] + " " + arr[N - 1]);
    }
}