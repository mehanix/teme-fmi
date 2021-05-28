package com.company.servicii;

import com.company.entitati.Categorie;
import com.company.entitati.Produs;
import com.company.entitati.ProdusNeperisabil;
import com.company.entitati.ProdusPerisabil;

import java.sql.*;
import java.util.ArrayList;
import java.util.Scanner;

import static com.company.servicii.Environment.*;


public class CategorieService {
    private static CategorieService instanta = null;

    private final ArrayList<Categorie> categorii = new ArrayList<Categorie>();

    // constructor privat
    private CategorieService() {

    }

    // afiseaza lista categorii
    public Categorie selecteazaCategorie(String mesaj, Scanner in) {
        System.out.println("=====================");
        System.out.println("=      Categorii    =");
        System.out.println("=====================");
        for (Categorie c : categorii) {
            System.out.println(c.getId() + ": " + c.getNume());
        }
        System.out.println(mesaj);
        try {
            return getCategorie(in.nextInt());
        } catch (Exception e) {
            System.out.println("Ai introdus input gresit!");
            return null;
        }
    }

    public Categorie getCategorie(int id) {
        return categorii.stream().filter(c -> c.getId() == id).findFirst().orElse(null);
    }

    // creaza categorie noua
    public void creeazaCategorie(String nume) {

        insertDb(nume);
        loadFromDb();

    }

    // load din db in ram
    private void loadCategorie(int id, String nume) {

        Categorie cat = new Categorie(id, nume);
        categorii.add(cat);

    }

    public static CategorieService getInstance() {
        if (instanta == null)
            instanta = new CategorieService();
        return instanta;
    }

    // CRUD DB

    // Create
    public boolean insertDb(String nume) {
        try {
            String query = String.format("insert into Categorie values (null,'%s');", nume);
            Statement stmt = conn.createStatement();
            stmt.executeUpdate(query);

            System.out.println("Succes!");
            return true;

        } catch (Exception e) {
            System.err.println("Eroare insert db!");
            return false;
        }
    }

    public Produs findProdus(int id) {
        for (Categorie cat : categorii) {
            Produs p = cat.getProdus(id);
            if (p != null)
                return p;
        }
        return null;
    }

    // Read: toata lista
    public void loadFromDb() {
        // incarc categoriile
        categorii.clear();
        try {
            Statement stmt = conn.createStatement();
            ResultSet res = stmt.executeQuery("select * from Categorie");
            while (res.next())
                loadCategorie(res.getInt("id"), res.getString("nume"));

            //incarc produsele categoriilor din db
            stmt = conn.createStatement();
            res = stmt.executeQuery("select * from Produs");
            while (res.next()) {
                Produs p;
                int id = res.getInt("id");
                String nume = res.getString("nume");
                int pret = res.getInt("pret");
                String tip = res.getString("tipProdus");

                if (tip.equals("perisabil")){
                    int val = res.getInt("luniValabilitate");
                    p = new ProdusPerisabil(id,nume,pret,val);
                } else {
                    int val = res.getInt("aniGarantie");
                    p = new ProdusNeperisabil(id,nume,pret,val);
                }
                // adauga in ram
                adaugaProdusInCategorie(p, res.getInt("idCategorie"));
            }

        } catch (Exception e) {
        }
    }

    private void adaugaProdusInCategorie(Produs p, int idCategorie) {
        getCategorie(idCategorie).adaugaProdus(p);
    }


    public int getSize() {
        return categorii.size();
    }

    public ArrayList<Categorie> getCategorii() {
        return categorii;
    }
}

