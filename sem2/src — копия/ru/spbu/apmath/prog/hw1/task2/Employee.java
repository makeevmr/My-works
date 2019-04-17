package ru.spbu.apmath.prog.hw1.task2;

public class Employee {
    private String name;
    private double salary;
    private int hours;

    public Employee(String name, double salary,int hours) {
        if (salary < 0  || hours< 0){
            throw new IllegalArgumentException("Были введены отрицательные параметры");
        }
        this.name = name;
        this.salary = salary;
        this.hours = hours;
    }
    private double getSalary(){
        double allsalary;
        if (this.hours > 60 || this.salary < 70 ){
            throw new IllegalStateException("ОШИБКА");
        }else if (this.hours <= 40){
            allsalary = this.hours*this.salary;
        }else{
            allsalary = 40*this.salary + (this.hours-40)*1.5*this.salary;
        }
        return allsalary;
    }
    @Override
    public String toString(){
        try{
            return (this.name + " " + this.salary + " " + this.hours + " " + this.getSalary());
        }catch(IllegalStateException e){
            return (this.name + " " + this.salary + " " + this.hours + " " + e.getMessage());
        }
    }
}
