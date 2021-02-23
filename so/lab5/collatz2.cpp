#include <sys/types.h>
#include <unistd.h>
#include <errno.h>
#include <stdio.h>
#include <sys/wait.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
using namespace std;

int nr;
char *arg;
int main(int argc, char *argv[])
{
    //pid_t pid;
    if (argc == 0)
    {
        return errno;
    }

    //iau bucata memorie de page_size*nr argumente
    size_t page_size = getpagesize();
    size_t shm_size = page_size * (argc - 1);
    char shm_name[] = "myshm";
    int shm_fd;
    shm_fd = shm_open(shm_name, O_CREAT | O_RDWR, S_IRUSR | S_IWUSR);
    if (shm_fd < 0)
    {
        perror(NULL);
        return errno;
    }
    if (ftruncate(shm_fd, shm_size) == -1)
    {
        perror(NULL);
        shm_unlink(shm_name);
        return errno;
    }

    // pointer catre memorie
    int *results = mmap(0, shm_size, PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd, 0);
    for (int i = 1; i <= argc - 1; i++)
    {
        if (fork() == 0)
        {
            //pointer catre bucata din memorie unde pun intul
            int *nr = results + (i - 1) * page_size / sizeof(int);
            if (nr == MAP_FAILED)
            {
                return -1;
            }

            *nr = atoi(argv[i]);
            printf("%d: %d ", *nr, *nr);
            while (*nr != 1)
            {
                if (*nr % 2 == 0)
                    *nr = *nr / 2;
                else
                    *nr = 3 * *nr + 1;
                printf("%d ", *nr);
            }
            printf("\nDone Parent %d Me %d\n", getppid(), getpid());
            return 0;
        }
    }
            for (int i = 0; i < argc; i++)
            wait(NULL);
    printf("\nDone Parent %d Me %d\n", getppid(), getpid());
    munmap(results, shm_size);
    close(shm_fd);
    shm_unlink(shm_name);
}
