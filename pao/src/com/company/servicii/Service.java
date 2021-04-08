package com.company.servicii;

import com.company.entitati.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Service {
    private final Stoc stoc = new Stoc();
    private final ArrayList<Categorie> categorii = new ArrayList<Categorie>();
    private final ArrayList<Distribuitor> distribuitori = new ArrayList<Distribuitor>();

    // afiseaza produsele din stoc
    public void veziStoc() {

    }

    // 1
    public void adaugaCategorie(Scanner in) {
        String nume;
        System.out.println("Introdu numele categoriei:");
        nume = in.nextLine();
        Categorie cat = new Categorie(nume);
        categorii.add(cat);

    }

    public void adaugaDistribuitor(Scanner in) {

        if (categorii.size() == 0) {
            System.out.println("Nu poti adauga distribuitori daca nu exista categorii!");
            return;
        }
        try {
        System.out.println("Introdu numele distribuitorului:");
        String nume = in.nextLine();
        afiseazaCategorii();
        System.out.println("Introdu id-ul categoriei de produse pe care distribuitorul le va furniza:");

            int id = in.nextInt();
            Distribuitor d = new Distribuitor(nume, categorii.get(id));
            distribuitori.add(d);
            System.out.println("Adaugat cu succes!");

        } catch (Exception e) {
            System.out.println("Ai introdus input gresit!");
        }
    }


    private void afiseazaCategorii() {
        System.out.println("Categorii");
        System.out.println("=====================");
        for (int i = 0; i < categorii.size(); i++) {
            System.out.println(i + ": " + categorii.get(i).getNume());
        }

    }
    //4
    public void veziProduseCategorie(Scanner in) {
        afiseazaCategorii();
        System.out.println();
        System.out.println("Introdu numarul categoriei pentru care vrei sa vezi produsele: ");
        try {
            int res = in.nextInt();
            categorii.get(res).afiseaza();
        } catch (Exception e) {
            System.out.println("Ai introdus input gresit!");
        }
    }

    public void adaugaProdus(Scanner in) {
        Categorie cat;
        String nume;
        Integer pret;
        afiseazaCategorii();
        try {
        System.out.println("Din ce categorie face parte produsul?");
        int idCategorie = in.nextInt();
        in.nextLine();
        System.out.println("Denumirea produsului:");
        nume = in.nextLine();

        System.out.println("Pretul produsului:");
        pret = in.nextInt();

        System.out.println("Ce fel de produs este?");
        System.out.println("1. Perisabil");
        System.out.println("2. Neperisabil");
        int res = in.nextInt();

        Produs p;
        if (res == 1) {
            System.out.println("Introdu durata de valabilitate a produsului: (in luni)");
            int valabilitate = in.nextInt();
             p = new ProdusPerisabil(nume,pret,valabilitate);
        } else if (res == 2) {
            System.out.println("Introdu lungimea perioadei de garantie a produsului: (in ani)");
            int garantie = in.nextInt();
            p = new ProdusPerisabil(nume,pret,garantie);
        } else { return; }

        categorii.get(idCategorie).adaugaProdus(p);


        } catch (Exception e) {
            System.out.println("Ai introdus input gresit!");
        }

    }


}
