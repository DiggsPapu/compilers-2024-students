%{
#include <stdlib.h>
#include <string.h>
#include "y.tab.h"
%}

ID [a-zA-Z][a-zA-Z0-9]*
NUMBER [0-9]+
PLUS "+"
MINUS "-"
MULTIPLY "*"
DIVIDE "/"
EQUAL "="
ENTER "\n"
TAB [ \t]

%%
{ID}        { yylval = strdup(yytext); return ID; }
{NUMBER}    { yylval = atoi(yytext); return NUMBER; }
{PLUS}      { return PLUS; }
{MINUS}     { return MINUS; }
{MULTIPLY}  { return MULTIPLY; }
{DIVIDE}    { return DIVIDE; }
{EQUAL}     { return EQUAL; }
{ENTER}     { return ENTER; }
{TAB}       ;  // skip whitespace

.         { return yytext[0]; }

%%

int yywrap(void) {
    return 1;
}
