package com.company.servicii;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class FileReaderService {
    private static FileReaderService instanta = null;

    // constructor privat
    private FileReaderService() {

    }

    public static FileReaderService getInstance() {
        if (instanta == null)
            instanta = new FileReaderService();
        return instanta;
    }

    /**
     * Citeste si formateaza csv-uri.
     * @param path: path catre csv.
     * @return lista de liste, datele efectiv din csv, fara virgule
     * */
    public ArrayList<ArrayList<String>> read(String path) {

        ArrayList<ArrayList<String>> content = new ArrayList<ArrayList<String>>();

        try {
            File input = new File(path);
            Scanner s = new Scanner(input);
            while (s.hasNextLine()) {

                String line = s.nextLine().strip();
                String[] spl = line.split(",");
                ArrayList<String> bucati = new ArrayList<String>(Arrays.asList(spl));

                content.add(bucati);
            }
            return content;
        } catch (FileNotFoundException e) {
            System.out.println("Fisier inexistent: " + path);
        }
        return null;
    }
}
