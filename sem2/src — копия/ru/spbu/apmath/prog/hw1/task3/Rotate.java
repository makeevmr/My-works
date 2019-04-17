package ru.spbu.apmath.prog.hw1.task3;

import java.util.ArrayList;
import java.util.List;

public class Rotate {
    public static List<Integer> rotate(List<Integer> list) {
        List<Integer> rotatelist = new ArrayList<>();
        int length = list.size();
        if(length==0){
            return rotatelist;
        }else{
            for (int i = length - 1; i <= length - 1; i++) {
                rotatelist.add(list.get(i));
            }
            for (int i = 0; i < length - 1; i++) {
                rotatelist.add(list.get(i));
            }
            return rotatelist;
        }
    }
}