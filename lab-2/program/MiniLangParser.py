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
        4,1,18,105,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,4,0,16,8,0,11,0,12,0,17,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,39,8,1,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,3,2,48,8,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,56,8,2,10,
        2,12,2,59,9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,71,8,3,
        1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,5,5,84,8,5,10,5,12,5,
        87,9,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,5,6,98,8,6,10,6,12,6,
        101,9,6,1,6,1,6,1,6,0,1,4,7,0,2,4,6,8,10,12,0,3,1,0,10,11,1,0,12,
        13,1,0,4,5,112,0,15,1,0,0,0,2,38,1,0,0,0,4,47,1,0,0,0,6,70,1,0,0,
        0,8,72,1,0,0,0,10,77,1,0,0,0,12,92,1,0,0,0,14,16,3,2,1,0,15,14,1,
        0,0,0,16,17,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,1,1,0,0,0,19,
        20,3,4,2,0,20,21,5,16,0,0,21,39,1,0,0,0,22,23,5,14,0,0,23,24,5,1,
        0,0,24,25,3,4,2,0,25,26,5,16,0,0,26,39,1,0,0,0,27,39,5,16,0,0,28,
        29,5,9,0,0,29,39,5,16,0,0,30,31,3,6,3,0,31,32,5,16,0,0,32,39,1,0,
        0,0,33,39,3,8,4,0,34,35,3,10,5,0,35,36,5,16,0,0,36,39,1,0,0,0,37,
        39,3,12,6,0,38,19,1,0,0,0,38,22,1,0,0,0,38,27,1,0,0,0,38,28,1,0,
        0,0,38,30,1,0,0,0,38,33,1,0,0,0,38,34,1,0,0,0,38,37,1,0,0,0,39,3,
        1,0,0,0,40,41,6,2,-1,0,41,48,5,15,0,0,42,48,5,14,0,0,43,44,5,2,0,
        0,44,45,3,4,2,0,45,46,5,3,0,0,46,48,1,0,0,0,47,40,1,0,0,0,47,42,
        1,0,0,0,47,43,1,0,0,0,48,57,1,0,0,0,49,50,10,5,0,0,50,51,7,0,0,0,
        51,56,3,4,2,6,52,53,10,4,0,0,53,54,7,1,0,0,54,56,3,4,2,5,55,49,1,
        0,0,0,55,52,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,
        5,1,0,0,0,59,57,1,0,0,0,60,61,3,4,2,0,61,62,5,18,0,0,62,63,3,4,2,
        0,63,71,1,0,0,0,64,65,5,2,0,0,65,66,3,4,2,0,66,67,5,18,0,0,67,68,
        3,4,2,0,68,69,5,3,0,0,69,71,1,0,0,0,70,60,1,0,0,0,70,64,1,0,0,0,
        71,7,1,0,0,0,72,73,7,2,0,0,73,74,3,6,3,0,74,75,5,6,0,0,75,76,3,2,
        1,0,76,9,1,0,0,0,77,78,5,7,0,0,78,79,3,4,2,0,79,80,5,2,0,0,80,85,
        5,14,0,0,81,82,5,8,0,0,82,84,5,14,0,0,83,81,1,0,0,0,84,87,1,0,0,
        0,85,83,1,0,0,0,85,86,1,0,0,0,86,88,1,0,0,0,87,85,1,0,0,0,88,89,
        5,3,0,0,89,90,5,6,0,0,90,91,3,2,1,0,91,11,1,0,0,0,92,93,3,4,2,0,
        93,94,5,2,0,0,94,99,5,14,0,0,95,96,5,8,0,0,96,98,5,14,0,0,97,95,
        1,0,0,0,98,101,1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,102,1,0,
        0,0,101,99,1,0,0,0,102,103,5,3,0,0,103,13,1,0,0,0,8,17,38,47,55,
        57,70,85,99
    ]

