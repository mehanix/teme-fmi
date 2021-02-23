#include <sys/types.h>
#include <unistd.h>
#include <errno.h>
#include <stdio.h>
#include <sys/wait.h>
#include <stdlib.h>
using namespace std;

int nr;
// ex 3
int main(int argc, char *argv[])
{
    pid_t pid;
    printf("Starting parent %d\n", getpid());
    if (argc == 0)
    {
        return errno;
    }
    for (int i = 1; i <= argc - 1; i++)
    {
        if (fork() == 0)
        {
            nr = atoi(argv[i]);
            printf("%d: %d ", nr, nr);
            while (nr != 1)
            {
                if (nr % 2 == 0)
                    nr = nr / 2;
                else
                    nr = 3 * nr + 1;
                //sleep(1);
                printf("%d ", nr);
            }
            printf("\nDone Parent %d Me %d\n", getppid(), getpid());
            return 0;
        }
    }
    for (int i = 0; i < argc; i++)
    {
        wait(NULL);
    }
    printf("\nDone Parent %d Me %d\n", getppid(), getpid());
}
