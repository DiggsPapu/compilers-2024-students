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
%type <num> expression
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
          | expression PLUS expression {$$ = $1 + $3;printf("%d+%d=%d\n",$1,$3,$$);}
          | expression MINUS expression {$$ = $1 - $3;printf("%d-%d=%d\n",$1,$3,$$);}
          | expression MULTIPLY expression {$$ = $1 * $3;printf("%d*%d=%d\n",$1,$3,$$);}
          | expression DIVIDE expression {$$ = $1 / $3;printf("%d/%d=%f\n",$1,$3,$$);}
          ;

%%

int main() {
    yyparse();
    return 0;
}

void yyerror(const char *str) {
    fprintf(stderr, "error: %s\n", str);
}
