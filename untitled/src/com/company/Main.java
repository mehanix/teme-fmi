package com.company;

class A{
    int intA;
    public A met1(){
        return new A();
    }
    private void met2(){}

    private int met5(int i){return 5;}
}

class B extends A{
    int intB;
    public B met1(){
        return new B();
    }
    public void met2(){}

    private int met5(){return 5;}
}

public class Main {
    public static void main(String[] args) {
        Fir fir = new Fir(0);
        fir.start();
    }
}