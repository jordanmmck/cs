#include <stdio.h>      /* printf */
#include <string.h>     /* strcat */
#include <stdlib.h>     /* strtol */

char *decimal_to_binary(int n){
    int c, d, count;
    char *pointer;
 
    count = 0;
    pointer = (char*)malloc(32+1);
 
    if ( pointer == NULL )
        exit(EXIT_FAILURE);
 
    for ( c = 31 ; c >= 0 ; c-- )
    {
        d = n >> c;
 
        if ( d & 1 )
            *(pointer+count) = 1 + '0';
        else
            *(pointer+count) = 0 + '0';
 
        count++;
    }
    *(pointer+count) = '\0';
 
    return  pointer;
}

int main(int argc, char *argv[]){ 
    int a=2000000000;

    printf("%s\n", decimal_to_binary(a));
    printf("%d\n", a);
    a<<=1;
    printf("%s\n", decimal_to_binary(a));
    printf("%d\n", a);
    a<<=1;
    printf("%s\n", decimal_to_binary(a));
    printf("%d\n", a);

}
