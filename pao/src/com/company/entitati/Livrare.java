package com.company.entitati;

import com.company.servicii.CategorieService;
import com.company.servicii.DistribuitorService;

import java.text.SimpleDateFormat;
import java.util.Comparator;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;

public class Livrare {
    private int id;
    private int idDistribuitor;
    private Date data;
    private Map<Integer,Integer> produseCantitati;
    private CategorieService categorieService = CategorieService.getInstance();
    private DistribuitorService distribuitorService = DistribuitorService.getInstance();

    public Livrare(int id, int idDistribuitor, Date data) {
        this.id = id;
        this.idDistribuitor = idDistribuitor;
        this.data = data;
        this.produseCantitati = new HashMap<Integer,Integer>();
    }

    public int getIdDistribuitor() { return idDistribuitor;}
    public Distribuitor getDistribuitor() {
        return distribuitorService.getDistribuitor(this.idDistribuitor);
    }

    public Date getData() {
        return data;
    }

    public void setData(Date data) {
        this.data = data;
    }

    public void adaugaProdus(int idProdus, int cantitate) {
        produseCantitati.put(idProdus,cantitate);
    }

    public Map<Integer, Integer> getProduseCantitati() {
        return produseCantitati;
    }

    public void afiseaza() {
        int cost = 0;
        System.out.println("Data: " + new SimpleDateFormat("yyyy-MM-dd").format(data));
        System.out.println("Distribuitor: "+ getDistribuitor().getNume());
        System.out.println("Continutul livrarii: ");
        for(Map.Entry<Integer,Integer> entry :produseCantitati.entrySet()) {
            Produs produs = categorieService.findProdus(entry.getKey());
            int cantitate = entry.getValue();
            System.out.println(produs.getNume() + " - cantitate: " + cantitate + " - pret per bucata: " + produs.getPret());
            cost = cost + cantitate * produs.getPret();
        };
        System.out.println("----------------------");
        System.out.println("Cost total: " + cost +" lei");
        System.out.println();

    }


    public int getId() {
        return id;
    }

    public void setId(long id) {
        this.id = (int)id;
    }
}
