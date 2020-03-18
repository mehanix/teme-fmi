//
// Created by nico7 on 3/5/2020.
//

#ifndef LAB_2_STRING_H
#define LAB_2_STRING_H
#include <cstring>
#include <utility>

class String {
private:
    size_t len;
    char *info;
public:
    String() : len(0), info(new char('\0')) {}

    String(char *p) : len(std::strlen(p)) {
        info = new char[len + 1];
        std::strcpy(info, p);
    }

    inline char *getInfo() const {
        return this->info;
    }

    String(std::string str) : len(str.size()) {
        info = new char[len + 1];
        for (int i = 0; i < len; i++) {
            info[i] = str[i];
        }
        info[len] = '\0';
    }

    String(const String &other) : len(other.len) {
        info = new char[len + 1];
        strcpy(info, other.info);
    }

    void change(unsigned poz, char c) {
        if (poz >= len)
            return;
        info[poz] = c;
    }

    char &change(unsigned pos) {
        if (pos <= len) { return info[pos]; }
    }
/*
    String(String &&other) : len(std::exchange(len, 0)), info(std::exchange(other.info, nullptr)) {
        std::cout
                << "MC\n"; ///exchange returneaza pointer spre primul param, si pe al 2lea pointer il seteaza cu valoarea param2
    }
*/
    ///Move assignment operator///
    String &operator = (String &&) = default;
            /*{

        len = std::exchange(other.len, 0);
        info = std::exchange(other.info, nullptr);
        std::cout << "MC egal\n";
        return *this;
    }*/


    String& operator = (const String& rhs) { ///overload pe operatorul =
        if (&rhs != this) {
            delete[] info;
            len = rhs.len;
            info = new char[len + 1];
            strcpy(info, rhs.info);
            return *this;
        }

    }

};
#endif //LAB_2_STRING_H
