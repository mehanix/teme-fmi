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

char *arg;
int main(int argc, char *argv[])
{
    //pid_t pid;
    if (argc == 1)
    {
        return errno;
    }

    //iau bucata memorie de page_size*nr argumente
    size_t page_size = getpagesize();
    size_t shm_size = page_size * (argc - 1) * sizeof(int);
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
    int *results = (int *)mmap(0, shm_size, PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd, 0);
    for (int i = 1; i < argc; i++)
    {
        pid_t child_pid = fork();
        if (child_pid == 0)
        {
            //pointer catre bucata din memorie unde pun valorile
            int *buf = results + i * page_size / sizeof(int);
            if (buf == MAP_FAILED)
            {
                return -1;
            }

            int nr = atoi(argv[i]);
            int len = 0;
            //printf("%d: %d ", nr, nr);
            while (nr != 1)
            {
                buf[++len] = nr;
                if (nr % 2 == 0)
                    nr = nr / 2;
                else
                    nr = 3 * nr + 1;
            }
            buf[len] = nr;
            buf[0] = len;
            // printf("\nDone Parent %d Me %d\n", getppid(), getpid());
            return 0;
        }
        else if (child_pid < 0)
        {
            return 1;
        }
    }
    //astept sa termine toti
    for (int i = 1; i < argc; i++)
        wait(NULL);

    for (int i = 1; i < argc; i++)
    {
        int *buf = &results[i * page_size / 4];
        int size = buf[0];
        printf("%d\n", size);
        for (int j = 1; j <= size; ++j)
        {
            printf("%d ", buf[j]);
        }
        printf("\n");
    }
    printf("\nDone Parent %d Me %d\n", getppid(), getpid());
    munmap(results, shm_size);
    close(shm_fd);
    shm_unlink(shm_name);
}
