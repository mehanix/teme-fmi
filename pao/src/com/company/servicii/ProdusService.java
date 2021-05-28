package com.company.servicii;

import com.company.entitati.Categorie;
import com.company.entitati.Produs;
import com.company.entitati.ProdusNeperisabil;
import com.company.entitati.ProdusPerisabil;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

import static com.company.servicii.Environment.conn;


public class ProdusService {
    private static ProdusService instanta = null;

    // constructor privat
    private ProdusService() {


    }

    public static ProdusService getInstance() {
        if (instanta == null)
            instanta = new ProdusService();
        return instanta;
    }

    public void creeazaProdus(Categorie cat, Scanner in) {
        try {
            in.nextLine();
            System.out.println("Denumirea produsului:");
            String nume = in.nextLine();

            System.out.println("Pretul produsului:");
            Integer pret = in.nextInt();

            System.out.println("Ce fel de produs este?");
            System.out.println("1. Perisabil");
            System.out.println("2. Neperisabil");
            int res = in.nextInt();

            int val;
            if (res == 1) {
                System.out.println("Introdu durata de valabilitate a produsului: (in luni)");
                val = in.nextInt();
                insertDb(nume, pret, cat.getId(), "perisabil", null, val);
            } else if (res == 2) {
                System.out.println("Introdu lungimea perioadei de garantie a produsului: (in ani)");
                val = in.nextInt();
                insertDb(nume, pret, cat.getId(), "neperisabil", val, null);
            }
        } catch (Exception e) {
            System.err.println("Input gresit :(");
        }
    }

    public Produs getProdus(int id) {
        try {
            Statement stmt = conn.createStatement();
            ResultSet res = stmt.executeQuery(String.format("select * from Produs where id=%d", id));
            String nume = res.getString("nume");
            Integer pret =res.getInt("pret");
            String tipProdus = res.getString("tipProdus");
            Integer aniGarantie = tipProdus.equals("neperisabil") ? res.getInt("aniGarantie") : null;
            Integer luniValabilitate = tipProdus.equals("perisabil") ? res.getInt("luniValabilitate") : null;


            if (tipProdus == "neperisabil")
                return new ProdusNeperisabil(id,nume,pret,aniGarantie);
            return new ProdusPerisabil(id,nume,pret,luniValabilitate);
        } catch (Exception e) {
            System.err.println("Problema la BD");
        }
        return null;
    }
    // CRUD DB

    // Create
    public boolean insertDb(String nume, Integer pret, Integer idCategorie, String tipProdus, Integer aniGarantie, Integer luniValabilitate) {

        try {
            String query = String.format("insert into Produs values (null,'%s','%d','%d','%s',%d,%d);", nume, pret, idCategorie, tipProdus, aniGarantie, luniValabilitate);
            System.out.println(query);
            Statement stmt = conn.createStatement();
            stmt.executeUpdate(query);
            System.out.println("Successsss!");
            return true;

        } catch (Exception e) {
            System.err.println("Eroare insert db!");
            return false;
        }
    }
//    // Create
//    public boolean insertDb(Produs p,Categorie cat) {
//        String nume = p.getNume();
//        Integer pret = p.getPret();
//        String tipProdus = p instanceof ProdusPerisabil ? "perisabil" : "neperisabil";
//        Integer aniGarantie = p instanceof ProdusNeperisabil ? ((ProdusNeperisabil) p).getAniGarantie() : null;
//        Integer luniValabilitate = p instanceof ProdusPerisabil ? ((ProdusPerisabil) p).getValabilitate() : null;
//
//        try {
//            String query = String.format("insert into Produs values (null,'%s','%d','%d','%s',%d,%d);", nume, pret, cat.getId(), tipProdus, aniGarantie, luniValabilitate);
//            System.out.println(query);
//            stmt.executeUpdate(query);
//            System.out.println("Succes!");
//            return true;
//
//        } catch (Exception e) {
//            System.err.println("Eroare insert db!");
//            return false;
//        }
//    }
//    // Read: toata lista
//    public Boolean loadFromDb() {
//        .clear();
//        try {
//            ResultSet res = stmt.executeQuery("select * from Categorie");
//            while (res.next()) {
//                loadCategorie(res.getInt("id"), res.getString("nume"));
//            }
//            return true;
//
//        } catch (Exception e) {
//            return false;
//        }
//    }

    // Update: Modifica o categorie
    public boolean update(int id, String nume) {
        return false;
    }

    // Delete
    public boolean delete(int id) {
        return false;
    }

    public void loadFromDb() {
    }
}