class MiniLangParser ( Parser ):

    grammarFileName = "MiniLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "'while'", "'if'", 
                     "':'", "'def'", "','", "<INVALID>", "'*'", "'/'", "'+'", 
                     "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "COMMENT", "MUL", "DIV", "ADD", "SUB", 
                      "ID", "INT", "NEWLINE", "WS", "COMPARATOR" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_comparation = 3
    RULE_stmt = 4
    RULE_defFun = 5
    RULE_fun = 6

    ruleNames =  [ "prog", "stat", "expr", "comparation", "stmt", "defFun", 
                   "fun" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    COMMENT=9
    MUL=10
    DIV=11
    ADD=12
    SUB=13
    ID=14
    INT=15
    NEWLINE=16
    WS=17
    COMPARATOR=18

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
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.stat()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 115380) != 0)):
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

        def NEWLINE(self):
            return self.getToken(MiniLangParser.NEWLINE, 0)

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
                self.state = 19
                self.expr(0)
                self.state = 20
                self.match(MiniLangParser.NEWLINE)
                pass

            elif la_ == 2:
                localctx = MiniLangParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.match(MiniLangParser.ID)
                self.state = 23
                self.match(MiniLangParser.T__0)
                self.state = 24
                self.expr(0)
                self.state = 25
                self.match(MiniLangParser.NEWLINE)
                pass

            elif la_ == 3:
                localctx = MiniLangParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.match(MiniLangParser.NEWLINE)
                pass

            elif la_ == 4:
                localctx = MiniLangParser.CommentContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 28
                self.match(MiniLangParser.COMMENT)
                self.state = 29
                self.match(MiniLangParser.NEWLINE)
                pass

            elif la_ == 5:
                localctx = MiniLangParser.ComparisonStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 30
                self.comparation()
                self.state = 31
                self.match(MiniLangParser.NEWLINE)
                pass

            elif la_ == 6:
                localctx = MiniLangParser.CondStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 33
                self.stmt()
                pass

            elif la_ == 7:
                localctx = MiniLangParser.DefunStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 34
                self.defFun()
                self.state = 35
                self.match(MiniLangParser.NEWLINE)
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
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                localctx = MiniLangParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 41
                self.match(MiniLangParser.INT)
                pass
            elif token in [14]:
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
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 57
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 55
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = MiniLangParser.MulDivContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 49
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 50
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 51
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = MiniLangParser.AddSubContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 52
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 53
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 54
                        self.expr(5)
                        pass

             
                self.state = 59
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
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.expr(0)
                self.state = 61
                self.match(MiniLangParser.COMPARATOR)
                self.state = 62
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.match(MiniLangParser.T__1)
                self.state = 65
                self.expr(0)
                self.state = 66
                self.match(MiniLangParser.COMPARATOR)
                self.state = 67
                self.expr(0)
                self.state = 68
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
            self.state = 72
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 73
            self.comparation()
            self.state = 74
            self.match(MiniLangParser.T__5)
            self.state = 75
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

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.ID)
            else:
                return self.getToken(MiniLangParser.ID, i)

        def stat(self):
            return self.getTypedRuleContext(MiniLangParser.StatContext,0)


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
            self.state = 77
            self.match(MiniLangParser.T__6)
            self.state = 78
            self.expr(0)
            self.state = 79
            self.match(MiniLangParser.T__1)
            self.state = 80
            self.match(MiniLangParser.ID)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 81
                self.match(MiniLangParser.T__7)
                self.state = 82
                self.match(MiniLangParser.ID)
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88
            self.match(MiniLangParser.T__2)
            self.state = 89
            self.match(MiniLangParser.T__5)
            self.state = 90
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

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.ID)
            else:
                return self.getToken(MiniLangParser.ID, i)

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
            self.state = 92
            self.expr(0)
            self.state = 93
            self.match(MiniLangParser.T__1)
            self.state = 94
            self.match(MiniLangParser.ID)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 95
                self.match(MiniLangParser.T__7)
                self.state = 96
                self.match(MiniLangParser.ID)
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 102
            self.match(MiniLangParser.T__2)
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
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




