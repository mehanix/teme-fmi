package com.company.entitati;

import java.text.SimpleDateFormat;
import java.util.Comparator;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;

public class Livrare {
    private Distribuitor distribuitor;
    private Date data;
    private Map<Produs,Integer> produseCantitati;

    public Livrare(Distribuitor distribuitor, Date data) {
        this.distribuitor = distribuitor;
        this.data = data;
        this.produseCantitati = new HashMap<Produs,Integer>();
    }

    public Distribuitor getDistribuitor() {
        return distribuitor;
    }

    public void setDistribuitor(Distribuitor distribuitor) {
        this.distribuitor = distribuitor;
    }

    public Date getData() {
        return data;
    }

    public void setData(Date data) {
        this.data = data;
    }

    public void adaugaProdus(Produs p, int cantitate) {
        produseCantitati.put(p,cantitate);
    }

    public Map<Produs, Integer> getProduseCantitati() {
        return produseCantitati;
    }

    public void afiseaza() {
        int cost = 0;
        System.out.println("Data: " + new SimpleDateFormat("yyyy-MM-dd").format(data));
        System.out.println("Distribuitor: "+ distribuitor.getNume());
        System.out.println("Continutul livrarii: ");
        for(Map.Entry<Produs,Integer> entry :produseCantitati.entrySet()) {
            Produs produs = entry.getKey();
            int cantitate = entry.getValue();
            System.out.println(produs.getNume() + " - cantitate: " + cantitate + " - pret bucata: " + produs.getPret());
            cost = cost + cantitate * produs.getPret();
        };
        System.out.println("----------------------");
        System.out.println("Cost total: " + cost +" lei");
        System.out.println();

    }


}
