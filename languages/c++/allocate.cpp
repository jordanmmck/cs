#include <iostream>

using namespace std;

int g; // global

void f(int f0) { // parameter
    int f1 = f0; // local
}

int main() {
    int m0 = 100; // local

    f(m0);

    // allocate new dynamic memory. this is an array! *mp is a pointer that points
    // to the start of the array. 
    int *mp = new int[3]; 

    cout<<endl;
    cout<<endl;
    cout<< "*mp: " << *mp << endl; // this is a random 32 bit integer sitting in memory
    cout<< "mp: " << mp << endl;    // this is the memory location of the start of array

    cout<<endl;
    cout<< "assign '1' to mp[0]."<< endl;
    mp[0] = 1;

    cout<<endl;
    cout<< "*mp: " << *mp << endl;
    cout<< "mp: " << mp << endl;
    cout<<endl;

    cout<< "assign '2' to mp[1]."<< endl;
    mp[1] = 2;

    cout<<endl;
    cout<< "*mp: " << *mp +4 << endl;
    cout<< "mp: " << mp << endl;
    cout<<endl;

    cout<<endl;
    delete mp; // release the memory
}
