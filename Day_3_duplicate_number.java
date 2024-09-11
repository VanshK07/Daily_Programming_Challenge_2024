import java.util.*;
public class FindDuplicateNumber {
    public static int findDuplicate(int[] arr) {
        int tortoise = arr[0];
        int hare = arr[0];
        do {
            tortoise = arr[tortoise];
            hare = arr[arr[hare]];
        } while (tortoise != hare);
        tortoise = arr[0];
        while (tortoise != hare) {
            tortoise = arr[tortoise];
            hare = arr[hare];
        }
        return hare;
    }

    public static void main(String[] args) {
        int[] arr = {1, 3, 4, 2, 2};
        System.out.println("The duplicate number is: " + findDuplicate(arr));
    }
}
