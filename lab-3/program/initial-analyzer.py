import sys
from antlr4 import *
from ConfRoomSchedulerLexer import ConfRoomSchedulerLexer
from ConfRoomSchedulerParser import ConfRoomSchedulerParser
from ConfRoomSchedulerVisitor import ConfRoomSchedulerVisitor
def main():
    input_stream = FileStream('C:/Users/Diana/Desktop/UVG/octavo_semestre/Compis/lab3/compilers-2024-students/lab-3/program/test.confroomdsl')
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

    visitor.notify_upcoming_reservations(time_frame_minutes=30)

if __name__ == '__main__':
    main()