import sys
from antlr4 import *
from ConfRoomSchedulerLexer import ConfRoomSchedulerLexer
from ConfRoomSchedulerParser import ConfRoomSchedulerParser
from ConfRoomSchedulerVisitor import ConfRoomSchedulerVisitor
def main():
    input_stream = FileStream('/home/diggspapu/compilers-2024-students/lab-3/program/test.confroomdsl')
    lexer = ConfRoomSchedulerLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ConfRoomSchedulerParser(stream)
    tree = parser.prog()
    print(tree.toStringTree(recog=parser))
    visitor = ConfRoomSchedulerVisitor()
    visitor.visit(tree)
    print("reservations:")
    print(visitor.reservations)
    print("cancelations:")
    print(visitor.cancelations)

if __name__ == '__main__':
    main()