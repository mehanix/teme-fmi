package com.company.entitati;

import com.company.entitati.Produs;
import com.company.servicii.CategorieService;

import java.util.HashMap;
import java.util.Map;

public class Tranzactie {

    private Map<Integer, Integer> produseCumparate;
    private Integer total = 0;
    private CategorieService categorieService = CategorieService.getInstance();

    public Tranzactie() {
        this.produseCumparate = new HashMap<Integer, Integer>();
    }

    public Map<Integer, Integer> getProduseCumparate() {
        return produseCumparate;
    }

    public void adaugaPeBon(int idP, int c) {
        produseCumparate.put(idP,c);
    }

    public int afiseazaBon() {

        System.out.println("=======================");
        System.out.println("=         Bon         =");
        System.out.println("=======================");
        for (Map.Entry<Integer,Integer> entry: produseCumparate.entrySet()) {
            Produs produs = categorieService.findProdus(entry.getKey());
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
        for (Map.Entry<Integer,Integer> entry: produseCumparate.entrySet()) {
            total += entry.getValue() * categorieService.findProdus(entry.getKey()).getPret();
        }
    }
}
