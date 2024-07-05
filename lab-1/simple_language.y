%{
#include <stdio.h>
#include <ctype.h>
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

program: statement_list
        ;

statement_list: statement {printf("\n");}
              | statement_list statement
              ;

statement: assignment  {printf("\n");}
         | expression  {printf("\n");}
         ;

assignment: ID EQUAL expression
        { 
            printf("Assign %s = %d\n", $1, $3);
        }
          ;

expression: NUMBER
          | ID
          | expression PLUS expression {$$ = $1 + $3;printf("%d+%d=%d ",$1,$3,$$);}
          | expression MINUS expression {$$ = $1 - $3;printf("%d-%d=%d ",$1,$3,$$);}
          | expression MULTIPLY expression {$$ = $1 * $3;printf("%d*%d=%d ",$1,$3,$$);}
          | expression DIVIDE expression {$$ = $1 / $3;printf("%d/%d=%f ",$1,$3,$$);}
          ;

%%

int main() {
    yyparse();
    return 0;
}

void yyerror(const char *str) {
    extern char* yytext;
    fprintf(stderr, "error: %s\ninvalid token: %s", str, yytext);
}
