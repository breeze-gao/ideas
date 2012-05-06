#ifndef GLOBALS_H_
#define GLOBALS_H_

#define MAX_TOKEN_LENGTH (256)

typedef enum{
  //state tokens
  END_OF_FILE, ERROR,
  //identifier
  ID,
  //reserved words
  IF, THEN, ELSE, END, REPEAT, UNTIL, READ, WRITE,
  //special symbols
  ASSIGN, EQUAL, LOWRE_THAN, GREATER_THAN, PLUS, MINUS, PRODUCT, DIVIDE,
  LEFT_PARANTHESIS, RIGHT_PARENTHESIS,SEMICOLON
}TokenType;

typedef struct{
  char str[MAX_TOKEN_LENGTH];
  int length = 0;
  TokenType type;
}Token;

#endif
