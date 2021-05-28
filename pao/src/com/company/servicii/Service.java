
package com.company.servicii;

import com.company.entitati.*;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;
import static com.company.servicii.Environment.*;

public class Service {

    /*
    Service prinicipal cu toate comenzile din meniu.
    * */

    private AuditService audit = AuditService.getInstance();
    private FileWriterService fws = FileWriterService.getInstance();

    private CategorieService categorieService = CategorieService.getInstance();
    private DistribuitorService distribuitorService = DistribuitorService.getInstance();
    private ProdusService produsService = ProdusService.getInstance();
    private StocService stocService = StocService.getInstance();

    // 1
    public void adaugaCategorie(Scanner in) {
        String nume;
        System.out.println("Introdu numele categoriei:");
        nume = in.nextLine();

        categorieService.creeazaCategorie(nume);
        audit.log("adauga_categorie");

    }

    // 3
    public void adaugaDistribuitor(Scanner in) {

        if (categorieService.getSize() == 0) {
            System.out.println("Nu poti adauga distribuitori daca nu exista categorii!");
            return;
        }
        try {
            System.out.println("Introdu numele distribuitorului:");
            String nume = in.nextLine();
            Categorie cat = categorieService.selecteazaCategorie("Introdu id-ul categoriei de produse pe care distribuitorul le va furniza:",in);
            distribuitorService.creeazaDistribuitor(nume, cat);
            System.out.println("Adaugat cu succes!");
            audit.log("adauga_distribuitor");

        } catch (Exception e) {
            System.out.println("Ai introdus input gresit!");
        }
        in.nextLine();

    }

    //4
    public Categorie veziProduseCategorie(Scanner in) {
        if (categorieService.getSize() == 0)
        {
            System.out.println("Nu exista categorii");
            return null;
        }
        Categorie selectata = categorieService.selecteazaCategorie("Introdu numarul categoriei pentru care vrei sa vezi produsele: ",in);
        selectata.afiseaza();

        in.nextLine();
        audit.log("afiseaza_produse_categorie");

        return selectata;
    }

    public void adaugaProdus(Scanner in) {
        Categorie cat;

        if (categorieService.getSize() == 0)
        {
            System.out.println("Trebuie creata minim o categorie pentru a adauga produse!");
            return;
        }

        cat = categorieService.selecteazaCategorie("Din ce categorie face parte produsul?",in);
        produsService.creeazaProdus(cat,in);
        categorieService.loadFromDb();
        in.nextLine();
        audit.log("adauga_produs");

    }
    public void adaugaLivrare(Scanner in) throws ParseException {
        if (distribuitorService.getSize() == 0 ) {
            System.out.println("Nu exista niciun distribuitor - nu are cine sa faca livrari");
            return;
        }

        distribuitorService.afiseazaDistribuitori();
        System.out.print("Id-ul distribuitorului: ");
        int idDistribuitor = in.nextInt();
        if (idDistribuitor == -1) {
            System.out.println("Anulez...");
            return;
        }
        Distribuitor d = distribuitorService.getDistribuitor(idDistribuitor);
        if (d == null)
            return;
        System.out.print("Data livrarii (yyyy-mm-dd): ");
        String dataStr = in.next();
        System.out.println(dataStr);
        Livrare l;
        try {
            Date data = new SimpleDateFormat("yyyy-MM-dd").parse(dataStr);
            l = new Livrare(-1,idDistribuitor,data);

        }   catch(ParseException e) {
            System.out.println("Data incorecta, anulez...");
            in.nextLine();
            return;
        }
        System.out.println("Acestea sunt produsele pe care le poate livra distribuitorul " + d.getNume() +": ");
        Categorie cat = d.getCategorie();
        cat.afiseaza();

        int idProdus = -1;
        int cantitate;
        do {
            try {
                System.out.print("Introdu id-ul produsului, sau -1 pentru a termina/anula: ");
                idProdus = in.nextInt();
                if (idProdus == -1)
                    break;
                Produs p = cat.getProdus(idProdus);
                System.out.print("Cate produse " + p.getNume() + " vor fi livrate? ");
                cantitate = in.nextInt();
                l.adaugaProdus(idProdus,cantitate);
                System.out.println("Adaugat!");
                audit.log("adauga_livrare");



            }
            catch(Exception e) {
                System.out.print("Input invalid!");

            }
        } while (true);

        if (l.getProduseCantitati().isEmpty()) {
            System.out.println("Livrare fara marfa, o anulez...");
            in.nextLine();
            return;

        }
        stocService.adaugaLivrare(l);

        System.out.println("Livrare adaugata cu succes!");

        in.nextLine();


    }

    public void veziDetaliiProdus(Scanner in) {
        if (categorieService.getSize() == 0)
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
        stocService.afiseaza();
        audit.log("afiseaza_stoc");

    }

    public void veziIstoricLivrari() {
        stocService.afiseazaIstoric();
        audit.log("afiseaza_istoric_livrari");

    }

    public void efectueazaTranzactie(Scanner in) {
        stocService.efectueazaTranzactie(in);
        audit.log("efectueaza_tranzactie");
        in.nextLine();


    }

    public void afiseazaStocZero() {
        boolean ok = false;
        stocService.afiseazaStocZero();
        audit.log("afiseaza_alerta_stoc");

    }

    /*
    * Incarca datele salvate in db.
    * */
    public void incarcaDate(Scanner in) {

        // Incarca categorii
        categorieService.loadFromDb();
        distribuitorService.loadFromDb();
        stocService.loadFromDb();
    }

    public void modificaNumeDistribuitor(Scanner in) {

        Distribuitor d = distribuitorService.afiseazaDistribuitori("Introdu id-ul distribuitorului al carui nume vrei sa il modifici:",in);
        in.nextLine();
        System.out.println("Introdu numele nou:");
        String nume = in.nextLine();
        try {
            // CRUD Db Update
            Statement stmt = conn.createStatement();
            stmt.executeUpdate(String.format("update Distribuitor set `nume`='%s' where `id`=%d",nume,d.getId()));
            distribuitorService.loadFromDb();

        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }

    }

    public void stergeCategorie(Scanner in) {
        Categorie c = categorieService.selecteazaCategorie("Introdu id-ul categoriei pe care doresti sa o stergi:(sau -1 pt anulare)",in);
        if (c != null) {
            try {
                Statement stmt = conn.createStatement();
                stmt.executeUpdate(String.format("delete from Categorie where id=%d", c.getId()));
                incarcaDate(in);

            } catch (SQLException throwables) {
                throwables.printStackTrace();
            }
        }
    }
}
