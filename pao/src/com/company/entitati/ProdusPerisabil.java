package com.company.entitati;

import java.util.ArrayList;
import java.util.Date;

public class ProdusPerisabil extends Produs {
    private Integer valabilitate;

    public Integer getValabilitate() {
        return valabilitate;
    }

    public void setValabilitate(Integer valabilitate) {
        this.valabilitate = valabilitate;
    }

    public ProdusPerisabil(int id, String nume, Integer pret, Integer valabilitate) {
        super(id, nume, pret);
        this.valabilitate = valabilitate;
    }

    public void afiseaza() {
        super.afiseaza();

        System.out.println("Produs perisabil cu valabilitate: " + valabilitate + " luni");
    }
}

