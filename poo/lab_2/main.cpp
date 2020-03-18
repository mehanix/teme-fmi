#include <iostream>
#include "Complex.h"
#include "String.h"

String f(String o){return o;}

int main() {
    String s1;
    //  std::cout<<s1.getInfo()<<std::endl;
    String s2("abc def");
    //  std::cout<<s2.getInfo();
    String s3(std::string("lala lala"));
    //  std::cout<<s3.getInfo();

    String s4(s3);
    s4.change(1) = 'n';
// std::cout << s3.getInfo();
  //  std::cout << s4.getInfo();
 //   s1 = s4;
    s4.change(1, 'w');
    std::cout << s1.getInfo();

    String s5 = f(s3);
    String s77;
    String s6 = std::move(s77);
    std::cout<<s3.getInfo();


    return 0;
}