package com.company.entitati;

public class Produs {
    static int uniqueIdCounter = 0;

    private Integer id;
    private String nume;
    private Integer pret;

    public String getNume() {
        return nume;
    }

    public void setNume(String nume) {
        this.nume = nume;
    }

    public Integer getPret() {
        return pret;
    }

    public void setPret(Integer pret) {
        this.pret = pret;
    }

    public Produs(String nume, Integer pret) {
        this.id = uniqueIdCounter++;
        this.nume = nume;
        this.pret = pret;
    }
}
