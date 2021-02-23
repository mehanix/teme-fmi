#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <sys/shm.h>
#include <pthread.h>
#include <errno.h>

#define MAX_RESOURCES 3

int available_resources = MAX_RESOURCES;

pthread_mutex_t mtx;
pthread_t *vthr;

int decrease_count(int count, int cpy)
{
    pthread_mutex_lock(&mtx);
    if (available_resources < count)
    {
        pthread_mutex_unlock(&mtx);
        return -1;
    }
    else
    {
        available_resources -= count;

        printf("%d: %d ", cpy, cpy);
        while (cpy != 1)
        {
            if (cpy % 2 == 1)
                cpy = cpy * 3 + 1;
            else
                cpy = cpy / 2;
            printf("%d ", cpy);
        }

        printf("Got %d resources %d remaining\n", count, available_resources);
        pthread_mutex_unlock(&mtx);
    }
    return 0;
}

int increase_count(int count)
{
    pthread_mutex_lock(&mtx);
    available_resources += count;
    printf("Released %d resources %d remaining\n", count, available_resources);
    pthread_mutex_unlock(&mtx);
    return 0;
}

void *f(void *argc)
{
    int *val = (int *)argc;
    int cpy = *val;
    while (decrease_count(1, cpy) == -1)
        sleep(1);
    increase_count(1);
    return NULL;
}

int main(int argc, char **argv)
{
    int n = argc - 1;
    int *v = malloc(sizeof(int) * argc);
    for (int i = 0; i < n; ++i)
        v[i] = atoi(argv[i + 1]);

    if (pthread_mutex_init(&mtx, NULL))
    {
        perror(NULL);
        return errno;
    }

    vthr = (pthread_t *)malloc(5 * sizeof(pthread_t));
    for (int i = 0; i < 5; ++i)
    {
        int *val;
        val = (int *)malloc(sizeof(int));
        *val = v[i];
        if (pthread_create(&vthr[i], NULL, f, val))
        {
            perror(NULL);
            return errno;
        }
    }

    for (int i = 0; i < 5; ++i)
    {
        if (pthread_join(vthr[i], NULL))
        {
            perror(NULL);
            return errno;
        }
        pthread_mutex_destroy(&mtx);
    }
    return 0;
}