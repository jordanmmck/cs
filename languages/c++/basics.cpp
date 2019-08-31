#include <iostream>
#include <string>
/* #include "helper.h" */
using namespace std;

//int product(int a, int b);

class myClass{
    public:
        myClass(){ X=0; cout << X << endl;}
        myClass(int newX){ X = newX; cout << X << endl;}
        ~myClass(){     cout << "d: "<< X << endl;}

        void setX(int newX){X = newX;}
        int getX(){return X;}

    private:
        int X;
};

int main(){

     myClass object1(3);
     object1.setX(5);
     cout<< object1.getX() << endl;

     myClass *object2 = new myClass(100);
     delete object2;

     helper object3;


     //myClass *Object = new myClass(20);


     /********************************************
     cout<< "\nBasics of C++:\n\n";

     int a;
     int b;
     int sum;

     cout << "Enter a number:\t\t";
     cin >> a;

     cout << "Enter another number:\t";
     cin >> b;

     cout << "Sum =\t\t\t" << a+b << endl;
     

     int num = 99;
     int array[] = {1, 2, 3};

     cout << sizeof(num) << endl;
     cout<< sizeof(array) << endl;
     cout << product(5, 9) << endl;
     ********************************************/

     return 0;
}
