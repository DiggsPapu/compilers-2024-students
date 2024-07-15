# Generated from MiniLang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,19,179,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,4,0,18,8,0,11,0,12,0,19,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,39,8,1,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,3,2,49,8,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,57,8,
        2,10,2,12,2,60,9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,72,
        8,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,4,5,81,8,5,11,5,12,5,82,1,5,5,5,
        86,8,5,10,5,12,5,89,9,5,1,5,1,5,4,5,93,8,5,11,5,12,5,94,1,5,5,5,
        98,8,5,10,5,12,5,101,9,5,3,5,103,8,5,1,5,1,5,4,5,107,8,5,11,5,12,
        5,108,1,5,5,5,112,8,5,10,5,12,5,115,9,5,5,5,117,8,5,10,5,12,5,120,
        9,5,1,5,1,5,1,5,1,5,1,6,4,6,127,8,6,11,6,12,6,128,1,6,5,6,132,8,
        6,10,6,12,6,135,9,6,1,6,1,6,4,6,139,8,6,11,6,12,6,140,1,6,5,6,144,
        8,6,10,6,12,6,147,9,6,3,6,149,8,6,1,6,1,6,4,6,153,8,6,11,6,12,6,
        154,1,6,5,6,158,8,6,10,6,12,6,161,9,6,5,6,163,8,6,10,6,12,6,166,
        9,6,1,6,1,6,1,7,1,7,5,7,172,8,7,10,7,12,7,175,9,7,1,7,1,7,1,7,0,
        1,4,8,0,2,4,6,8,10,12,14,0,5,1,0,11,12,1,0,13,14,1,0,4,5,1,0,15,
        16,2,0,11,16,18,19,201,0,17,1,0,0,0,2,38,1,0,0,0,4,48,1,0,0,0,6,
        71,1,0,0,0,8,73,1,0,0,0,10,78,1,0,0,0,12,126,1,0,0,0,14,169,1,0,
        0,0,16,18,3,2,1,0,17,16,1,0,0,0,18,19,1,0,0,0,19,17,1,0,0,0,19,20,
        1,0,0,0,20,1,1,0,0,0,21,22,3,4,2,0,22,23,5,17,0,0,23,39,1,0,0,0,
        24,25,5,15,0,0,25,26,5,1,0,0,26,27,3,4,2,0,27,28,5,17,0,0,28,39,
        1,0,0,0,29,39,5,17,0,0,30,31,5,10,0,0,31,39,5,17,0,0,32,33,3,6,3,
        0,33,34,5,17,0,0,34,39,1,0,0,0,35,39,3,8,4,0,36,39,3,10,5,0,37,39,
        3,12,6,0,38,21,1,0,0,0,38,24,1,0,0,0,38,29,1,0,0,0,38,30,1,0,0,0,
        38,32,1,0,0,0,38,35,1,0,0,0,38,36,1,0,0,0,38,37,1,0,0,0,39,3,1,0,
        0,0,40,41,6,2,-1,0,41,49,5,16,0,0,42,49,5,15,0,0,43,44,5,2,0,0,44,
        45,3,4,2,0,45,46,5,3,0,0,46,49,1,0,0,0,47,49,3,14,7,0,48,40,1,0,
        0,0,48,42,1,0,0,0,48,43,1,0,0,0,48,47,1,0,0,0,49,58,1,0,0,0,50,51,
        10,6,0,0,51,52,7,0,0,0,52,57,3,4,2,7,53,54,10,5,0,0,54,55,7,1,0,
        0,55,57,3,4,2,6,56,50,1,0,0,0,56,53,1,0,0,0,57,60,1,0,0,0,58,56,
        1,0,0,0,58,59,1,0,0,0,59,5,1,0,0,0,60,58,1,0,0,0,61,62,3,4,2,0,62,
        63,5,19,0,0,63,64,3,4,2,0,64,72,1,0,0,0,65,66,5,2,0,0,66,67,3,4,
        2,0,67,68,5,19,0,0,68,69,3,4,2,0,69,70,5,3,0,0,70,72,1,0,0,0,71,
        61,1,0,0,0,71,65,1,0,0,0,72,7,1,0,0,0,73,74,7,2,0,0,74,75,3,6,3,
        0,75,76,5,6,0,0,76,77,3,2,1,0,77,9,1,0,0,0,78,80,5,7,0,0,79,81,5,
        15,0,0,80,79,1,0,0,0,81,82,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,
        87,1,0,0,0,84,86,7,3,0,0,85,84,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,
        0,87,88,1,0,0,0,88,90,1,0,0,0,89,87,1,0,0,0,90,102,5,2,0,0,91,93,
        5,15,0,0,92,91,1,0,0,0,93,94,1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,
        95,99,1,0,0,0,96,98,7,3,0,0,97,96,1,0,0,0,98,101,1,0,0,0,99,97,1,
        0,0,0,99,100,1,0,0,0,100,103,1,0,0,0,101,99,1,0,0,0,102,92,1,0,0,
        0,102,103,1,0,0,0,103,118,1,0,0,0,104,106,5,8,0,0,105,107,5,15,0,
        0,106,105,1,0,0,0,107,108,1,0,0,0,108,106,1,0,0,0,108,109,1,0,0,
        0,109,113,1,0,0,0,110,112,7,3,0,0,111,110,1,0,0,0,112,115,1,0,0,
        0,113,111,1,0,0,0,113,114,1,0,0,0,114,117,1,0,0,0,115,113,1,0,0,
        0,116,104,1,0,0,0,117,120,1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,
        0,119,121,1,0,0,0,120,118,1,0,0,0,121,122,5,3,0,0,122,123,5,6,0,
        0,123,124,3,2,1,0,124,11,1,0,0,0,125,127,5,15,0,0,126,125,1,0,0,
        0,127,128,1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,133,1,0,0,
        0,130,132,7,3,0,0,131,130,1,0,0,0,132,135,1,0,0,0,133,131,1,0,0,
        0,133,134,1,0,0,0,134,136,1,0,0,0,135,133,1,0,0,0,136,148,5,2,0,
        0,137,139,5,15,0,0,138,137,1,0,0,0,139,140,1,0,0,0,140,138,1,0,0,
        0,140,141,1,0,0,0,141,145,1,0,0,0,142,144,7,3,0,0,143,142,1,0,0,
        0,144,147,1,0,0,0,145,143,1,0,0,0,145,146,1,0,0,0,146,149,1,0,0,
        0,147,145,1,0,0,0,148,138,1,0,0,0,148,149,1,0,0,0,149,164,1,0,0,
        0,150,152,5,8,0,0,151,153,5,15,0,0,152,151,1,0,0,0,153,154,1,0,0,
        0,154,152,1,0,0,0,154,155,1,0,0,0,155,159,1,0,0,0,156,158,7,3,0,
        0,157,156,1,0,0,0,158,161,1,0,0,0,159,157,1,0,0,0,159,160,1,0,0,
        0,160,163,1,0,0,0,161,159,1,0,0,0,162,150,1,0,0,0,163,166,1,0,0,
        0,164,162,1,0,0,0,164,165,1,0,0,0,165,167,1,0,0,0,166,164,1,0,0,
        0,167,168,5,3,0,0,168,13,1,0,0,0,169,173,5,9,0,0,170,172,7,4,0,0,
        171,170,1,0,0,0,172,175,1,0,0,0,173,171,1,0,0,0,173,174,1,0,0,0,
        174,176,1,0,0,0,175,173,1,0,0,0,176,177,5,9,0,0,177,15,1,0,0,0,23,
        19,38,48,56,58,71,82,87,94,99,102,108,113,118,128,133,140,145,148,
        154,159,164,173
    ]

