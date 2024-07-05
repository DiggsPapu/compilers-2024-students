%{
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "simple_language.tab.h"
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
{ID}        {   const char* original = yytext;
                yylval.str = strdup(original);
                return ID; 
            }
{NUMBER}    {   
                yylval.num = atoi(yytext); return NUMBER; }
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
