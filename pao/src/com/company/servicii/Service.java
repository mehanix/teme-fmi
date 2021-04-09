
package com.company.servicii;

import com.company.entitati.*;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;

public class Service {
    private final Stoc stoc = new Stoc();
    private final ArrayList<Categorie> categorii = new ArrayList<Categorie>();
    private final ArrayList<Distribuitor> distribuitori = new ArrayList<Distribuitor>();

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
        System.out.println("=====================");
        System.out.println("=      Categorii    =");
        System.out.println("=====================");
        for (int i = 0; i < categorii.size(); i++) {
            System.out.println(i + ": " + categorii.get(i).getNume());
        }
    }


    private void afiseazaDistribuitori() {
        System.out.println("=====================");
        System.out.println("=   Distribuitori   =");
        System.out.println("=====================");
        for (int i = 0; i < distribuitori.size(); i++) {
            Distribuitor d = distribuitori.get(i);
            System.out.println(i + ": " + d.getNume() + " -- " + d.getCategorie().getNume());

        }
    }

    //4
    public Categorie veziProduseCategorie(Scanner in) {
        afiseazaCategorii();
        System.out.println();
        Categorie c = null;
        System.out.println("Introdu numarul categoriei pentru care vrei sa vezi produsele: ");
        try {
            int res = in.nextInt();
            c = categorii.get(res);
            c.afiseaza();
        } catch (Exception e) {
            System.out.println("Ai introdus input gresit!");
        }
        return c;
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
    public void adaugaLivrare(Scanner in) throws ParseException {
        if (distribuitori.size() == 0 ) {
            System.out.println("Nu exista niciun distribuitor - nu are cine sa faca livrari");
            return;
        }

        Date data = new Date();
        afiseazaDistribuitori();
        System.out.print("Id-ul distribuitorului: ");
        int idDistribuitor = in.nextInt();
        System.out.print("Data livrarii (yyyy-mm-dd): ");
        String dataStr = in.next();
        System.out.println(dataStr);
        data = new SimpleDateFormat("yyyy-MM-dd").parse(dataStr);
        Distribuitor d = distribuitori.get(idDistribuitor);
        Livrare l = new Livrare(d,data);

        System.out.println("Acestea sunt produsele pe care le poate livra distribuitorul " + d.getNume() +": ");
        Categorie cat = d.getCategorie();
        cat.afiseaza();

        int idProdus = -1;
        int cantitate;
        do {
            try {
                System.out.print("Introdu id-ul produsului, sau -1 pentru a termina:");
                idProdus = in.nextInt();
                if (idProdus == -1)
                    break;
                Produs p = cat.getProdus(idProdus);
                System.out.print("Cate produse " + p.getNume() + " vor fi livrate? ");
                cantitate = in.nextInt();
                l.adaugaProdus(p,cantitate);
                System.out.println("Adaugat!");

            } catch(Exception e) {
                System.out.print("Input invalid!");

            }
        } while (true);

        stoc.adaugaLivrare(l);

        System.out.println("Livrare adaugata cu succes!" + l.toString());



    }

    public void veziDetaliiProdus(Scanner in) {
        Categorie catSelectata = veziProduseCategorie(in);
        int idProdus;
        Produs p;
        System.out.print("Introdu id-ul produsului care te intereseaza: ");

        try {
            idProdus = in.nextInt();
            p = catSelectata.getProdus(idProdus);
            p.afiseaza();
        } catch (Exception e) {System.out.println(e);};
    }

    public void afiseazaStoc() {
        stoc.afiseaza();
    }

    public void veziIstoricLivrari() {
        stoc.afiseazaIstoric();
    }

}
