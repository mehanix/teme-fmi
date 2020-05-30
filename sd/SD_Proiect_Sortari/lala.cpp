#include <iostream>
#include <unistd.h>
#include <sys/types.h>
void slp(int x)
{
    printf("   %d", x);
}

int main(int argc, char *argv[])
{
    int k = 5;
    if (auto x = fork(), y = fork(); x != y)
    {
        slp(++k);
        std::cout << x << ' ' << y << '\n';
    }
    else
        slp(--k);
    printf("   \n");
    return 0;
}