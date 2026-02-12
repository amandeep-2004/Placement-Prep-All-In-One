// Rotate array right by k steps (do it in O(n) without using extra full array if possible)

#include <stdio.h>
#include <stdlib.h>

void main()
{
    int n = 5;
    int a[] = {1, 2, 3, 4, 5};
    int k = 2;
    int i;
    int j = n - 1;
    for (i = 0; i < n / 2; i++)
    {
        a[i] = a[i] + a[j];
        a[j] = a[i] - a[j];
        a[i] = a[i] - a[j];
        j--;
    }
    j = k - 1;
    for (i = 0; i < k / 2; i++)
    {
        a[i] = a[i] + a[j];
        a[j] = a[i] - a[j];
        a[i] = a[i] - a[j];
        j--;
    }
    j = n - 1;
    int t = ((n - k) / 2) + k;
    for (i = k; i < t; i++)
    {
        a[i] = a[i] + a[j];
        a[j] = a[i] - a[j];
        a[i] = a[i] - a[j];
        j--;
    }

    for (i = 0; i < n; i++)
    {
        printf("%d ", a[i]);
    }
}