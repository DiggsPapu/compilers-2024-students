grammar MiniLang;

prog:   stat+ ;

stat:   expr NEWLINE                       # printExpr
    |   ID '=' expr NEWLINE                # assign
    |   NEWLINE                            # blank
    |   COMMENT NEWLINE                    # commentStmt
    |   comparison NEWLINE                 # comparisonStmt
    |   defFunction NEWLINE                # defFunStmt
    |   callFunction NEWLINE               # callFunStmt
    |   statement NEWLINE                  # stmt
    ;
    
expr:   expr ('*'|'/') expr                # MulDiv
    |   expr ('+'|'-') expr                # AddSub
    |   INT                                # int
    |   ID                                 # id
    |   '(' expr ')'                       # parens
    |   string                             # stringExpr
    ;

comparison: expr COMPARATOR expr
    |   '(' expr COMPARATOR expr ')'
    ;

statement: ('while'|'if') WS comparison ':' NEWLINE (WS+ (expr|callFunction|statement) NEWLINE)* WS+(expr|callFunction|statement)
    ;

defFunction: 'def' WS ID WS* '(' WS* ID WS* (',' WS* ID WS*)* ')' ':' NEWLINE (WS+ (expr|callFunction|statement) NEWLINE)* WS+(expr|callFunction|statement)
    ;

callFunction: ID WS* '(' WS* (ID|INT) WS* (',' WS* (ID|INT) WS*)* ')'
    ;

string: '"' (ID|WS|INT|MUL|DIV|ADD|SUB)+ '"'
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
COMPARATOR : (('=' '=')|('!' '=')|(('>'|'<') '='?)); // comparators
