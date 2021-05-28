package com.company.entitati;

public class Distribuitor {
    private int id;
    private String nume;
    private Categorie categorie;

    public Distribuitor(int id, String nume, Categorie categorie) {
        this.id = id;
        this.nume = nume;
        this.categorie = categorie;
    }

    public String getNume() {
        return nume;
    }

    public void setNume(String nume) {
        this.nume = nume;
    }

    public Categorie getCategorie() {
        return categorie;
    }

    public void setCategorie(Categorie categorie) {
        this.categorie = categorie;
    }


    public int getId() {
        return this.id;
    }
}
