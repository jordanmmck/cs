#include <stdio.h>
#include <stdlib.h>
#include "../include/headers.h"

int main(){
    int a;
    int b;
    a = add(15,9);
    b = sub(15,9);
    if(a>0 && b>0)
        printf("\nMain executed succesfully\n\n");
}
