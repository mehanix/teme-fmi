#include <sys/types.h>
#include <unistd.h>
#include <errno.h>
#include <stdio.h>
#include <sys/wait.h>
#include <stdlib.h>
using namespace std;

//ex 2
int nr;
int main(int argc, char *argv[])
{
    nr = atoi(argv[1]);
    pid_t pid = fork();
    if (pid < 0)
        return errno;
    else if (pid == 0)
    {
        //child
        printf("%d: %d ", nr, nr);
        while (nr != 1)
        {
            if (nr % 2 == 0)
                nr = nr / 2;
            else
                nr = 3 * nr + 1;
            printf("%d ", nr);
        }
        printf("\nChild %d finished\n", getpid());
    }
}
