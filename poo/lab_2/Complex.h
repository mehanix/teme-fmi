//
// Created by nico7 on 3/5/2020.
//

#ifndef LAB_2_COMPLEX_H
#define LAB_2_COMPLEX_H
class Complex {
    int r, i;
public:
    explicit Complex(int init = 0) : r(init), i(init) {
        std::cout << "c";
        std::cout << sizeof(r);
    } //constructor
    Complex(const Complex &ob) : r(ob.r), i(ob.i) { std::cout << "cc"; } //copy constructor



};
#endif //LAB_2_COMPLEX_H
