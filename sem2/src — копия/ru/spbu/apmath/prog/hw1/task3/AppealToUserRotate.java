package ru.spbu.apmath.prog.hw1.task3;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class AppealToUserRotate {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Введите длину списка:");
        int length = scan.nextInt();
        System.out.println("Введите значения в списке:");
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i <= length - 1; i++) {
            int value = scan.nextInt();
            list.add(value);
        }
        System.out.println(Rotate.rotate(list));
    }
}