class MiniLangParser ( Parser ):

    grammarFileName = "MiniLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "'while'", "'if'", 
                     "':'", "'def'", "','", "'\"'", "<INVALID>", "'*'", 
                     "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "COMMENT", "MUL", "DIV", 
                      "ADD", "SUB", "ID", "INT", "NEWLINE", "WS", "COMPARATOR" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_comparation = 3
    RULE_stmt = 4
    RULE_defFun = 5
    RULE_fun = 6
    RULE_string = 7

    ruleNames =  [ "prog", "stat", "expr", "comparation", "stmt", "defFun", 
                   "fun", "string" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    COMMENT=10
    MUL=11
    DIV=12
    ADD=13
    SUB=14
    ID=15
    INT=16
    NEWLINE=17
    WS=18
    COMPARATOR=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.StatContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.StatContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = MiniLangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.stat()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 231092) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniLangParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(MiniLangParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlank" ):
                listener.enterBlank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlank" ):
                listener.exitBlank(self)


    class CommentContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COMMENT(self):
            return self.getToken(MiniLangParser.COMMENT, 0)
        def NEWLINE(self):
            return self.getToken(MiniLangParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)


    class ComparisonStmtContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def comparation(self):
            return self.getTypedRuleContext(MiniLangParser.ComparationContext,0)

        def NEWLINE(self):
            return self.getToken(MiniLangParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonStmt" ):
                listener.enterComparisonStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonStmt" ):
                listener.exitComparisonStmt(self)


    class DefunStmtContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def defFun(self):
            return self.getTypedRuleContext(MiniLangParser.DefFunContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefunStmt" ):
                listener.enterDefunStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefunStmt" ):
                listener.exitDefunStmt(self)


    class PrintExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(MiniLangParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(MiniLangParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)


    class CondStmtContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def stmt(self):
            return self.getTypedRuleContext(MiniLangParser.StmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondStmt" ):
                listener.enterCondStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondStmt" ):
                listener.exitCondStmt(self)


    class FunStmtContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def fun(self):
            return self.getTypedRuleContext(MiniLangParser.FunContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunStmt" ):
                listener.enterFunStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunStmt" ):
                listener.exitFunStmt(self)



    def stat(self):

        localctx = MiniLangParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = MiniLangParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.expr(0)
                self.state = 22
                self.match(MiniLangParser.NEWLINE)
                pass

            elif la_ == 2:
                localctx = MiniLangParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.match(MiniLangParser.ID)
                self.state = 25
                self.match(MiniLangParser.T__0)
                self.state = 26
                self.expr(0)
                self.state = 27
                self.match(MiniLangParser.NEWLINE)
                pass

            elif la_ == 3:
                localctx = MiniLangParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.match(MiniLangParser.NEWLINE)
                pass

            elif la_ == 4:
                localctx = MiniLangParser.CommentContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 30
                self.match(MiniLangParser.COMMENT)
                self.state = 31
                self.match(MiniLangParser.NEWLINE)
                pass

            elif la_ == 5:
                localctx = MiniLangParser.ComparisonStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 32
                self.comparation()
                self.state = 33
                self.match(MiniLangParser.NEWLINE)
                pass

            elif la_ == 6:
                localctx = MiniLangParser.CondStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 35
                self.stmt()
                pass

            elif la_ == 7:
                localctx = MiniLangParser.DefunStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 36
                self.defFun()
                pass

            elif la_ == 8:
                localctx = MiniLangParser.FunStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 37
                self.fun()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)

        def MUL(self):
            return self.getToken(MiniLangParser.MUL, 0)
        def DIV(self):
            return self.getToken(MiniLangParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)

        def ADD(self):
            return self.getToken(MiniLangParser.ADD, 0)
        def SUB(self):
            return self.getToken(MiniLangParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class StrExpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def string(self):
            return self.getTypedRuleContext(MiniLangParser.StringContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStrExp" ):
                listener.enterStrExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStrExp" ):
                listener.exitStrExp(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(MiniLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                localctx = MiniLangParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 41
                self.match(MiniLangParser.INT)
                pass
            elif token in [15]:
                localctx = MiniLangParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 42
                self.match(MiniLangParser.ID)
                pass
            elif token in [2]:
                localctx = MiniLangParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 43
                self.match(MiniLangParser.T__1)
                self.state = 44
                self.expr(0)
                self.state = 45
                self.match(MiniLangParser.T__2)
                pass
            elif token in [9]:
                localctx = MiniLangParser.StrExpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 47
                self.string()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 58
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 56
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = MiniLangParser.MulDivContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 50
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 51
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 52
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = MiniLangParser.AddSubContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 53
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 54
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 55
                        self.expr(6)
                        pass

             
                self.state = 60
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ComparationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)


        def COMPARATOR(self):
            return self.getToken(MiniLangParser.COMPARATOR, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_comparation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparation" ):
                listener.enterComparation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparation" ):
                listener.exitComparation(self)




    def comparation(self):

        localctx = MiniLangParser.ComparationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_comparation)
        try:
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.expr(0)
                self.state = 62
                self.match(MiniLangParser.COMPARATOR)
                self.state = 63
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.match(MiniLangParser.T__1)
                self.state = 66
                self.expr(0)
                self.state = 67
                self.match(MiniLangParser.COMPARATOR)
                self.state = 68
                self.expr(0)
                self.state = 69
                self.match(MiniLangParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparation(self):
            return self.getTypedRuleContext(MiniLangParser.ComparationContext,0)


        def stat(self):
            return self.getTypedRuleContext(MiniLangParser.StatContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = MiniLangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 74
            self.comparation()
            self.state = 75
            self.match(MiniLangParser.T__5)
            self.state = 76
            self.stat()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefFunContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self):
            return self.getTypedRuleContext(MiniLangParser.StatContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.ID)
            else:
                return self.getToken(MiniLangParser.ID, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.INT)
            else:
                return self.getToken(MiniLangParser.INT, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_defFun

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefFun" ):
                listener.enterDefFun(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefFun" ):
                listener.exitDefFun(self)




    def defFun(self):

        localctx = MiniLangParser.DefFunContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_defFun)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(MiniLangParser.T__6)

            self.state = 80 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 79
                    self.match(MiniLangParser.ID)

                else:
                    raise NoViableAltException(self)
                self.state = 82 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15 or _la==16:
                self.state = 84
                _la = self._input.LA(1)
                if not(_la==15 or _la==16):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 90
            self.match(MiniLangParser.T__1)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 92 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 91
                        self.match(MiniLangParser.ID)

                    else:
                        raise NoViableAltException(self)
                    self.state = 94 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15 or _la==16:
                    self.state = 96
                    _la = self._input.LA(1)
                    if not(_la==15 or _la==16):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 101
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 104
                self.match(MiniLangParser.T__7)

                self.state = 106 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 105
                        self.match(MiniLangParser.ID)

                    else:
                        raise NoViableAltException(self)
                    self.state = 108 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15 or _la==16:
                    self.state = 110
                    _la = self._input.LA(1)
                    if not(_la==15 or _la==16):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 115
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 121
            self.match(MiniLangParser.T__2)
            self.state = 122
            self.match(MiniLangParser.T__5)
            self.state = 123
            self.stat()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.ID)
            else:
                return self.getToken(MiniLangParser.ID, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.INT)
            else:
                return self.getToken(MiniLangParser.INT, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_fun

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFun" ):
                listener.enterFun(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFun" ):
                listener.exitFun(self)




    def fun(self):

        localctx = MiniLangParser.FunContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_fun)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 125
                    self.match(MiniLangParser.ID)

                else:
                    raise NoViableAltException(self)
                self.state = 128 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15 or _la==16:
                self.state = 130
                _la = self._input.LA(1)
                if not(_la==15 or _la==16):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 136
            self.match(MiniLangParser.T__1)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 138 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 137
                        self.match(MiniLangParser.ID)

                    else:
                        raise NoViableAltException(self)
                    self.state = 140 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15 or _la==16:
                    self.state = 142
                    _la = self._input.LA(1)
                    if not(_la==15 or _la==16):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 147
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 150
                self.match(MiniLangParser.T__7)

                self.state = 152 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 151
                        self.match(MiniLangParser.ID)

                    else:
                        raise NoViableAltException(self)
                    self.state = 154 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15 or _la==16:
                    self.state = 156
                    _la = self._input.LA(1)
                    if not(_la==15 or _la==16):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 161
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 167
            self.match(MiniLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.ID)
            else:
                return self.getToken(MiniLangParser.ID, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.INT)
            else:
                return self.getToken(MiniLangParser.INT, i)

        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.MUL)
            else:
                return self.getToken(MiniLangParser.MUL, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.WS)
            else:
                return self.getToken(MiniLangParser.WS, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.DIV)
            else:
                return self.getToken(MiniLangParser.DIV, i)

        def ADD(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.ADD)
            else:
                return self.getToken(MiniLangParser.ADD, i)

        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.SUB)
            else:
                return self.getToken(MiniLangParser.SUB, i)

        def COMPARATOR(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.COMPARATOR)
            else:
                return self.getToken(MiniLangParser.COMPARATOR, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)




    def string(self):

        localctx = MiniLangParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(MiniLangParser.T__8)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 915456) != 0):
                self.state = 170
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 915456) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 176
            self.match(MiniLangParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         




