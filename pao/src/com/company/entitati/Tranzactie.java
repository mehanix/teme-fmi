package com.company.entitati;

import com.company.entitati.Produs;

import java.util.HashMap;
import java.util.Map;

public class Tranzactie {

    private Map<Produs, Integer> produseCumparate;
    private Integer total = 0;

    public Tranzactie() {
        this.produseCumparate = new HashMap<Produs, Integer>();
    }

    public Map<Produs, Integer> getProduseCumparate() {
        return produseCumparate;
    }

    public void adaugaPeBon(Produs p, int c) {
        produseCumparate.put(p,c);
    }

    public int afiseazaBon() {

        System.out.println("=======================");
        System.out.println("=         Bon         =");
        System.out.println("=======================");
        for (Map.Entry<Produs,Integer> entry: produseCumparate.entrySet()) {
            Produs produs = entry.getKey();
            int cantitate = entry.getValue();
            System.out.println(produs.getNume() + " - cantitate: " + cantitate + " - pret bucata: " + produs.getPret());
            total = total + cantitate * produs.getPret();
        }
        System.out.println("----------------------");
        System.out.println("Cost total: " + total +" lei");

        return total;
    }

    public Integer getTotal() {
        return total;
    }

    public void setTotal(Integer total) {
        total = 0;
        for (Map.Entry<Produs,Integer> entry: produseCumparate.entrySet()) {
            total += entry.getValue() * entry.getKey().getPret();
        }
    }
}
