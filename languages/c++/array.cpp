#include <iostream>

using namespace std;

int array_sum_length(int a[], int n) {
    int sum = 0;

    for (int i = 0; i < n; i++) {
        sum = sum + a[i];
    }
    return sum;
}

int main() {
    int a[] = {2, 4, 6, 1, 3};

    cout << array_sum_length(a, 5) << endl;

    cout << array_sum_length(a, 3) << endl;

    cout << array_sum_length(a+1, 3) << endl;
}
