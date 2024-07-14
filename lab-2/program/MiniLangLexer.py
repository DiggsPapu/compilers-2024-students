# Generated from MiniLang.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,18,107,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,1,1,1,
        1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,6,
        1,6,1,7,1,7,1,8,1,8,5,8,63,8,8,10,8,12,8,66,9,8,1,9,1,9,1,10,1,10,
        1,11,1,11,1,12,1,12,1,13,4,13,77,8,13,11,13,12,13,78,1,14,4,14,82,
        8,14,11,14,12,14,83,1,15,3,15,87,8,15,1,15,1,15,1,16,4,16,92,8,16,
        11,16,12,16,93,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,3,17,104,
        8,17,3,17,106,8,17,0,0,18,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,
        9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,1,0,5,2,
        0,10,10,13,13,2,0,65,90,97,122,1,0,48,57,2,0,9,9,32,32,2,0,60,60,
        62,62,114,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,
        0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,
        0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,
        0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,1,37,1,0,0,0,3,39,1,
        0,0,0,5,41,1,0,0,0,7,43,1,0,0,0,9,49,1,0,0,0,11,52,1,0,0,0,13,54,
        1,0,0,0,15,58,1,0,0,0,17,60,1,0,0,0,19,67,1,0,0,0,21,69,1,0,0,0,
        23,71,1,0,0,0,25,73,1,0,0,0,27,76,1,0,0,0,29,81,1,0,0,0,31,86,1,
        0,0,0,33,91,1,0,0,0,35,105,1,0,0,0,37,38,5,61,0,0,38,2,1,0,0,0,39,
        40,5,40,0,0,40,4,1,0,0,0,41,42,5,41,0,0,42,6,1,0,0,0,43,44,5,119,
        0,0,44,45,5,104,0,0,45,46,5,105,0,0,46,47,5,108,0,0,47,48,5,101,
        0,0,48,8,1,0,0,0,49,50,5,105,0,0,50,51,5,102,0,0,51,10,1,0,0,0,52,
        53,5,58,0,0,53,12,1,0,0,0,54,55,5,100,0,0,55,56,5,101,0,0,56,57,
        5,102,0,0,57,14,1,0,0,0,58,59,5,44,0,0,59,16,1,0,0,0,60,64,5,35,
        0,0,61,63,8,0,0,0,62,61,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,
        1,0,0,0,65,18,1,0,0,0,66,64,1,0,0,0,67,68,5,42,0,0,68,20,1,0,0,0,
        69,70,5,47,0,0,70,22,1,0,0,0,71,72,5,43,0,0,72,24,1,0,0,0,73,74,
        5,45,0,0,74,26,1,0,0,0,75,77,7,1,0,0,76,75,1,0,0,0,77,78,1,0,0,0,
        78,76,1,0,0,0,78,79,1,0,0,0,79,28,1,0,0,0,80,82,7,2,0,0,81,80,1,
        0,0,0,82,83,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,30,1,0,0,0,85,
        87,5,13,0,0,86,85,1,0,0,0,86,87,1,0,0,0,87,88,1,0,0,0,88,89,5,10,
        0,0,89,32,1,0,0,0,90,92,7,3,0,0,91,90,1,0,0,0,92,93,1,0,0,0,93,91,
        1,0,0,0,93,94,1,0,0,0,94,95,1,0,0,0,95,96,6,16,0,0,96,34,1,0,0,0,
        97,98,5,61,0,0,98,106,5,61,0,0,99,100,5,33,0,0,100,106,5,61,0,0,
        101,103,7,4,0,0,102,104,5,61,0,0,103,102,1,0,0,0,103,104,1,0,0,0,
        104,106,1,0,0,0,105,97,1,0,0,0,105,99,1,0,0,0,105,101,1,0,0,0,106,
        36,1,0,0,0,8,0,64,78,83,86,93,103,105,1,6,0,0
    ]

class MiniLangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    COMMENT = 9
    MUL = 10
    DIV = 11
    ADD = 12
    SUB = 13
    ID = 14
    INT = 15
    NEWLINE = 16
    WS = 17
    COMPARATOR = 18

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'('", "')'", "'while'", "'if'", "':'", "'def'", "','", 
            "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "MUL", "DIV", "ADD", "SUB", "ID", "INT", "NEWLINE", 
            "WS", "COMPARATOR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "COMMENT", "MUL", "DIV", "ADD", "SUB", "ID", "INT", 
                  "NEWLINE", "WS", "COMPARATOR" ]

    grammarFileName = "MiniLang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


