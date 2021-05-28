package com.company;

import com.company.servicii.CategorieService;
import com.company.servicii.Service;

import java.util.Scanner;

public class Main {

    public static void main(String[] args)  {
        Scanner in = new Scanner(System.in);
        Service service = new Service();
        CategorieService cats  = CategorieService.getInstance();
        service.incarcaDate(in);
        String command = "";
        while (command != "13") {
            System.out.println("========================================");
            System.out.println("= Sistem de gestionare al magazinului: =");
            System.out.println("========================================");
            System.out.println("Introdu comanda: ");
            System.out.println("1. Adauga categorie");
            System.out.println("2. Adauga produs");
            System.out.println("3. Adauga distribuitor");
            System.out.println("4. Vezi toate produsele dintr-o categorie");
            System.out.println("5. Adauga o livrare in sistem");
            System.out.println("6. Afiseaza stoc");
            System.out.println("7. Efectueaza o tranzactie");
            System.out.println("8. Alerta stoc - afiseaza produsele cu stoc 0");
            System.out.println("9. Vezi detaliile unui produs");
            System.out.println("10. Vezi istoric livrari");
            System.out.println("11. Modifica numele unui distribuitor");
            System.out.println("12. Sterge o categorie");
            System.out.println("13. Iesire");

            command = in.nextLine();
            try {
                switch (command) {
                    case "1": {
                        service.adaugaCategorie(in);
                        break;
                    }
                    case "2": {
                        service.adaugaProdus(in);
                        break;
                    }
                    case "3": {
                        service.adaugaDistribuitor(in);
                        break;
                    }
                    case "4": {
                        service.veziProduseCategorie(in);
                        break;
                    }
                    case "5": {
                        service.adaugaLivrare(in);
                        break;
                    }
                    case "6": {
                        service.afiseazaStoc();
                        break;
                    }
                    case "7": {
                        service.efectueazaTranzactie(in);
                        break;
                    }
                    case "8": {
                        service.afiseazaStocZero();
                        break;
                    }
                    case "9": {
                        service.veziDetaliiProdus(in);
                        break;
                    }
                    case "10": {
                        service.veziIstoricLivrari();
                        break;
                    }
                    case "11": {
                        service.modificaNumeDistribuitor(in);
                        break;
                    }
                    case "12": {
                        service.stergeCategorie(in);
                        break;
                    }
                    case "13": {
                       return;
                    }
                }
            } catch (Exception e) {
                System.out.println(e.toString());
            }
        }
    }
}
