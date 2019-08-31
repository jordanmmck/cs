#include <iostream>

using namespace std;

int array_sum_sentinel(int a[]) {
    int sum = 0;

    for (int i = 0; a[i] != -1; i++) 
            sum = sum + a[i];

    return sum;
}

int main() {
        int a[] = {2, 4, 6, 1, 3, -1};

        cout << array_sum_sentinel(a) << endl;

        cout << array_sum_sentinel(a + 2) << endl;

        return 0;
}
