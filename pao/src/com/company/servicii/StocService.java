package com.company.servicii;

import com.company.entitati.*;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.text.SimpleDateFormat;
import java.util.*;

import static com.company.servicii.Environment.conn;


public class StocService {
    private static StocService instanta = null;
    private final Stoc stoc = new Stoc();
    private ArrayList<Tranzactie> tranzactii = new ArrayList<Tranzactie>();
    private final CategorieService categorieService = CategorieService.getInstance();


    // constructor privat
    private StocService() {

    }

    public void efectueazaTranzactie(Scanner in) {
        Tranzactie t = new Tranzactie();

        afiseaza();

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
                        tranzactii.add(t);
                        System.out.println("Tranzactie efectuata cu succes!");

                        return;
                    }
                    System.out.println("Tranzactie anulata!");
                    return;
                }
                p = categorieService.findProdus(idProdus);
                int remaining = stoc.get(idProdus);
                System.out.print("Cate bucati din " + p.getNume() + " vrei? (max. " + remaining + " bucati)");
                cantitate = in.nextInt();
                if (cantitate > remaining) {
                    System.out.println("Stoc insuficient!");
                    in.nextLine();
                    return;
                }
                t.adaugaPeBon(idProdus, cantitate);
                System.out.println("Adaugat!");
            } while(true);
        } catch (Exception e) {System.out.println(e); e.printStackTrace();};
    }

    public void afiseaza() {
        stoc.afiseaza();
    }
    public void afiseazaIstoric() {
        stoc.afiseazaIstoric();
    }

    public static StocService getInstance() {
        if (instanta == null)
            instanta = new StocService();
        return instanta;
    }

    // CRUD

    // Update: Modifica o categorie
    public boolean update(int id, String nume) {
        return false;
    }

    // Delete
    public boolean delete(int id) {
        return false;
    }

    public void loadFromDb() {
        // incarc livrarile si le bag in stoc
        stoc.clear();

        try {
            Statement stmt = conn.createStatement();
            ResultSet res = stmt.executeQuery("select * from Livrare");
            while (res.next()) {
                Date data = res.getDate("data");
                Livrare l = new Livrare(res.getInt("id"),res.getInt("idDistribuitor"),data);
                // get produse si cantitati pe livrarea l
                String query = String.format("select idProdus, cantitate from LivrareProdus where idLivrare=%d", res.getInt("id"));
                Statement stmt2 = conn.createStatement();
                ResultSet prodCant = stmt2.executeQuery(query);
                while (prodCant.next()) {
                    l.adaugaProdus(prodCant.getInt("idProdus"),prodCant.getInt("cantitate"));
                }
                stoc.adaugaLivrare(l);
            }
            recalculeazaStoc();
        } catch (Exception e) {
            e.printStackTrace();
        }

    }

    private void recalculeazaStoc() {
        System.out.println("size"+" " +tranzactii.size());
        for (Tranzactie t: tranzactii) {
            stoc.efectueaza(t);
        }
    }

    public void afiseazaStocZero() {
        System.out.println("Urmatoarele produse nu se afla pe stoc:");
        for(Categorie c : categorieService.getCategorii()) {
            for(Produs p: c.getProduse()) {
                if (!stoc.getStoc().containsKey(p.getId()) || stoc.get(p.getId()) == 0) {
                    System.out.println("[" + p.getId() + "] " + p.getNume());
                }
            }

        }
    }

    public void adaugaLivrare(Livrare l) {
        try {
            int id = l.getId();
            String query = "insert into Livrare () values(null, ?, ?)";
//            String query = "insert into Livrare values(null, '%s', %d)",  new SimpleDateFormat("yyyy-MM-dd").format(l.getData()), l.getIdDistribuitor());

            PreparedStatement st = conn.prepareStatement(query, Statement.RETURN_GENERATED_KEYS);
            st.setString(1,new SimpleDateFormat("yyyy-MM-dd").format(l.getData()));
            st.setInt(2,l.getIdDistribuitor());
            st.executeUpdate();
            try (ResultSet generatedKeys = st.getGeneratedKeys()) {
                if (generatedKeys.next()) {
                    l.setId(generatedKeys.getLong(1));
                }

            } catch (Exception e) {e.printStackTrace();}

            for(Map.Entry<Integer,Integer> pc : l.getProduseCantitati().entrySet()) {
                String query2 = String.format("insert into LivrareProdus values (null,%d,%d,%d)",l.getId(),pc.getKey(),pc.getValue());
                System.out.println(query2);
                Statement stmt = conn.createStatement();
                stmt.executeUpdate(query2);
            }
            loadFromDb();
        } catch (Exception e) {
            System.err.println("Eroare de scriere, incearca din nou!");

        }

    }
}

