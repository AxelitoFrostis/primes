package JavaVerison;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class JavaVersion {
    public static void main(String[] args) {
        File rawPrimes = new File("results/primedata.txt");
        try {
            Scanner scan = new Scanner(rawPrimes);
            while (scan.hasNextLine()) {
                String primesText = scan.nextLine();
            }
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        String[] primes = primesText.split(", ");
    }
}