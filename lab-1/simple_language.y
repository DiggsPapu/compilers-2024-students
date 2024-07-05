%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
%}

// Define YYSTYPE
%union {
    char* str;
    int num;
    int lastOp;
}

// Token declarations
%token <num> NUMBER
%token <str> ID
%token PLUS MINUS MULTIPLY DIVIDE EQUAL ENTER

%%

program: statement_list ENTER
        ;

statement_list: statement
              | statement_list statement
              ;

statement: assignment
         | expression
         ;

assignment: ID EQUAL expression
        { 
            printf("Assign %s =", $1);
            printf(" %d\n", yylval.num);
        }
          ;

expression: NUMBER
          | ID
          | expression PLUS expression
          | expression MINUS expression
          | expression MULTIPLY expression
          | expression DIVIDE expression
          ;

%%

int main() {
    yyparse();
    return 0;
}

void yyerror(const char *str) {
    fprintf(stderr, "error: %s\n", str);
}
