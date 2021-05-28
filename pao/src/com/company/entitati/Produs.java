package com.company.entitati;

public class Produs {

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

    public Produs(int id, String nume, Integer pret) {
        this.id = id;
        this.nume = nume;
        this.pret = pret;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public void afiseaza() {
        System.out.println("=======================");
        System.out.println("= Fisa detalii produs =");
        System.out.println("=======================");
        System.out.println("Nume: " + nume);
        System.out.println("Pret: " + pret + " lei");


    }
}