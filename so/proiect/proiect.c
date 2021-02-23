#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <stdbool.h>
#include <time.h>
#include <stdint.h>

struct proc_node {
    pid_t pid;
    pid_t ppid;
    pid_t* children_pids;
    int children_count;
    time_t time;
    uid_t user_id;
};

bool check_if_exists(pid_t pid)
{
    int exists = syscall(122,pid,0);
    if(exists < 0)
	return false;
    return true;
}

void afiseaza(struct proc_node *p, int level) {
 printf("======== %d =========\n", level);
 printf("PID ---------- %d\n", p->pid);
 printf("PPID --------- %d\n", p->ppid);
 printf("Nr copii ----- %d\n", p->children_count);
 printf("System time -- %jd\n", (intmax_t)p->time);
 printf("User ID ------ %d\n", p->user_id);
 printf("====================\n");
 printf("\n");
}
void dfs(pid_t pid, pid_t ppid, int level)
{
   if(check_if_exists(pid) == false)
	return;

  // aloc memorie pt proces nou
    struct proc_node *p = (struct proc_node*) malloc(sizeof(struct 
proc_node));

   int nr_copii = syscall(334,pid);
   if (nr_copii < 0) return;
   p->children_count = nr_copii;
   p->children_pids = (pid_t*)malloc(sizeof(pid_t) * nr_copii);
   p->pid = pid;
   p->ppid = ppid;

   int result = syscall(333,pid,p);

   if(result < 0) {
   printf("Procesul nu mai exista\n");
   return;
   }
   
   afiseaza(p,level);

   int i=0;
   for(i=0;i< nr_copii;i++) {
	dfs(p->children_pids[i],pid,level+1);
   }

  free(p->children_pids);
  free(p);

}
   
   
int main(int argc, char** argv) 
{
    pid_t root_pid = atoi(argv[1]);
    if(check_if_exists(root_pid) == false)
	{
	printf("Procesul nu exista\n\n");
	return 0;
	}
    printf("exista\n");
    dfs(root_pid, -1, 0);
}
