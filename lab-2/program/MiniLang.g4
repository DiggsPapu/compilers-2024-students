grammar MiniLang;

prog:   stat+ ;

stat:   expr NEWLINE                 # printExpr
    |   ID '=' expr NEWLINE          # assign
    |   NEWLINE                      # blank
    |   COMMENT NEWLINE              # comment
    |   comparation NEWLINE          # comparisonStmt
    |   stmt                         # condStmt
    |   defFun                       # defunStmt
    |   fun                          # funStmt
    ;
    
expr:   expr ('*'|'/') expr          # MulDiv
    |   expr ('+'|'-') expr          # AddSub
    |   INT                          # int
    |   ID                           # id
    |   '(' expr ')'                 # parens
    |   string                       # strExp
    ;

comparation: expr COMPARATOR expr
    |   '(' expr COMPARATOR expr ')'
    ;

stmt: ('while'|'if') comparation ':' stat
    ;

defFun: 'def' (ID+ (INT|ID)*) '(' (ID+ (INT|ID)*)? ( ',' (ID+ (INT|ID)*) )* ')' ':' stat
    ;

fun: (ID+ (INT|ID)*) '(' (ID+ (INT|ID)*)? ( ',' (ID+ (INT|ID)*) )* ')'
    ;

string: '"' (ID|INT|MUL|WS|DIV|ADD|SUB|COMPARATOR)* '"'
    ;

COMMENT : '#' ~[\r\n]* ; // define token for comments
MUL : '*' ; // define token for multiplication
DIV : '/' ; // define token for division
ADD : '+' ; // define token for addition
SUB : '-' ; // define token for subtraction
ID  : [a-zA-Z]+ ; // match identifiers
INT : [0-9]+ ; // match integers
NEWLINE : '\r'? '\n' ; // return newlines to parser (is end-statement signal)
WS  : [ \t]+ -> skip ; // toss out whitespace
COMPARATOR : (('=''=')|('!''=')|(('>'|'<')'='?)); // comparators
