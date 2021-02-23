#include <stdio.h>
#include <errno.h>
#include <pthread.h>
#include <string.h>

char *reversed;

void *reverse(void *v)
{
    char *who = (char *)v;
    int len = strlen(who);
    char rev[len + 1];
    for (int i = 0, j = len - 1; i < len; i++, j--)
    {
        rev[j] = who[i];
    }
    rev[len] = '\0';
    reversed = rev;
    return reversed;
}

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("wrong number of arguments\n");
        return -1;
    }

    char *msg = argv[1];

    pthread_t thr;
    if (pthread_create(&thr, NULL, reverse, msg))
    {
        perror(NULL);
        return errno;
    }

    void *result;
    if (pthread_join(thr, &result))
    {
        perror(NULL);
        return errno;
    }
    printf(result);
}