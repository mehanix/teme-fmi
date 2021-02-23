#include <stdio.h>
#include <errno.h>
#include <pthread.h>
#include <string.h>
#include <stdlib.h>
int A[10][10], B[10][10], C[10][10];
int rand_a, col_a, rand_b, col_b, rand_c, col_c;

void *inmultire(void *args)
{
    int *numere = args;
    int *suma = calloc(sizeof(int), 1);
    printf("args: %d %d\n", numere[0], numere[1]);
    *suma = 0;
    for (int i = 0; i < col_a; i++)
        *suma += A[numere[0]][i] * B[i][numere[1]];
    return suma;
}
int main()
{
    printf("introdu nr linii nr col matricea A:");
    scanf("%d%d", &rand_a, &col_a);
    printf("introdu nr linii nr col matricea B:");
    scanf("%d%d", &rand_b, &col_b);
    if (col_a != rand_b)
    {
        printf("matrici incompatibile\n");
        return -1;
    }

    for (int i = 0; i < rand_a; i++)
        for (int j = 0; j < col_a; j++)
        {
            printf("A[%d][%d]=", i, j);
            scanf("%d", &A[i][j]);
        }

    for (int i = 0; i < rand_b; i++)
        for (int j = 0; j < col_b; j++)
        {
            printf("B[%d][%d]=", i, j);
            scanf("%d", &B[i][j]);
        }

    pthread_t thr[rand_a * col_b];
    int index_thr = 0;
    for (int i = 0; i < rand_a; i++)
        for (int j = 0; j < col_b; j++)
        {
            int *args = malloc(sizeof(int) * 2);
            args[0] = i;
            args[1] = j;
            if (pthread_create(&thr[index_thr], NULL, inmultire, args))
            {
                perror(NULL);
                return errno;
            }
            index_thr++;
        }
    index_thr = 0;
    void *result;
    for (int i = 0; i < rand_a; i++)
        for (int j = 0; j < col_b; j++)
        {
            if (pthread_join(thr[index_thr], &result))
            {
                perror(NULL);
                return errno;
            }
            C[i][j] = *(int *)result;
            index_thr++;
        }
    for (int i = 0; i < rand_a; i++)
    {
        for (int j = 0; j < col_b; j++)
            printf("%d ", C[i][j]);
        printf("\n");
    }
    return 0;
}