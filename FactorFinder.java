package com.company;
import java.util.Scanner;
import java.lang.Math;

public class Main {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        int numFactors = 1;

        // Input
        System.out.println("\nEnter a positive whole number that you would like to find the factors of: (Warning: Gets crazy at like the 10^16 range)");
        double N = scan.nextDouble();

        //BS checker/program exitor
        if(N == 1) {
            System.out.println("\n1.");
        }
        else if(N == 0){
            System.out.println("\nThis number's factors are every number and itself.");
        }
        else if(N % 2 != 0 && N % 2 != 1 && N%2 != -1 && N < 0) {
            System.out.println("\nBruh are you trying to break like. EVERY SINGLE DIRECTION I JUST GAVE YOU");
        }
        else if(N % 2 != 0 && N % 2 != 1 && N%2 != -1) {
            System.out.println("\nBruh does that LOOK whole to you!?!");
        }
        else if(N < 0){
            System.out.println("Bruh that isn't positive");
        }
        else if (N < 4) {
            System.out.println("This number is prime, so its only factors are " + N + " and 1.");
        }

        else {

            // "root" is used as an upper limit for checking factors, to prevent duplicates of pairs.
            double root = Math.sqrt(N);

            System.out.println("\nThe factors of " + N + " are:\n");
            System.out.println("1.0 and " + N); //It's this for everything so just stuff it in the start

            //If the number divided by two has a remainder of 0 or 1, (aka is it whole) it gets printed with its pair.
            for (double i = 2.0; i <= root; i++) {
                double Q1 = N/i;
                if ((Q1 % 2 == 0 || Q1 % 2 == 1) && (Q1-i) > -1) {
                    System.out.println(i + " and " + Q1);
                    numFactors++;
                }
            }

            // If it only has one factor pair
            if (numFactors == 1) {
                System.out.println("\nThis number, " + N + ", is prime. Its only factors are 1 and itself.");
            }
            else {
                System.out.println("\nThis number has "+numFactors+" unique pairs of factors.");
            }
        }


    }
}