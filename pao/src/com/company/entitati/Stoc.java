package com.company.entitati;

import com.company.entitati.Produs;
import com.company.servicii.CategorieService;

import java.util.*;

public class Stoc {
    private Set<Livrare> istoricLivrari;
    private Map<Integer,Integer> stoc;
    static private Integer incasari = 0;
    private CategorieService categorieService = CategorieService.getInstance();


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

        this.stoc = new HashMap<Integer, Integer>();
        this.istoricLivrari = new TreeSet<Livrare>(sortByDate);
    }

    public Map<Integer, Integer> getStoc() {
        return stoc;
    }

    // adaug livrarea in istoric si actualizez stocul, adaugand produsele nou venite
    public void adaugaLivrare(Livrare l) {
        istoricLivrari.add(l);
        l.getProduseCantitati().forEach((produs, cantitate) -> {
            int old = stoc.getOrDefault(produs, 0);
           stoc.put(produs, old+cantitate);
        });
    }

    public void afiseaza() {
        System.out.println("===========================");
        System.out.println("=     Produse pe stoc     =");
        System.out.println("===========================");

        stoc.forEach((idProdus, cantitate) -> {
            if(cantitate > 0) {
                Produs produs = categorieService.findProdus(idProdus);
                System.out.println("[" + produs.getId() + "] " + produs.getNume() + ": " + cantitate);
            }
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

    public int get(int idP) {
        return stoc.get(idP);
    }

    public void efectueaza(Tranzactie t) {
        incasari += t.getTotal();

        for (Map.Entry<Integer, Integer> entry : t.getProduseCumparate().entrySet()) {
            Integer idP = entry.getKey();
            Integer c = entry.getValue();
            stoc.put(entry.getKey(),stoc.get(idP) - c);
        }
    }

    public void clear() {
        istoricLivrari.clear();
        stoc.clear();
        incasari = 0;
    }
}
