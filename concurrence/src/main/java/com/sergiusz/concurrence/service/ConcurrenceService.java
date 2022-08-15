package com.sergiusz.concurrence.service;

public class ConcurrenceService {

    public Integer getPrimeNumbers(Integer start, Integer end){

        Integer sumPrime = 0;
        for(int i = start; i <= end; i++) {
                if(isPrime(i))
                    sumPrime += 1;
        }

        return sumPrime;
    }

    private boolean isPrime(int num) {
        if (num <= 1)
            return false;
        for (int i = 2; i < num; i++)
            if (num % i == 0)
                return false;
        return true;
    }
}
