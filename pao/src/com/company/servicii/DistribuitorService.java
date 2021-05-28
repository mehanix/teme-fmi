package com.company.servicii;

import com.company.entitati.Categorie;
import com.company.entitati.Distribuitor;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Optional;
import java.util.Scanner;

import static com.company.servicii.Environment.conn;


public class DistribuitorService {
    private static DistribuitorService instanta = null;
    private final ArrayList<Distribuitor> distribuitori = new ArrayList<Distribuitor>();
    private CategorieService categorieService = CategorieService.getInstance();

    // constructor privat
    private DistribuitorService() {

    }
    public Distribuitor getDistribuitor(int id) {
        return distribuitori.stream().filter(d -> d.getId() == id).findFirst().orElse(null);
    }

    public static DistribuitorService getInstance() {
        if (instanta == null)
            instanta = new DistribuitorService();
        return instanta;
    }

    public void creeazaDistribuitor(String nume, Categorie cat) {
        insertDb(nume,cat.getId());
        loadFromDb();
    }

    // load din db in ram
    private void loadDistribuitor(int id,String nume, int idCat) {

        Distribuitor d = new Distribuitor(id, nume, categorieService.getCategorie(idCat));
        distribuitori.add(d);

    }
    public int getSize() {
        return distribuitori.size();
    }

    public void afiseazaDistribuitori() {
        System.out.println("=====================");
        System.out.println("=   Distribuitori   =");
        System.out.println("=====================");
        for (Distribuitor d:distribuitori) {
            System.out.println(d.getId() + ": " + d.getNume() + " -- " + d.getCategorie().getNume());

        }
    }
    public Distribuitor afiseazaDistribuitori(String mesaj, Scanner in) {
        System.out.println("=====================");
        System.out.println("=   Distribuitori   =");
        System.out.println("=====================");
        for (Distribuitor d:distribuitori)
            System.out.println(d.getId() + ": " + d.getNume() + " -- " + d.getCategorie().getNume());

        System.out.println(mesaj);
        try {
            return getDistribuitor(in.nextInt());
        } catch (Exception e) {
            System.out.println("Ai introdus input gresit!");
            return null;
        }
    }
    // CRUD db

    // Create
    public boolean insertDb(String nume, int idCat) {
        try {
            String query = String.format("insert into Distribuitor values (null, '%s', '%d');",nume, idCat);
            Statement stmt = conn.createStatement();
            System.out.println(query);

            stmt.executeUpdate(query);

            System.out.println("Succes!");
            return true;

        } catch (Exception e) {
            System.err.println("Eroare insert db!");
            return false;
        }
    }

    // Read: toata lista
    public Boolean loadFromDb() {
        distribuitori.clear();
        try {
            Statement stmt = conn.createStatement();
            ResultSet res = stmt.executeQuery("select * from Distribuitor");
            while (res.next()) {
                this.loadDistribuitor(res.getInt("id"), res.getString("nume"), res.getInt("idCategorie"));
            }
            return true;

        } catch (Exception e) {
            return false;
        }
    }




}
