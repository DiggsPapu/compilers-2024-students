# Generated from /program/ConfRoomScheduler.g4 by ANTLR 4.13.1
import datetime
from antlr4 import *
if "." in __name__:
    from .ConfRoomSchedulerParser import ConfRoomSchedulerParser
else:
    from ConfRoomSchedulerParser import ConfRoomSchedulerParser

# This class defines a complete generic visitor for a parse tree produced by ConfRoomSchedulerParser.

class ConfRoomSchedulerVisitor(ParseTreeVisitor):
    def __init__(self) -> None:
        self.reservations = {}
        self.cancelations = {}
        
    # Visit a parse tree produced by ConfRoomSchedulerParser#prog.
    def visitProg(self, ctx:ConfRoomSchedulerParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConfRoomSchedulerParser#reserveStat.
    def visitReserveStat(self, ctx:ConfRoomSchedulerParser.ReserveStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConfRoomSchedulerParser#cancelStat.
    def visitCancelStat(self, ctx:ConfRoomSchedulerParser.CancelStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConfRoomSchedulerParser#blank.
    def visitBlank(self, ctx:ConfRoomSchedulerParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConfRoomSchedulerParser#reserve.
    def visitReserve(self, ctx:ConfRoomSchedulerParser.ReserveContext):
        meetRoom = ctx.ID().getText()
        date = ctx.DATE().getText().split("/")
        initTime = ctx.TIME(0).getText().split(":")
        finTime = ctx.TIME(1).getText().split(":")
        self.reservations[f'{meetRoom}({ctx.TIME(0).getText()}-{ctx.TIME(1).getText()})'] = {
        "meetingRoom":meetRoom,
        "initTime":datetime.datetime(year=int(date[2]),month=int(date[1]),day=int(date[0]),hour=int(initTime[0]),minute=int(initTime[1])),
        "finTime":datetime.datetime(year=int(date[2]),month=int(date[1]),day=int(date[0]),hour=int(finTime[0]),minute=int(finTime[1])),
        }
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConfRoomSchedulerParser#cancel.
    def visitCancel(self, ctx:ConfRoomSchedulerParser.CancelContext):
        meetRoom = ctx.ID().getText()
        id = f'{meetRoom}({ctx.TIME(0).getText()}-{ctx.TIME(1).getText()})'
        if self.reservations.get(id) != None:
                self.cancelations[id] = self.reservations.pop(id)
        return self.visitChildren(ctx)



del ConfRoomSchedulerParser