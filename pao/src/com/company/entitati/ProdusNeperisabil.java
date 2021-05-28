package com.company.entitati;

public class ProdusNeperisabil extends Produs {
    private Integer aniGarantie;


    public ProdusNeperisabil(int id,String nume, Integer pret, Integer aniGarantie) {
        super(id, nume, pret);
        this.aniGarantie = aniGarantie;
    }

    public Integer getAniGarantie() {
        return aniGarantie;
    }

    public void setAniGarantie(Integer aniGarantie) {
        this.aniGarantie = aniGarantie;
    }

    public void afiseaza() {
        super.afiseaza();

        System.out.println("Produs neperisabil cu perioada de garantie: " + aniGarantie + " ani");
    }
}
