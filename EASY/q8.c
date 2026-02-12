// Merge two sorted arrays into one sorted array (classic merge step).

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a[] = {1, 3, 4, 6, 9};
    int b[] = {2, 5, 7, 8, 10};
    int n1 = 5;
    int n2 = 5;
    int n3 = n1 + n2;
    int c[10];
    int i, j, k;
    j = 0;
    k = 0;
    i = 0;
    while (i < n1 && j < n2)
    {
        if (a[i] < b[j])
        {
            c[k] = a[i];
            i++;
            k++;
        }
        else if (a[i] == b[j])
        {
            c[k] = a[i];
            k++;
            i++;
            c[k] = b[j];
            k++;
            j++;
        }
        else
        {
            c[k] = b[j];
            j++;
            k++;
        }
    }

    while (i < n1)
    {
        c[k] = a[i];
        i++;
        k++;
    }

    while (j < n2)
    {
        c[k] = b[j];
        j++;
        k++;
    }

    int x;
    for (x = 0; x < n3; x++)
        printf("%d ", c[x]);

    return 0;
}