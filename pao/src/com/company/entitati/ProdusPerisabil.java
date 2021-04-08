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

    public ProdusPerisabil(String nume, Integer pret, Integer valabilitate) {
        super(nume, pret);
        this.valabilitate = valabilitate;
    }
}
