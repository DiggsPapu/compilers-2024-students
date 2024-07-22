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
        4,1,15,85,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,4,0,16,8,0,11,0,12,0,17,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,3,1,31,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,3,2,45,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,5,1,5,4,5,79,8,5,11,5,12,5,80,1,6,1,6,1,6,0,0,7,0,2,4,6,
        8,10,12,0,1,1,0,9,10,84,0,15,1,0,0,0,2,30,1,0,0,0,4,32,1,0,0,0,6,
        46,1,0,0,0,8,58,1,0,0,0,10,76,1,0,0,0,12,82,1,0,0,0,14,16,3,2,1,
        0,15,14,1,0,0,0,16,17,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,1,1,
        0,0,0,19,20,3,4,2,0,20,21,5,14,0,0,21,31,1,0,0,0,22,23,3,6,3,0,23,
        24,5,14,0,0,24,31,1,0,0,0,25,26,3,8,4,0,26,27,5,14,0,0,27,31,1,0,
        0,0,28,31,5,14,0,0,29,31,5,1,0,0,30,19,1,0,0,0,30,22,1,0,0,0,30,
        25,1,0,0,0,30,28,1,0,0,0,30,29,1,0,0,0,31,3,1,0,0,0,32,33,5,2,0,
        0,33,34,3,12,6,0,34,35,5,13,0,0,35,36,5,3,0,0,36,37,5,13,0,0,37,
        38,5,3,0,0,38,39,5,11,0,0,39,40,5,4,0,0,40,41,5,12,0,0,41,42,5,5,
        0,0,42,44,5,12,0,0,43,45,3,10,5,0,44,43,1,0,0,0,44,45,1,0,0,0,45,
        5,1,0,0,0,46,47,5,6,0,0,47,48,3,12,6,0,48,49,5,13,0,0,49,50,5,3,
        0,0,50,51,5,13,0,0,51,52,5,3,0,0,52,53,5,11,0,0,53,54,5,4,0,0,54,
        55,5,12,0,0,55,56,5,5,0,0,56,57,5,12,0,0,57,7,1,0,0,0,58,59,5,7,
        0,0,59,60,3,12,6,0,60,61,5,13,0,0,61,62,5,3,0,0,62,63,5,13,0,0,63,
        64,5,3,0,0,64,65,5,11,0,0,65,66,5,4,0,0,66,67,5,12,0,0,67,68,5,5,
        0,0,68,69,5,12,0,0,69,70,5,5,0,0,70,71,5,11,0,0,71,72,5,4,0,0,72,
        73,5,12,0,0,73,74,5,5,0,0,74,75,5,12,0,0,75,9,1,0,0,0,76,78,5,8,
        0,0,77,79,5,13,0,0,78,77,1,0,0,0,79,80,1,0,0,0,80,78,1,0,0,0,80,
        81,1,0,0,0,81,11,1,0,0,0,82,83,7,0,0,0,83,13,1,0,0,0,4,17,30,44,
        80
    ]

