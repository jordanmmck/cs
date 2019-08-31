#include <stdio.h>
/* This is a comment */

int main()
{
    char initial;
    char firstName[20], lastName[20];

printf("type your first initial:\n");
    scanf("%c", &initial);
    printf("%c\n", initial);

    printf("type your first and last name\n");
    scanf("%s %s", firstName, lastName);
    printf("%s %s\n", firstName, lastName);

    return 0;
}
