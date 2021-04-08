package com.company.entitati;

import com.company.entitati.Produs;

import java.util.HashMap;
import java.util.Map;

public class Tranzactie {

    private Map<Produs, Integer> produseCumparate;

    public Tranzactie() {
        this.produseCumparate = new HashMap<Produs, Integer>();
    }

    public Map<Produs, Integer> getProduseCumparate() {
        return produseCumparate;
    }

}
