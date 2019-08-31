#include <iostream>

using namespace std;

class C {
    public:
        //default constructor
        C() { a[0] = 5; a[1] = 10; a[2] = 15;}
        // Destructor only needed for dynamic!
        //~C(){cout<<"destruct"<<endl;}

        // We are overloading the operator []
        // How does it know which thing to use?
        //int size(){return a.size();}

        int& operator[](unsigned int i)                                        { cout << "not const" << endl; return a[i]; };

        const int& operator[](unsigned int i) const
            { cout << "const" << endl; return a[i]; };

    private:
        int a[5];
};

void f(const C &x) {
        cout << "f " << x[0] << endl;
}

int main() {
    cout<<endl;

    int b[5] = {1, 2, 3, 4, 5};
    cout << "size of b: " << sizeof(b)/sizeof(b[0]) << endl;

    C x;

    cout << x[0] << endl;

    cout << x.operator[](0) << endl;

    f(x);

    cout<<endl;
}
