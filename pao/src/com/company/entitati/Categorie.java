package com.company.entitati;

import java.util.ArrayList;
import java.util.List;

public class Categorie {
    private Integer id;
    private String nume;
    private List<Produs> produse;

    public Categorie(String nume) {
        this.nume = nume;
        this.produse = new ArrayList<Produs>();
    }

    public Categorie(int id, String nume) {
        this.id = id;
        this.nume = nume;
        this.produse = new ArrayList<Produs>();
    }
    public String getNume() {
        return nume;
    }

    public void setNume(String nume) {
        this.nume = nume;
    }

    public List<Produs> getProduse() {
        return produse;
    }

    public void afiseaza() {
        System.out.print(nume + ": [ ");
        for (Produs p : produse) {
            System.out.print("(" + p.getId() + "):" + p.getNume() + " " );
        }
        System.out.println(" ]");
    }

    public Produs getProdus(int idProdus) {
        return produse.stream().filter(p -> p.getId().equals(idProdus)).findFirst().orElse(null);
    }
    public void adaugaProdus(Produs p) {
        this.produse.add(p);
    }

    public Integer getId() {
        return id;
    }
}
