#include <stdio.h>
#include "scan.h"
#include "globals.h"

int main(int argc, char* args[]){
    FILE* f = fopen("sample.tny", "r");
    Token token;
    token.length=0; //TODO change to initial funtion
    if (f != NULL) {
      getToken(token, f);
      printf("token:%s\n", token.str);
    }
    return 0;
}
