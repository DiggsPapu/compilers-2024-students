%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
%}

// Define YYSTYPE
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

assignment: ID EQUAL expression
          { printf("Assign %s = %d\n", yylval.str, yyval.num); }
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

int yyerror(const char *s) {
    printf("Error: %s\n", s);
    return 0;
}
