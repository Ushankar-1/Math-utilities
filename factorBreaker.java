package com.company;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        int numFactors = 0;
        final double THRESHOLD = 0.000001;

        Scanner scan = new Scanner(System.in);

        System.out.println("Enter the positive whole number you would like broken into prime numbers:\n");
        double N = scan.nextDouble();

        if(N == 1) {
            System.out.println("\n1.");
        }
        else if(N == 0){
            System.out.println("\n0.");
        }
        else if(N % 2 != 0 && N % 2 != 0.5 && N < 0) {
            System.out.println("\nBruh are you trying to break like. EVERY SINGLE DIRECTION I JUST GAVE YOU");
        }
        else if(N < 1) {
            System.out.println("\nBruh does that LOOK positive and nonzero to you?!?");
        }

        else if(N % 2 != 0 && N % 2 != 1) {
            System.out.println("\nBruh does that LOOK whole to you!?!");
        }
        else {

            double A = N;
            double root = (Math.sqrt(N));

            if(N == 1) {
                System.out.println("\nThis number's only factor is itself.");
            }

            else {
                System.out.println("\nThis number can be broken into:\n ");

                for(double i = 2.0; i <= root; i+=1) {
                    while(A % i == 0 && A != i) {
                        System.out.println(i);
                        numFactors++;
                        A = A/i;
                        i = 2.0;
                        root = A;
                    }
                    if(Math.abs(A-i) < THRESHOLD) {
                        System.out.println(i);
                        numFactors++;
                        i = root + 1;
                    }
                }

                if(numFactors == 0) {
                    System.out.println("...");
                    System.out.println("...Nevermind, it can't be broken into anything special.");
                    System.out.println("This number, "+N+" is prime. Its only factors are 1 and itself.");
                }
                else {
                    System.out.println("\nThat's "+numFactors+" prime factors.");
                }

            }
        }

    }
}
