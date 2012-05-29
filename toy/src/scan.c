#include <stdio.h>
#include <ctype.h>
#include "globals.h"
#include "scan.h"


/* a buffer for read characters*/
static const int BUF_SIZE = 256;
static char buf[BUF_SIZE];
static int bufLength = 0;
static int bufPos = 0;

static int getNextChar(FILE* f){
  if (bufPos < bufLength){
    return buf[bufPos++];
  } else {
    bufLength = fread(buf, 1, BUF_SIZE, f);
    if (bufLength > 0) {
      bufPos = 0;
      return buf[bufPos++];
    } else {
      return EOF;
    }
  }
}

static int unGetChar() {
  bufPos--;
  return bufPos;
}

static int endProcess(Token& token, int ch, TokenType type) {
  token.str[token.length++] = (char)ch;
  token.type = type;
  return -1;
}

static int startState(Token& token, int ch){
  switch (ch) {
    case '+' : return endProcess(token, ch, PLUS);
    case '-' : return endProcess(token, ch, MINUS);
    case '*' : return endProcess(token, ch, PRODUCT);
    case '/' : return endProcess(token, ch, DIVIDE);
    case '=' : return endProcess(token, ch, ASSIGN);
    case '<' : return endProcess(token, ch, LOWER_THAN);
    case '>' : return endProcess(token, ch, GREATER_THAN);
    case '(' : return endProcess(token, ch, LEFT_PARENTHESIS);
    case ')' : return endProcess(token, ch, RIGHT_PARENTHESIS);
    case ';' : return endProcess(token, ch, SEMICOLON);
    case -1 :
      token.type = END_OF_FILE; 
      return -1;
    default:
      if (isdigit(ch)) {
        token.type = DIGIT;
        token.str[token.length++] = ch;
        return 1;
      } else if (isalpha(ch)) {
        token.type = ID;
        token.str[token.length++] = ch;
        return 2;
      } else if (ch == '{') {
 //       token[token.length++] = ch;
        token.type = ANNOTATION;
        return 3;
      } else if (ch == ':') {
        token.type = ASSIGN;
        token.str[token.length++] = ch;
        return 4;
      }
  }
}

static int digitState (TokenType& token, char ch) {
  if (isdigit(ch)){
    token[token.length++] = ch;
    return 1;
  } else {
    unGetChar();
    return -1;
  }
}

static int wordState (TokenType& token, char ch) {
  if (isalnum(ch)) {
    token.str[token.length++] = ch;
    return 1;
  } else {
    unGetChar();
    return -1;
  }
}

static int annotationState(TokenType& token, char ch) { 
  if (ch == '}') {
    return -1;
  } else {
    token.str[token.length++] = ch;
    return 3;
  }
}

static int assignState(TokenType& token, char ch) {
  if (ch == '=') {
    token.str[token.length++] = ch;
    return -1;
  } else {
    ungetChar();
    token.type = ERROR;
    return -1;
  }
}

int (*stateFunctions[4])(Token& , char ) = {stateState, digitState, wordState, annotationState, assignState};

TokenType getToken(Token& token, FILE* f){
  int state = 0;
  int ch;
  while (state != -1) {
    ch = getNextChar(f);
    stateFunctions[state](token, ch);
  }
  return startState(token, (char)ch);
}
