
package com.company.servicii;

import com.company.entitati.*;

import java.io.File;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;

public class Service {
    private final Stoc stoc = new Stoc();
    private final ArrayList<Categorie> categorii = new ArrayList<Categorie>();
    private final ArrayList<Distribuitor> distribuitori = new ArrayList<Distribuitor>();
    private List<Tranzactie> tranzactii;
    private AuditService audit = AuditService.getInstance();

    // 1
    public void adaugaCategorie(Scanner in) {
        String nume;
        System.out.println("Introdu numele categoriei:");
        nume = in.nextLine();
        _creeazaCategorie(nume);
        audit.log("adauga_categorie");
    }

    private void _creeazaCategorie(String nume) {

        Categorie cat = new Categorie(nume);
        categorii.add(cat);
    }
    public void adaugaDistribuitor(Scanner in) {

        if (categorii.size() == 0) {
            System.out.println("Nu poti adauga distribuitori daca nu exista categorii!");
            return;
        }
        try {
            System.out.println("Introdu numele distribuitorului:");
            String nume = in.nextLine();
            afiseazaCategorii();
            System.out.println("Introdu id-ul categoriei de produse pe care distribuitorul le va furniza:");

            int id = in.nextInt();
            _creeazaDistribuitor(nume, id);

            System.out.println("Adaugat cu succes!");
            audit.log("adauga_distribuitor");


        } catch (Exception e) {
            System.out.println("Ai introdus input gresit!");
        }
        in.nextLine();

    }

    private void _creeazaDistribuitor(String nume, int id) {
        Distribuitor d = new Distribuitor(nume,  categorii.get(id));
        distribuitori.add(d);
    }

    private void afiseazaCategorii() {
        System.out.println("=====================");
        System.out.println("=      Categorii    =");
        System.out.println("=====================");
        for (int i = 0; i < categorii.size(); i++) {
            System.out.println(i + ": " + categorii.get(i).getNume());
        }
    }


    private void afiseazaDistribuitori() {
        System.out.println("=====================");
        System.out.println("=   Distribuitori   =");
        System.out.println("=====================");
        for (int i = 0; i < distribuitori.size(); i++) {
            Distribuitor d = distribuitori.get(i);
            System.out.println(i + ": " + d.getNume() + " -- " + d.getCategorie().getNume());

        }
    }

    //4
    public Categorie veziProduseCategorie(Scanner in) {
        if (categorii.isEmpty())
        {
            System.out.println("Nu exista categorii");
            return null;
        }
        afiseazaCategorii();
        System.out.println();
        Categorie c = null;
        System.out.println("Introdu numarul categoriei pentru care vrei sa vezi produsele: ");
        try {
            int res = in.nextInt();
            c = categorii.get(res);
            c.afiseaza();
        } catch (Exception e) {
            System.out.println("Ai introdus input gresit!");
        }
        in.nextLine();
        audit.log("afiseaza_produse_categorie");

        return c;
    }

    public void adaugaProdus(Scanner in) {
        Categorie cat;
        String nume;
        Integer pret;
        if (categorii.isEmpty())
        {
            System.out.println("Trebuie creata minim o categorie pentru a adauga produse!");
            return;
        }
        afiseazaCategorii();
        try {
            System.out.println("Din ce categorie face parte produsul?");
            int idCategorie = in.nextInt();
            in.nextLine();
            System.out.println("Denumirea produsului:");
            nume = in.nextLine();

            System.out.println("Pretul produsului:");
            pret = in.nextInt();

            System.out.println("Ce fel de produs este?");
            System.out.println("1. Perisabil");
            System.out.println("2. Neperisabil");
            int res = in.nextInt();

            Produs p;
            if (res == 1) {
                System.out.println("Introdu durata de valabilitate a produsului: (in luni)");
                int valabilitate = in.nextInt();
                p = new ProdusPerisabil(nume,pret,valabilitate);
            } else if (res == 2) {
                System.out.println("Introdu lungimea perioadei de garantie a produsului: (in ani)");
                int garantie = in.nextInt();
                p = new ProdusNeperisabil(nume,pret,garantie);
            } else { return; }

            categorii.get(idCategorie).adaugaProdus(p);
            in.nextLine();
            audit.log("adauga_produs");


        } catch (Exception e) {
            System.out.println("Ai introdus input gresit!");
        }
    }
    public void adaugaLivrare(Scanner in) throws ParseException {
        if (distribuitori.size() == 0 ) {
            System.out.println("Nu exista niciun distribuitor - nu are cine sa faca livrari");
            return;
        }

        Date data = new Date();
        afiseazaDistribuitori();
        System.out.print("Id-ul distribuitorului: ");
        int idDistribuitor = in.nextInt();
        System.out.print("Data livrarii (yyyy-mm-dd): ");
        String dataStr = in.next();
        System.out.println(dataStr);
        data = new SimpleDateFormat("yyyy-MM-dd").parse(dataStr);
        Distribuitor d = distribuitori.get(idDistribuitor);
        Livrare l = new Livrare(d,data);

        System.out.println("Acestea sunt produsele pe care le poate livra distribuitorul " + d.getNume() +": ");
        Categorie cat = d.getCategorie();
        cat.afiseaza();

        int idProdus = -1;
        int cantitate;
        do {
            try {
                System.out.print("Introdu id-ul produsului, sau -1 pentru a termina:");
                idProdus = in.nextInt();
                if (idProdus == -1)
                    break;
                Produs p = cat.getProdus(idProdus);
                System.out.print("Cate produse " + p.getNume() + " vor fi livrate? ");
                cantitate = in.nextInt();
                l.adaugaProdus(p,cantitate);
                System.out.println("Adaugat!");
                audit.log("adauga_livrare");


            } catch(Exception e) {
                System.out.print("Input invalid!");

            }
        } while (true);

        stoc.adaugaLivrare(l);

        System.out.println("Livrare adaugata cu succes!");

        in.nextLine();


    }

