#include "sorts.h"
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <time.h>

// Linear congruential random number generator
// Constants from Kernighan & Ritchie, C Programming Language
int lcrng(int nbits, int reset) {
    static int rnd = 1;
    if (reset) {
        rnd = 1;
    } else {
        rnd = (rnd * 1103515245 + 12345) & ((1U << nbits) - 1);
    }
    return rnd;
}

int *randarray(int nbits) {
    lcrng(nbits, 1);        // reset to same seed
    int size = 1<<nbits;
    int *array = malloc(size * sizeof(int));
    for (int i = 0;  i < size;  i++) {
        array[i] = lcrng(nbits, 0);
    }
    return array;
}

void print_array(int *a, int size) {
    for (int i = 0;  i < size;  i++) {
        printf("%d ", a[i]);
    }
    printf("\n");
}

void validate_sorted(int *a, int size) {
    for (int i = 0;  i < size;  i++) {
        assert(a[i] == i);
    }
}

void time_sorts(int nbits) {
    const int size = 1 << nbits;
    int *data;

    clock_t start, end;
    double elapsed;

    printf("%d,", size);

    // Selection Sort
    data = randarray(nbits);
    start = clock();
    SelectionSort(data, size);
    end = clock();
    validate_sorted(data, size);
    elapsed = (double)(end - start) / CLOCKS_PER_SEC;
    printf("%f,", elapsed);
    free(data);

    // Insertion Sort
    data = randarray(nbits);
    start = clock();
    InsertionSort(data, size);
    end = clock();
    validate_sorted(data, size);
    elapsed = (double)(end - start) / CLOCKS_PER_SEC;
    printf("%f,", elapsed);
    free(data);

    // Insertion Sort Improved
    data = randarray(nbits);
    start = clock();
    InsertionSortImproved(data, size);
    end = clock();
    validate_sorted(data, size);
    elapsed = (double)(end - start) / CLOCKS_PER_SEC;
    printf("%f,", elapsed);
    free(data);

    // Bubble Sort
    data = randarray(nbits);
    start = clock();
    BubbleSort(data, size);
    end = clock();
    validate_sorted(data, size);
    elapsed = (double)(end - start) / CLOCKS_PER_SEC;
    printf("%f,", elapsed);
    free(data);

    // Bubble Sort Improved
    data = randarray(nbits);
    start = clock();
    BubbleSortImproved(data, size);
    end = clock();
    validate_sorted(data, size);
    elapsed = (double)(end - start) / CLOCKS_PER_SEC;
    printf("%f\n", elapsed);
    free(data);
}

int main() {
    for (int nbits = 10;  nbits <= 16;  nbits++) {
        time_sorts(nbits);
    }
}