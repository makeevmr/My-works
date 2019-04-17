package ru.spbu.apmath.prog.hw1.task1;

public class TranslationToBinary {
    public int value;

    public TranslationToBinary(int value){
        this.value = value;
    }

    public String toBinary() {
        StringBuilder outputvalue = new StringBuilder();
        int changevalue = this.value;
        if(changevalue < 0){
            throw new IllegalArgumentException("Введите неотрицательное значение");
        }
        if(changevalue == 0){
            return "0";
        }
        while (changevalue > 1) {
            if (changevalue % 2 == 1)
                outputvalue.insert(0,"1");
            else{
                outputvalue.insert(0,"0");
            }
            changevalue = changevalue/2;
        }
        if(changevalue == 1){
            outputvalue.insert(0,"1");
        }
        return outputvalue.toString();
    }
}