#include <unistd.h>
#include <sys/stat.h>
#include <stdio.h>
#include <errno.h>
#include <sys/types.h>
#include <fcntl.h>
#include <stdlib.h>

#define MIN(X, Y) (((X) < (Y)) ? (X) : (Y))
int main(int argc, char **argv)
{

    char *source_path = argv[1];
    char *dest_path = argv[2];
    int fd_s, fd_d;

    // deschid fisier sursa
    fd_s = open(source_path, O_RDONLY);

    if (fd_s < 0)
    {
        return errno;
    }
    // creez fisier nou cu numele dest_path
    fd_d = open(dest_path, O_WRONLY | O_CREAT | O_TRUNC, S_IRWXU); //file descriptor dest
    if (fd_d < 0)
    {
        return errno;
    }

    struct stat info;
    if (fstat(fd_s, &info) < 0)
    {
        return errno;
    }

    int file_size = info.st_size;
    int read_result, write_result;
    char buffer[1024];
    int transferred = 0;
    while (transferred < file_size)
    {
        // cat timp mai am de citit
        int remaining = file_size - transferred;
        int to_read = MIN(1024, remaining); // citesc 1024 chars sau cat mi a ramas

        //citesc
        read_result = read(fd_s, buffer, to_read);
        if (read_result < 0)
        {
            perror("read error:");
            break;
        }

        //scriu
        int written = 0;
        write_result = 0;
        //cat timp mai am de scris din ce am citit
        while (written < read_result)
        {
            int remaining = read_result - written;
            write_result = write(fd_d, buffer, remaining);
            if (write_result < 0)
            {
                break;
            }
            written += write_result;
        }
        if (write_result < 0)
        {
            perror("write error:");
            break;
        }

        transferred += read_result;
    }

    if (close(fd_s) < 0)
    {
        perror("closing source error:");
    }
    if (close(fd_d) < 0)
    {
        perror("closing dest error:");
    }
}