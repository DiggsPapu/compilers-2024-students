import sys
from antlr4 import *
from MiniLangLexer import *
from MiniLangParser import *
from MiniLangListener import *

def main(argv):
    input_stream = FileStream('program/program_test.txt')
    lexer = MiniLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiniLangParser(stream)
    tree = parser.prog()  # We are using 'prog' since this is the starting rule based on our MiniLang grammar, yay!
    listener = MiniLangListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    
if __name__ == '__main__':
    main(sys.argv)
