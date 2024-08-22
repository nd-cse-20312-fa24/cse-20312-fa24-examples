#include "duplicates.h"
#include <stdio.h>
#include <time.h>

#define SIZE (1<<12)

int main()
{
    int array[SIZE];
    for (int i = 0;  i < SIZE;  i++) {
        array[i] = i;
    }
    array[SIZE-1] = array[SIZE-2];

    clock_t start, end;
    bool found;
    double elapsed;

    printf("Slow\n");
    start = clock();
    found = has_duplicates_slow(array, SIZE);
    end = clock();
    elapsed = (double)(end - start)/CLOCKS_PER_SEC;
    printf("Time: %f seconds.\n", elapsed);

    printf("Fast\n");
    start = clock();
    found = has_duplicates_fast(array, SIZE);
    end = clock();
    elapsed = (double)(end - start)/CLOCKS_PER_SEC;
    printf("Time: %f seconds.\n", elapsed);

    if (found) {
        printf("found duplicate\n");
    } else {
        printf("no duplicates\n");
    }
}