    public void veziDetaliiProdus(Scanner in) {
        if (categorii.isEmpty())
        {
            System.out.println("Nu exista categorii!");
            return;
        }
        Categorie catSelectata = veziProduseCategorie(in);
        int idProdus;
        Produs p;
        System.out.print("Introdu id-ul produsului care te intereseaza: ");

        try {
            idProdus = in.nextInt();
            p = catSelectata.getProdus(idProdus);
            p.afiseaza();
            audit.log("vezi_detalii_produs");

        } catch (Exception e) {System.out.println(e);};
        in.nextLine();

    }

    public void afiseazaStoc() {
        stoc.afiseaza();
        audit.log("afiseaza_stoc");

    }

    private Produs findProdus(int id) {
        for (Categorie cat : categorii) {
            Produs p = cat.getProdus(id);
            if (p != null)
                return p;
        }
        return null;
    }

    public void veziIstoricLivrari() {
        stoc.afiseazaIstoric();
        audit.log("afiseaza_istoric_livrari");

    }

    public void efectueazaTranzactie(Scanner in) {
        Tranzactie t = new Tranzactie();

        afiseazaStoc();

        int idProdus, cantitate;
        Produs p;

        try {
            do {
                System.out.print("Introdu id-ul produsului care te intereseaza, sau -1 pentru a termina: ");
                idProdus = in.nextInt();
                if (idProdus == -1) {
                    if (t.getProduseCumparate() == null)
                        return;

                    int total = t.afiseazaBon();
                    System.out.print("Confirmi tranzactia? y/n: ");
                    String res = in.next();
                    if(res.equals("y"))
                    {
                        stoc.efectueaza(t);
                        System.out.println("Tranzactie efectuata cu succes!");
                        audit.log("efectueaza_tranzactie");

                        return;
                    }
                    System.out.println("Tranzactie anulata!");
                    return;
                }
                p = findProdus(idProdus);
                int remaining = stoc.get(p);
                System.out.print("Cate bucati din " + p.getNume() + " vrei? (max. " + remaining + " bucati)");
                cantitate = in.nextInt();
                if (cantitate > remaining) {
                    System.out.println("Stoc insuficient!");
                    in.nextLine();
                    return;
                }
                t.adaugaPeBon(p, cantitate);
                System.out.println("Adaugat!");
            } while(true);
        } catch (Exception e) {System.out.println(e);};
        in.nextLine();


    }

    public void afiseazaStocZero() {
        boolean ok = false;
        System.out.println("Urmatoarele produse nu se afla pe stoc:");
        for(Categorie c : categorii) {
            for(Produs p: c.getProduse()) {
                if (!stoc.getStoc().containsKey(p) || stoc.get(p) == 0) {
                    System.out.println("[" + p.getId() + "] " + p.getNume());
                    ok = true;
                }
            }

        }
        audit.log("afiseaza_alerta_stoc");

    }

    /*
    * Incarca datele salvate in csv-uri.
    * */
    public void incarcaDate() {

        String pathCategorie = "./date/Categorie.csv";
        String pathDistribuitor =  "date/Distribuitor.csv";
        String pathLivrare =  "date/Livrare.csv";
        String pathProdus =  "date/Produs.csv";

        FileReaderService fsv = FileReaderService.getInstance();

        // populeaza categorii
        ArrayList<ArrayList<String>> listaCategorii = fsv.read(pathCategorie);
        for(ArrayList<String> l : listaCategorii) {
            _creeazaCategorie(l.get(0));
        }

        // distribuitor
        ArrayList<ArrayList<String>> listaDistribuitori = fsv.read(pathDistribuitor);
        for(ArrayList<String> l : listaDistribuitori) {
            _creeazaDistribuitor(l.get(0),Integer.parseInt(l.get(1)));
        }

        // produs

        ArrayList<ArrayList<String>> listaProduse = fsv.read(pathProdus);
        for(ArrayList<String> l : listaProduse) {
            Integer idCategorie = Integer.parseInt(l.get(0));
            Integer tipProdus = Integer.parseInt(l.get(3));
            Produs p;
            if (tipProdus == 1) {
                // perisabil
                p = new ProdusPerisabil(l.get(1),Integer.parseInt(l.get(2)),Integer.parseInt(l.get(4)));
            } else {
                p = new ProdusNeperisabil(l.get(1),Integer.parseInt(l.get(2)),Integer.parseInt(l.get(4)));
            }
            categorii.get(idCategorie).adaugaProdus(p);
        }

        //livrare
        ArrayList<ArrayList<String>> listaLivrare = fsv.read(pathLivrare);
        System.out.println(listaLivrare);
        for(ArrayList<String> l : listaLivrare) {
            int idDistribuitor = Integer.parseInt(l.get(0));
            Categorie cat = distribuitori.get(idDistribuitor).getCategorie();

            try {
                Date data = new SimpleDateFormat("yyyy-MM-dd").parse(l.get(1));
                int nrProduse = Integer.parseInt(l.get(2));
                Livrare liv = new Livrare(distribuitori.get(idDistribuitor),data);
                for (int i=0; i<nrProduse*2; i+=2) {
                    int idProdus = Integer.parseInt(l.get(3+i));
                    int pret = Integer.parseInt(l.get(4+i));
                    System.out.println(idProdus);
                    System.out.println(pret);

                    liv.adaugaProdus(cat.getProdus(idProdus),pret);
                }
                stoc.adaugaLivrare(liv);
            }catch (ParseException p) {
                System.out.println("Bad date format");
            }



        }

    }
}
