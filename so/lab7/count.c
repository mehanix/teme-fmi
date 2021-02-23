#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <time.h>
#include <errno.h>
#include <unistd.h>
#define MAX_RESOURCES 5

int available_resources = MAX_RESOURCES;
pthread_mutex_t mtx;
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
        pthread_mutex_unlock(&mtx);
    }

    return 0;
}

int increase_count(int count)
{
    pthread_mutex_lock(&mtx);
    available_resources += count;
    pthread_mutex_unlock(&mtx);

    return 0;
}
void *f(void *argc)
{
    int *val = (int *)argc;
    int cpy = *val;
    //get resursa
    int res;
    res = decrease_count(1, cpy);
    if (res == 0)
    {
        //  printf("Got %d resources %d remaining\n", 1, available_resources);

        increase_count(1);
        // printf("Released %d resources %d remaining\n", 1, available_resources);
    }
}

int main()
{
    int thread_count = 10;
    printf("MAX_RESOURCES=%d\n", MAX_RESOURCES);
    if (pthread_mutex_init(&mtx, NULL))
    {
        perror(NULL);
        return errno;
    }
    srand(time(NULL));
    pthread_t thr[thread_count];
    for (int i = 0; i < thread_count; i++)
    {
        if (pthread_create(&thr[i], NULL, f, NULL))
        {
            perror(NULL);
            return errno;
        }
    }
    for (int i = 0; i < thread_count; i++)
    {
        if (pthread_join(thr[i], NULL))
        {
            perror(NULL);
            return errno;
        }
    }
    pthread_mutex_destroy(&mtx);
    return 0;
}