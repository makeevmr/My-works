package SumOfNumbers;

import java.util.Scanner;

public class SumOfNumbers {
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        System.out.print("Введите строку: ");
        String str = scan.nextLine();
        int sum = 0;
        for (int i = 0; i <= str.length() - 1; i++){
            if ((str.charAt(i) >= 48) & (str.charAt(i) <= 57)) {
                sum += (int)(str.charAt(i)) - 48;
            }
        }
        System.out.println(sum);
    }
}
