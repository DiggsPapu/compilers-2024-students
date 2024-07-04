%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
%}

%union {
    char *str;
    int num;
}

%token NUMBER
%token ID
%token PLUS MINUS MULTIPLY DIVIDE EQUAL ENTER

%%

program: statement_list
        ;

statement_list: statement
              | statement_list statement
              ;

statement: assignment
         | expression
         ;

assignment: ID EQUAL expression ENTER
          { printf("Assign %s = %d\n", &yylval.str, yylval.num); }
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
void yyerror(const char *str)
{
        fprintf(stderr,"error: %s\n",str);
}
