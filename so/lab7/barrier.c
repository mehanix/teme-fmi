#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <time.h>
#include <errno.h>
#include <unistd.h>
#include <semaphore.h>

pthread_mutex_t mtx;
int nr_threads = 5;
int reached = 0;
sem_t sem;
void barrier_point()
{
    pthread_mutex_lock(&mtx);
    reached++;
    if (reached == nr_threads)
    {
        pthread_mutex_unlock(&mtx);
        sem_post(&sem);
    }
    else
    {
        pthread_mutex_unlock(&mtx);

        sem_wait(&sem);
        sem_post(&sem);
    }
}
void *tfun(void *v)
{
    int *tid = (int *)v;
    printf("%d reached the barrier \n", *tid);
    barrier_point();
    printf("%d passed the barrier\n", *tid);

    free(tid);
    return NULL;
}
void init(int nr)
{
    nr_threads = nr;
}
int main()
{
    init(5);
    printf("nrthrs=%d\n", nr_threads);
    if (sem_init(&sem, 0, 0))
    {
        perror(NULL);
        return errno;
    }
    if (pthread_mutex_init(&mtx, NULL))
    {
        perror(NULL);
        return errno;
    }
    pthread_t thr[nr_threads];
    for (int i = 0; i < nr_threads; i++)
    {
        int *id = malloc(sizeof(int));
        *id = i;
        if (pthread_create(&thr[i], NULL, tfun, id))
        {
            perror(NULL);
            return errno;
        }
    }
    for (int i = 0; i < nr_threads; i++)
    {
        if (pthread_join(thr[i], NULL))
        {
            perror(NULL);
            return errno;
        }
    }
    pthread_mutex_destroy(&mtx);
    sem_destroy(&sem);
    return 0;
}