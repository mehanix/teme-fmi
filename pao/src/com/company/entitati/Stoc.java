package com.company.entitati;

import com.company.entitati.Produs;

import java.util.*;

public class Stoc {
    private Set<Livrare> istoricLivrari;
    private Map<Produs,Integer> stoc;
    static private Integer incasari = 0;


    Comparator<Livrare> sortByDate = new Comparator<Livrare>() {
        @Override
        public int compare(Livrare l1, Livrare l2) {
            return l1.getData().compareTo(l2.getData());
        }
    };
    /*
    * Stoc: Include date despre stocul magazinului.
    *       Pentru a se suplimenta stocul se fac livrari.
    *       Fiecare livrare noua este inregistrata in array-ul istoricLivrari.
    *       Stocul scade atunci cand se fac tranzactii.
    *
    * */
    public Stoc() {

        this.stoc = new HashMap<Produs, Integer>();
        this.istoricLivrari = new TreeSet<Livrare>(sortByDate);
    }

    public Map<Produs, Integer> getStoc() {
        return stoc;
    }

    // adaug livrarea in istoric si actualizez stocul, adaugand produsele nou venite
    public void adaugaLivrare(Livrare l) {
        istoricLivrari.add(l);
        l.getProduseCantitati().forEach((produs, cantitate) -> {
            int old = stoc.containsKey(produs) ? stoc.get(produs) : 0;
           stoc.put(produs, old+cantitate);
        });
    }

    public void afiseaza() {
        System.out.println("===========================");
        System.out.println("=     Produse pe stoc     =");
        System.out.println("===========================");

        stoc.forEach((produs, cantitate) -> {
            if(cantitate > 0)
                System.out.println("[" + produs.getId() + "] " + produs.getNume() + ": " + cantitate);
        });

        System.out.println("---------------------------");
        System.out.println("Incasari totale: " + incasari + " lei");

    }

    public void afiseazaIstoric() {

        if (istoricLivrari.isEmpty())
        {
            System.out.println("Nu exista livrari!");
            return;
        }
        System.out.println("===========================");
        System.out.println("=     Istoric livrari     =");
        System.out.println("===========================");

        for (Livrare l : istoricLivrari) {
            l.afiseaza();

        }
    }

    public int get(Produs p) {
        return stoc.get(p);
    }

    public void efectueaza(Tranzactie t) {
        incasari += t.getTotal();

        for (Map.Entry<Produs, Integer> entry : t.getProduseCumparate().entrySet()) {
            Produs p = entry.getKey();
            Integer c = entry.getValue();
            stoc.put(p,stoc.get(p) - c);
        }
    }

}