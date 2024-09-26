import java.util.Scanner;

public class DivisorCounter {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int number = scanner.nextInt();
        
        int divisorCount = countDivisors(number);
        
        System.out.println("The number of divisors of " + number + " is: " + divisorCount);
    }
    public static int countDivisors(int num) {
        int count = 0;

        for (int i = 1; i * i <= num; i++) {
            if (num % i == 0) {
                if (i == num / i) {
                    count++;
                } else {
                    count += 2;
                }
            }
        }

        return count;
    }
}
