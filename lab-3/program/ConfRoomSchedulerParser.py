# Generated from /program/ConfRoomScheduler.g4 by ANTLR 4.13.1
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
        4,1,12,53,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,21,8,1,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,4,2,36,8,2,11,2,12,2,37,3,2,40,8,
        2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,0,0,4,0,2,4,6,
        0,0,53,0,9,1,0,0,0,2,20,1,0,0,0,4,22,1,0,0,0,6,41,1,0,0,0,8,10,3,
        2,1,0,9,8,1,0,0,0,10,11,1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,1,
        1,0,0,0,13,14,3,4,2,0,14,15,5,11,0,0,15,21,1,0,0,0,16,17,3,6,3,0,
        17,18,5,11,0,0,18,21,1,0,0,0,19,21,5,11,0,0,20,13,1,0,0,0,20,16,
        1,0,0,0,20,19,1,0,0,0,21,3,1,0,0,0,22,23,5,1,0,0,23,24,5,10,0,0,
        24,25,5,2,0,0,25,26,5,10,0,0,26,27,5,2,0,0,27,28,5,8,0,0,28,29,5,
        3,0,0,29,30,5,9,0,0,30,31,5,4,0,0,31,39,5,9,0,0,32,35,5,5,0,0,33,
        34,5,10,0,0,34,36,5,6,0,0,35,33,1,0,0,0,36,37,1,0,0,0,37,35,1,0,
        0,0,37,38,1,0,0,0,38,40,1,0,0,0,39,32,1,0,0,0,39,40,1,0,0,0,40,5,
        1,0,0,0,41,42,5,7,0,0,42,43,5,10,0,0,43,44,5,2,0,0,44,45,5,10,0,
        0,45,46,5,2,0,0,46,47,5,8,0,0,47,48,5,3,0,0,48,49,5,9,0,0,49,50,
        5,4,0,0,50,51,5,9,0,0,51,7,1,0,0,0,4,11,20,37,39
    ]

