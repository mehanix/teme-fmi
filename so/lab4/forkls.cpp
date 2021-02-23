#include <sys/types.h>
#include <unistd.h>
#include <errno.h>
#include <stdio.h>
using namespace std;

int main()
{
    pid_t pid = fork();
    if (pid < 0)
        return errno;
    else if (pid == 0)
    {
        //copil
        char *argv[] = {"ls", NULL};
        execve("/usr/bin/ls", argv, NULL);
        perror(NULL);
    }
    else
    {
        //parent
        printf("My PID: %d Child PID: %d\n", getpid(), pid);
    }
}