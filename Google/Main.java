public
package org.example;

import java.util.*;

//Background-
//SE2 at a not so famous SaaS Unicorn Startup(HQ at SF,USA), working in India , ~3 YOE, Tier 1 College(non Cs/It but Circuit Branch)
//
//Applied on the careers page without referal and was surprised to get the call for Interview.
//I took 2 weeks time to appear for the interview, didnt try to negotiate as well .. She offered 2 weeks and I took it(dumb move I know but I wanted the experience)
//
//The first round was the phonescreen round, 45 mins, including the inital intro and the QnA at the end of interview.. So basically around 35 mins only I got to tackle the problem at best
//
//Question-
//
//You have to design 2 functions-
//        1. That takes a new range as input
//2. Which takes a number as parameter and returns true/false depending upon whether the number is present in the range or not
//
//For example-
//Starting the range is empty ->[]
//Input Range - [2,4]
//Updated Total range [[2,4]]
//Input Range- [5,7]
//Updated Total Range [[2,4],[5,7]]
//Query(1)-> false as 1 is not present in the range..
//Input Range -> [1,9] ..
//Updated Total Range [[1,9]]
//Query(1)-> True as 1 is now present in the range..
//I was not able to come with the most optimal solution thus endend up giving and writing the code for the O(N) solution with merging range in sorted order and linearly searching if number is present..
//
//Which I know wasn't optimal.. Some tree like structure can be used to solve it in O(logN) time..
//
//So, please can someone give a solution for the same..

public  class Main {

    static TreeMap<Integer , Integer> tMap = new TreeMap<>();
    public static void main (String[] args){

        addRange(2, 3);
        addRange(6,7);
        addRange(3 , 7);
        System.out.println(query(2));

    }

    public static void addRange(int start , int end)
    {
        var L = tMap.floorEntry(start);
        var R = tMap.floorEntry(end);

        if(L != null && L.getValue() >= start){
            start = L.getKey();
        }
        if(R != null && R.getValue() > end){
            end =  R.getValue();
        }

        tMap.subMap(start , end).clear();
        tMap.put(start , end);
    }

    public static boolean query(int value){
        var val = tMap.floorEntry(value);
        if (val != null && value <= val.getValue()){
            return true;
        }

        return  false;
    }




}{

}
