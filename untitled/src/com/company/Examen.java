package com.company;


import java.io.File;
import java.io.FileNotFoundException;
import java.util.NoSuchElementException;
import java.util.Scanner;

public class Examen {
    public static void main(String[] args) throws FileNotFoundException {
        for (int i = 1; i <= 5; i++)
            try (Scanner sc = new Scanner(new File("file" + i + ".txt"))) {
                System.out.print(sc.nextInt());
            } catch (FileNotFoundException e) {
                System.out.print("!");
                throw e;
            } catch (NoSuchElementException e) {
                System.out.print("?");
            } finally {
                System.out.print("F");
            }
    }
}