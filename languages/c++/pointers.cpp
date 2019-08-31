#include <iostream>
using namespace std;

int main (){
    int number = 5;
    int *numberPtr = &number;

    cout << &number << ": " << number << endl;      
    cout << numberPtr << ": " << number << endl;    

    int *array = new int[4] = {0, 1, 2, 3};

    for(int i = 0; i<4; i++){
            cout << array+i << ": "<< *(array+i) << " "<< array[i] << endl;
    }

    cout << "*array: " << *array << endl;
    cout << "array: " << array << endl;
    cout << "array[1]: " << array[1] << endl;

    delete array;
}