class ConfRoomSchedulerParser ( Parser ):

    grammarFileName = "ConfRoomScheduler.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'RESERVAR'", "'PARA'", "'DE'", "'A'", 
                     "'DESCRIPCION:'", "' '", "'CANCELAR'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "DATE", "TIME", "ID", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_reserve = 2
    RULE_cancel = 3

    ruleNames =  [ "prog", "stat", "reserve", "cancel" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    DATE=8
    TIME=9
    ID=10
    NEWLINE=11
    WS=12

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
                return self.getTypedRuleContexts(ConfRoomSchedulerParser.StatContext)
            else:
                return self.getTypedRuleContext(ConfRoomSchedulerParser.StatContext,i)


        def getRuleIndex(self):
            return ConfRoomSchedulerParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ConfRoomSchedulerParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.stat()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2178) != 0)):
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
            return ConfRoomSchedulerParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConfRoomSchedulerParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(ConfRoomSchedulerParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlank" ):
                listener.enterBlank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlank" ):
                listener.exitBlank(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlank" ):
                return visitor.visitBlank(self)
            else:
                return visitor.visitChildren(self)


    class ReserveStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConfRoomSchedulerParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def reserve(self):
            return self.getTypedRuleContext(ConfRoomSchedulerParser.ReserveContext,0)

        def NEWLINE(self):
            return self.getToken(ConfRoomSchedulerParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReserveStat" ):
                listener.enterReserveStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReserveStat" ):
                listener.exitReserveStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReserveStat" ):
                return visitor.visitReserveStat(self)
            else:
                return visitor.visitChildren(self)


    class CancelStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConfRoomSchedulerParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def cancel(self):
            return self.getTypedRuleContext(ConfRoomSchedulerParser.CancelContext,0)

        def NEWLINE(self):
            return self.getToken(ConfRoomSchedulerParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCancelStat" ):
                listener.enterCancelStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCancelStat" ):
                listener.exitCancelStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCancelStat" ):
                return visitor.visitCancelStat(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = ConfRoomSchedulerParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 20
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = ConfRoomSchedulerParser.ReserveStatContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.reserve()
                self.state = 14
                self.match(ConfRoomSchedulerParser.NEWLINE)
                pass
            elif token in [7]:
                localctx = ConfRoomSchedulerParser.CancelStatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.cancel()
                self.state = 17
                self.match(ConfRoomSchedulerParser.NEWLINE)
                pass
            elif token in [11]:
                localctx = ConfRoomSchedulerParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 19
                self.match(ConfRoomSchedulerParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReserveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ConfRoomSchedulerParser.ID)
            else:
                return self.getToken(ConfRoomSchedulerParser.ID, i)

        def DATE(self):
            return self.getToken(ConfRoomSchedulerParser.DATE, 0)

        def TIME(self, i:int=None):
            if i is None:
                return self.getTokens(ConfRoomSchedulerParser.TIME)
            else:
                return self.getToken(ConfRoomSchedulerParser.TIME, i)

        def getRuleIndex(self):
            return ConfRoomSchedulerParser.RULE_reserve

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReserve" ):
                listener.enterReserve(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReserve" ):
                listener.exitReserve(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReserve" ):
                return visitor.visitReserve(self)
            else:
                return visitor.visitChildren(self)




    def reserve(self):

        localctx = ConfRoomSchedulerParser.ReserveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_reserve)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(ConfRoomSchedulerParser.T__0)
            self.state = 23
            self.match(ConfRoomSchedulerParser.ID)
            self.state = 24
            self.match(ConfRoomSchedulerParser.T__1)
            self.state = 25
            self.match(ConfRoomSchedulerParser.ID)
            self.state = 26
            self.match(ConfRoomSchedulerParser.T__1)
            self.state = 27
            self.match(ConfRoomSchedulerParser.DATE)
            self.state = 28
            self.match(ConfRoomSchedulerParser.T__2)
            self.state = 29
            self.match(ConfRoomSchedulerParser.TIME)
            self.state = 30
            self.match(ConfRoomSchedulerParser.T__3)
            self.state = 31
            self.match(ConfRoomSchedulerParser.TIME)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 32
                self.match(ConfRoomSchedulerParser.T__4)
                self.state = 35 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 33
                    self.match(ConfRoomSchedulerParser.ID)
                    self.state = 34
                    self.match(ConfRoomSchedulerParser.T__5)
                    self.state = 37 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==10):
                        break



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CancelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ConfRoomSchedulerParser.ID)
            else:
                return self.getToken(ConfRoomSchedulerParser.ID, i)

        def DATE(self):
            return self.getToken(ConfRoomSchedulerParser.DATE, 0)

        def TIME(self, i:int=None):
            if i is None:
                return self.getTokens(ConfRoomSchedulerParser.TIME)
            else:
                return self.getToken(ConfRoomSchedulerParser.TIME, i)

        def getRuleIndex(self):
            return ConfRoomSchedulerParser.RULE_cancel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCancel" ):
                listener.enterCancel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCancel" ):
                listener.exitCancel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCancel" ):
                return visitor.visitCancel(self)
            else:
                return visitor.visitChildren(self)




    def cancel(self):

        localctx = ConfRoomSchedulerParser.CancelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_cancel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(ConfRoomSchedulerParser.T__6)
            self.state = 42
            self.match(ConfRoomSchedulerParser.ID)
            self.state = 43
            self.match(ConfRoomSchedulerParser.T__1)
            self.state = 44
            self.match(ConfRoomSchedulerParser.ID)
            self.state = 45
            self.match(ConfRoomSchedulerParser.T__1)
            self.state = 46
            self.match(ConfRoomSchedulerParser.DATE)
            self.state = 47
            self.match(ConfRoomSchedulerParser.T__2)
            self.state = 48
            self.match(ConfRoomSchedulerParser.TIME)
            self.state = 49
            self.match(ConfRoomSchedulerParser.T__3)
            self.state = 50
            self.match(ConfRoomSchedulerParser.TIME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





