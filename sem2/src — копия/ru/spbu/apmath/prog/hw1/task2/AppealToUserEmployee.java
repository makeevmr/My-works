package ru.spbu.apmath.prog.hw1.task2;

import java.util.Scanner;

public class AppealToUserEmployee {
    public static void main(String[] args){
        String name;
        double salary;
        int hours;
        Scanner scan = new Scanner(System.in);
        try{
            System.out.println("Введите количество сотрудников: ");
            int workers = scan.nextInt();
            Employee[] worker = new Employee[workers];
            for (int i = 0; i < workers; i++){
                System.out.println(("ФИО:"));
                scan.nextLine();
                name = scan.nextLine();
                System.out.println("Ставка в час:");
                salary = scan.nextDouble();
                System.out.println("Количество часов:");
                hours = scan.nextInt();
                worker[i] = new Employee(name, salary, hours);
            }
            for (int i = 0; i< workers; i++){
                System.out.println(worker[i].toString());
            }
        }catch(java.util.InputMismatchException e){
        System.out.println("Количество сотрудников целое число, ФИО - строка, количество часов - целое число, ставка в час - дробное число");
        }catch(java.lang.IllegalArgumentException e){
            System.out.println("Были введены отрицательные параметры");
        }
    }
}