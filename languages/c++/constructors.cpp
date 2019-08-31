#include <iostream>

using namespace std;


class C {
public:
    // default constructor
    C(){cout << "default constructor" << endl;}
    // constructor
    C(int i0){i = i0; cout << "constructor: " << i << endl;}
    // destructor
    ~C(){cout << "destructor: " << i << endl;}
private:
    int i;
};


int main() {
    cout << endl;
    cout << "a: " ;
    C a;

    cout << "b: " ;
    C b(10000000);  

    cout << "c: " ;
    C *c = new C(20000000);         // must have *

    cout << "c: " << c << " &c: " << &c << endl;            // cannot print *c

    delete c;
}
