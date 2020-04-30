

#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <ctime>
 
using namespace std;
 
class Animal
{
   int age;
   string Name;
 
public:
   Animal(int age = 0, string Name = "") : age(age), Name(Name) {}
   virtual void Zice() = 0;
};
 
class Caine : public Animal
{
   string rasa;
 
public:
   Caine(int age = 0, string Name = "", string rasa = "") : Animal(age, Name), rasa(rasa) {}
   void Zice() override
   {
       cout << "HAM!\n";
   }
};
 
class Pisica : public Animal
{
   string rasa;
 
public:
   Pisica(int age = 0, string Name = "", string rasa = "") : Animal(age, Name), rasa(rasa) {}
   void Zice() override
   {
       cout << "MIAU!\n";
   }
};
 
class Hamster : public Animal
{
   string rasa;
 
public:
   Hamster(int age = 0, string Name = "", string rasa = "") : Animal(age, Name), rasa(rasa) {}
   void Zice() override
   {
       cout << "Hatz!\n";
   }
};
 
int main()
{
 
   // Animal *a1 = new Caine(5, "rex", "maidanez");
   // Animal *a2 = new Pisica(5, "natasha", "pisica");
 
   // if(dynamic_cast<Pisica*>(a1)) {
   //     cout << "Pisca";
   // } else {
   //     cout << "Caine";
   // }
 
   // a1->Zice();
   // a2->Zice();
 
   srand(time(NULL));
 
   vector<Animal *> animale;
 
   for (int i = 0; i < 10; i++)
   {
       int tip = rand() % 3;
       switch (tip)
       {
       case 0:
           animale.push_back(new Caine(rand() % 12, "", ""));
           break;
 
       case 1:
           animale.push_back(new Pisica(rand() % 12, "", ""));
           break;
       case 2:
           animale.push_back(new Hamster(rand() % 20, "", ""));
           break;
       }
   }
 
   for (auto &animal : animale)
   {
       if (dynamic_cast<Pisica *>(animal))
       {
           cout << "Pisca";
       }
       else if (dynamic_cast<Hamster *>(animal))
       {
           cout << "Hamster";
       }
       else
       {
           cout << "Caine";
       }
       animal->Zice();
   }
 
   return 0;
}

