
#include <bits/stdc++.h>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

class Masina
{
protected:
    int an, viteza;
    string nume;
    float greutate;

public:
    Masina(int _an = 0, int _viteza = 0, string _nume = "", float _greutate = 0) : an(_an), viteza(_viteza), nume(_nume), greutate(_greutate){};
    virtual float get_Autonomie() = 0;
};

class ElectricCar : virtual public Masina
{
protected:
    int BatteryCapacity;

public:
    ElectricCar(int _an = 0, int _viteza = 0, string _nume = "", float _greutate = 0, int _batteryCapacity = 0) : Masina(_an, _viteza, _nume, _greutate), BatteryCapacity(_batteryCapacity){};
    float get_Autonomie()
    {
        return static_cast<float>(BatteryCapacity) / (greutate * greutate);
    }
    friend ostream &operator<<(ostream &out, const ElectricCar &e);
    friend istream &operator>>(istream &in, ElectricCar &e);
};

istream &operator>>(istream &in, ElectricCar &e)
{
    string _nume;
    int _batteryCapacity;
    int _an;
    int _greutate;
    in >> _nume >> _batteryCapacity >> _an >> _greutate;
    e.nume = _nume;
    e.BatteryCapacity = _batteryCapacity;
    e.an = _an;
    e.greutate = _greutate;
    return in;
}
ostream &operator<<(ostream &out, const ElectricCar &e)
{
    out << e.an << ' ' << e.BatteryCapacity << ' ' << e.nume << ' ' << e.greutate << '\n';
    return out;
}

class MasinaCombustibil : virtual public Masina
{
protected:
    int capacitate_rezervor;
    string tip_combustibil;

public:
    MasinaCombustibil(int _an = 0, int _viteza = 0, string _nume = "", float _greutate = 0, int _capacitate_rezervor = 0, string _tip_combustibil = "") : Masina(_an, _viteza, _nume, _greutate), capacitate_rezervor(_capacitate_rezervor), tip_combustibil(_tip_combustibil){};
    float get_Autonomie()
    {
        return static_cast<float>(capacitate_rezervor) / (greutate * greutate);
    }
};

class MasinaHibrid : public ElectricCar, public MasinaCombustibil
{

public:
    MasinaHibrid(int _an = 0, int _viteza = 0, string _nume = "", float _greutate = 0, int BatteryCapacity = 0, int _capacitate_rezervor = 0, string _tip_combustibil = "Benzina") : MasinaCombustibil(_an, _viteza, _nume, _greutate, _capacitate_rezervor),
                                                                                                                                                                                     Masina(_an, _viteza, _nume, _greutate), ElectricCar(_an, _viteza, _nume, _greutate, BatteryCapacity){};
    float get_Autonomie()
    {
        return ElectricCar::get_Autonomie() + MasinaCombustibil::get_Autonomie();
    }
};

class Tranzactie
{
    string nume_cumparator, data;
    vector<Masina *> achizitii;

public:
    Tranzactie(string nume_cumparator = "", string data = "", vector<Masina *> achizitii = {}) : nume_cumparator(nume_cumparator), data(data), achizitii(achizitii) {}
    /*~Tranzactie()
    {
        for (auto achizitie : achizitii)
            delete &achizitie;
        achizitii.clear();
    }*/
};

int main()
{
    ElectricCar electricCar;
    vector<Masina *> masini;
    masini.push_back(new ElectricCar());
    Tranzactie t("Ana", "2020-05-09", masini);
    cin>>electricCar;
    cout<<electricCar;

}
