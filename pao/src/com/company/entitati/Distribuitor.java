package com.company.entitati;

public class Distribuitor {
    private String nume;
    private Categorie categorie;

    public Distribuitor(String nume, Categorie categorie) {
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
}
