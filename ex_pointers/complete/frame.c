#include <stdio.h>

int main()
{
    char char_v1;
    int  int_v1;
    char char_v2;
    int  int_v2;
    char char_array[4];
    int  int_array[4];
    char char_v3;


    printf("Address of char_1:      %p\n", &char_v1);
    printf("Address of int_1:       %p\n", &int_v1);
    printf("Address of char_2:      %p\n", &char_v2);
    printf("Address of int_2:       %p\n", &int_v2);
    printf("Address of char_array:  %p\n", char_array);
    printf("Address of int_array:   %p\n", int_array);
    printf("Address of char_3:      %p\n", &char_v3);

}