class ConfRoomSchedulerParser ( Parser ):

    grammarFileName = "ConfRoomScheduler.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'LIST'", "'RESERVAR'", "'PARA'", "'DE'", 
                     "'A'", "'CANCELAR'", "'REPROGRAMAR'", "'DESCRIPCION:'", 
                     "'JUNTAS'", "'CAPACITACION'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "DATE", "TIME", 
                      "ID", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_reserve = 2
    RULE_cancel = 3
    RULE_reschedule = 4
    RULE_description = 5
    RULE_roomType = 6

    ruleNames =  [ "prog", "stat", "reserve", "cancel", "reschedule", "description", 
                   "roomType" ]

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
    T__9=10
    DATE=11
    TIME=12
    ID=13
    NEWLINE=14
    WS=15

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
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.stat()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 16582) != 0)):
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


    class RescheduleStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConfRoomSchedulerParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def reschedule(self):
            return self.getTypedRuleContext(ConfRoomSchedulerParser.RescheduleContext,0)

        def NEWLINE(self):
            return self.getToken(ConfRoomSchedulerParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRescheduleStat" ):
                listener.enterRescheduleStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRescheduleStat" ):
                listener.exitRescheduleStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRescheduleStat" ):
                return visitor.visitRescheduleStat(self)
            else:
                return visitor.visitChildren(self)


    class ListStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConfRoomSchedulerParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListStat" ):
                listener.enterListStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListStat" ):
                listener.exitListStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListStat" ):
                return visitor.visitListStat(self)
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
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = ConfRoomSchedulerParser.ReserveStatContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.reserve()
                self.state = 20
                self.match(ConfRoomSchedulerParser.NEWLINE)
                pass
            elif token in [6]:
                localctx = ConfRoomSchedulerParser.CancelStatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.cancel()
                self.state = 23
                self.match(ConfRoomSchedulerParser.NEWLINE)
                pass
            elif token in [7]:
                localctx = ConfRoomSchedulerParser.RescheduleStatContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.reschedule()
                self.state = 26
                self.match(ConfRoomSchedulerParser.NEWLINE)
                pass
            elif token in [14]:
                localctx = ConfRoomSchedulerParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 28
                self.match(ConfRoomSchedulerParser.NEWLINE)
                pass
            elif token in [1]:
                localctx = ConfRoomSchedulerParser.ListStatContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 29
                self.match(ConfRoomSchedulerParser.T__0)
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

        def roomType(self):
            return self.getTypedRuleContext(ConfRoomSchedulerParser.RoomTypeContext,0)


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

        def description(self):
            return self.getTypedRuleContext(ConfRoomSchedulerParser.DescriptionContext,0)


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
            self.state = 32
            self.match(ConfRoomSchedulerParser.T__1)
            self.state = 33
            self.roomType()
            self.state = 34
            self.match(ConfRoomSchedulerParser.ID)
            self.state = 35
            self.match(ConfRoomSchedulerParser.T__2)
            self.state = 36
            self.match(ConfRoomSchedulerParser.ID)
            self.state = 37
            self.match(ConfRoomSchedulerParser.T__2)
            self.state = 38
            self.match(ConfRoomSchedulerParser.DATE)
            self.state = 39
            self.match(ConfRoomSchedulerParser.T__3)
            self.state = 40
            self.match(ConfRoomSchedulerParser.TIME)
            self.state = 41
            self.match(ConfRoomSchedulerParser.T__4)
            self.state = 42
            self.match(ConfRoomSchedulerParser.TIME)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 43
                self.description()


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

        def roomType(self):
            return self.getTypedRuleContext(ConfRoomSchedulerParser.RoomTypeContext,0)


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
            self.state = 46
            self.match(ConfRoomSchedulerParser.T__5)
            self.state = 47
            self.roomType()
            self.state = 48
            self.match(ConfRoomSchedulerParser.ID)
            self.state = 49
            self.match(ConfRoomSchedulerParser.T__2)
            self.state = 50
            self.match(ConfRoomSchedulerParser.ID)
            self.state = 51
            self.match(ConfRoomSchedulerParser.T__2)
            self.state = 52
            self.match(ConfRoomSchedulerParser.DATE)
            self.state = 53
            self.match(ConfRoomSchedulerParser.T__3)
            self.state = 54
            self.match(ConfRoomSchedulerParser.TIME)
            self.state = 55
            self.match(ConfRoomSchedulerParser.T__4)
            self.state = 56
            self.match(ConfRoomSchedulerParser.TIME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RescheduleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def roomType(self):
            return self.getTypedRuleContext(ConfRoomSchedulerParser.RoomTypeContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ConfRoomSchedulerParser.ID)
            else:
                return self.getToken(ConfRoomSchedulerParser.ID, i)

        def DATE(self, i:int=None):
            if i is None:
                return self.getTokens(ConfRoomSchedulerParser.DATE)
            else:
                return self.getToken(ConfRoomSchedulerParser.DATE, i)

        def TIME(self, i:int=None):
            if i is None:
                return self.getTokens(ConfRoomSchedulerParser.TIME)
            else:
                return self.getToken(ConfRoomSchedulerParser.TIME, i)

        def getRuleIndex(self):
            return ConfRoomSchedulerParser.RULE_reschedule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReschedule" ):
                listener.enterReschedule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReschedule" ):
                listener.exitReschedule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReschedule" ):
                return visitor.visitReschedule(self)
            else:
                return visitor.visitChildren(self)




    def reschedule(self):

        localctx = ConfRoomSchedulerParser.RescheduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_reschedule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(ConfRoomSchedulerParser.T__6)
            self.state = 59
            self.roomType()
            self.state = 60
            self.match(ConfRoomSchedulerParser.ID)
            self.state = 61
            self.match(ConfRoomSchedulerParser.T__2)
            self.state = 62
            self.match(ConfRoomSchedulerParser.ID)
            self.state = 63
            self.match(ConfRoomSchedulerParser.T__2)
            self.state = 64
            self.match(ConfRoomSchedulerParser.DATE)
            self.state = 65
            self.match(ConfRoomSchedulerParser.T__3)
            self.state = 66
            self.match(ConfRoomSchedulerParser.TIME)
            self.state = 67
            self.match(ConfRoomSchedulerParser.T__4)
            self.state = 68
            self.match(ConfRoomSchedulerParser.TIME)
            self.state = 69
            self.match(ConfRoomSchedulerParser.T__4)
            self.state = 70
            self.match(ConfRoomSchedulerParser.DATE)
            self.state = 71
            self.match(ConfRoomSchedulerParser.T__3)
            self.state = 72
            self.match(ConfRoomSchedulerParser.TIME)
            self.state = 73
            self.match(ConfRoomSchedulerParser.T__4)
            self.state = 74
            self.match(ConfRoomSchedulerParser.TIME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DescriptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ConfRoomSchedulerParser.ID)
            else:
                return self.getToken(ConfRoomSchedulerParser.ID, i)

        def getRuleIndex(self):
            return ConfRoomSchedulerParser.RULE_description

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDescription" ):
                listener.enterDescription(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDescription" ):
                listener.exitDescription(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDescription" ):
                return visitor.visitDescription(self)
            else:
                return visitor.visitChildren(self)




    def description(self):

        localctx = ConfRoomSchedulerParser.DescriptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_description)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(ConfRoomSchedulerParser.T__7)
            self.state = 78 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 77
                self.match(ConfRoomSchedulerParser.ID)
                self.state = 80 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==13):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RoomTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ConfRoomSchedulerParser.RULE_roomType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoomType" ):
                listener.enterRoomType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoomType" ):
                listener.exitRoomType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoomType" ):
                return visitor.visitRoomType(self)
            else:
                return visitor.visitChildren(self)




    def roomType(self):

        localctx = ConfRoomSchedulerParser.RoomTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_roomType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            _la = self._input.LA(1)
            if not(_la==9 or _la==10):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





