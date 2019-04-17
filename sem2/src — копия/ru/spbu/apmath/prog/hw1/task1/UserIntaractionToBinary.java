package ru.spbu.apmath.prog.hw1.task1;

import java.util.Scanner;

public class UserIntaractionToBinary{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.print("Введите число для перевода в двоичную систему счисления:");
        try {
            int entered = scan.nextInt();
            TranslationToBinary t = new TranslationToBinary(entered);
            System.out.println(t.toBinary());
        }catch (java.util.InputMismatchException e){
            System.out.println("Введите целое число");
        }catch (java.lang.IllegalArgumentException e){
            System.out.println("Введите неотрицательное значение");

        }

    }

}