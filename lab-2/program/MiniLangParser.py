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
        4,1,16,70,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,0,
        11,0,12,0,13,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,3,1,31,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,40,8,2,1,2,1,
        2,1,2,1,2,1,2,1,2,5,2,48,8,2,10,2,12,2,51,9,2,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,3,3,63,8,3,1,4,1,4,1,4,1,4,1,4,1,4,0,1,4,5,
        0,2,4,6,8,0,3,1,0,8,9,1,0,10,11,1,0,4,5,75,0,11,1,0,0,0,2,30,1,0,
        0,0,4,39,1,0,0,0,6,62,1,0,0,0,8,64,1,0,0,0,10,12,3,2,1,0,11,10,1,
        0,0,0,12,13,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,1,1,0,0,0,15,
        16,3,4,2,0,16,17,5,14,0,0,17,31,1,0,0,0,18,19,5,12,0,0,19,20,5,1,
        0,0,20,21,3,4,2,0,21,22,5,14,0,0,22,31,1,0,0,0,23,31,5,14,0,0,24,
        25,5,7,0,0,25,31,5,14,0,0,26,27,3,6,3,0,27,28,5,14,0,0,28,31,1,0,
        0,0,29,31,3,8,4,0,30,15,1,0,0,0,30,18,1,0,0,0,30,23,1,0,0,0,30,24,
        1,0,0,0,30,26,1,0,0,0,30,29,1,0,0,0,31,3,1,0,0,0,32,33,6,2,-1,0,
        33,40,5,13,0,0,34,40,5,12,0,0,35,36,5,2,0,0,36,37,3,4,2,0,37,38,
        5,3,0,0,38,40,1,0,0,0,39,32,1,0,0,0,39,34,1,0,0,0,39,35,1,0,0,0,
        40,49,1,0,0,0,41,42,10,5,0,0,42,43,7,0,0,0,43,48,3,4,2,6,44,45,10,
        4,0,0,45,46,7,1,0,0,46,48,3,4,2,5,47,41,1,0,0,0,47,44,1,0,0,0,48,
        51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,5,1,0,0,0,51,49,1,0,0,
        0,52,53,3,4,2,0,53,54,5,16,0,0,54,55,3,4,2,0,55,63,1,0,0,0,56,57,
        5,2,0,0,57,58,3,4,2,0,58,59,5,16,0,0,59,60,3,4,2,0,60,61,5,3,0,0,
        61,63,1,0,0,0,62,52,1,0,0,0,62,56,1,0,0,0,63,7,1,0,0,0,64,65,7,2,
        0,0,65,66,3,6,3,0,66,67,5,6,0,0,67,68,3,2,1,0,68,9,1,0,0,0,6,13,
        30,39,47,49,62
    ]

class MiniLangParser ( Parser ):

    grammarFileName = "MiniLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "'while'", "'if'", 
                     "':'", "<INVALID>", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "COMMENT", 
                      "MUL", "DIV", "ADD", "SUB", "ID", "INT", "NEWLINE", 
                      "WS", "COMPARATOR" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_comparation = 3
    RULE_stmt = 4

    ruleNames =  [ "prog", "stat", "expr", "comparation", "stmt" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    COMMENT=7
    MUL=8
    DIV=9
    ADD=10
    SUB=11
    ID=12
    INT=13
    NEWLINE=14
    WS=15
    COMPARATOR=16

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
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.stat()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 28852) != 0)):
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



    def stat(self):

        localctx = MiniLangParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = MiniLangParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.expr(0)
                self.state = 16
                self.match(MiniLangParser.NEWLINE)
                pass

            elif la_ == 2:
                localctx = MiniLangParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.match(MiniLangParser.ID)
                self.state = 19
                self.match(MiniLangParser.T__0)
                self.state = 20
                self.expr(0)
                self.state = 21
                self.match(MiniLangParser.NEWLINE)
                pass

            elif la_ == 3:
                localctx = MiniLangParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                self.match(MiniLangParser.NEWLINE)
                pass

            elif la_ == 4:
                localctx = MiniLangParser.CommentContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 24
                self.match(MiniLangParser.COMMENT)
                self.state = 25
                self.match(MiniLangParser.NEWLINE)
                pass

            elif la_ == 5:
                localctx = MiniLangParser.ComparisonStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 26
                self.comparation()
                self.state = 27
                self.match(MiniLangParser.NEWLINE)
                pass

            elif la_ == 6:
                localctx = MiniLangParser.CondStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 29
                self.stmt()
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
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                localctx = MiniLangParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 33
                self.match(MiniLangParser.INT)
                pass
            elif token in [12]:
                localctx = MiniLangParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 34
                self.match(MiniLangParser.ID)
                pass
            elif token in [2]:
                localctx = MiniLangParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 35
                self.match(MiniLangParser.T__1)
                self.state = 36
                self.expr(0)
                self.state = 37
                self.match(MiniLangParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 49
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 47
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = MiniLangParser.MulDivContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 41
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 42
                        _la = self._input.LA(1)
                        if not(_la==8 or _la==9):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 43
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = MiniLangParser.AddSubContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 44
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 45
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 46
                        self.expr(5)
                        pass

             
                self.state = 51
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
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.expr(0)
                self.state = 53
                self.match(MiniLangParser.COMPARATOR)
                self.state = 54
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.match(MiniLangParser.T__1)
                self.state = 57
                self.expr(0)
                self.state = 58
                self.match(MiniLangParser.COMPARATOR)
                self.state = 59
                self.expr(0)
                self.state = 60
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
            self.state = 64
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 65
            self.comparation()
            self.state = 66
            self.match(MiniLangParser.T__5)
            self.state = 67
            self.stat()
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
         




