package com.company.entitati;

import com.company.entitati.Produs;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class Stoc {
    private Map<Produs,Integer> stoc;

    public Stoc() {
        this.stoc = new HashMap<Produs, Integer>();
    }

    public Map<Produs, Integer> getStoc() {
        return stoc;
    }

}
