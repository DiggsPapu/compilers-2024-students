# Generated from /program/ConfRoomScheduler.g4 by ANTLR 4.13.1
import datetime
from Reservation import Reservation
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
    
    
    # Visit a parse tree produced by ConfRoomSchedulerParser#listStat.
    def visitListStat(self, ctx:ConfRoomSchedulerParser.ListStatContext):
        keys = self.reservations.keys()
        for key in keys:
            reservations = self.reservations[key]
            for index in range(0,len(reservations)):
                reservation = reservations[index]
                print(f"reservation #{index}:\n     meeting room: {reservation.meetingRoom}\n     person: {reservation.person}\n    time: {reservation.initTime}-{reservation.finTime}\n    description: {reservation.description}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConfRoomSchedulerParser#reserve.
    def visitReserve(self, ctx:ConfRoomSchedulerParser.ReserveContext):
        meetRoom = ctx.ID(0).getText()
        person = ctx.ID(1).getText()
        date = ctx.DATE().getText().split("/")
        initTime = ctx.TIME(0).getText().split(":")
        finTime = ctx.TIME(1).getText().split(":")
        description = None
        if ctx.getChildCount()==11:
            description = ctx.getChild(10).getText()
        reservation = Reservation(
            meetRoom,
            person, 
            datetime.datetime(year=int(date[2]),month=int(date[1]),day=int(date[0]),hour=int(initTime[0]),minute=int(initTime[1])), 
            datetime.datetime(year=int(date[2]),month=int(date[1]),day=int(date[0]),hour=int(finTime[0]),minute=int(finTime[1])),
            description
            )
        rangeHours = reservation.finTime-reservation.initTime
        if rangeHours>datetime.timedelta(hours=0):
            # Person is the ID
            # time restriction
            if datetime.timedelta(hours=0)<rangeHours<=datetime.timedelta(hours=5):
                reservations = self.reservations.get(person)
                if reservations == None:
                    print(f"Made reservation: {ctx.getText()}")
                    self.reservations[person] = [reservation] 
                else:
                    # Check availability
                    for posRes in reservations:
                        if datetime.timedelta(0) <= posRes.finTime-posRes.initTime <= reservation.finTime-reservation.initTime:
                            print(f"Can't make reservation (not availability): {ctx.getText()}")
                        else: 
                            print(f"Made reservation: {ctx.getText()}")
                            self.reservations[person].append(reservation)
            else:
                print(f"Can't make reservation (reservation more than 5 hours long): {ctx.getText()}")
        else:
            print(f"Can't make reservation (reservation hours doesn't make sense): {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConfRoomSchedulerParser#cancel.
    def visitCancel(self, ctx:ConfRoomSchedulerParser.CancelContext):
        meetRoom = ctx.ID(0).getText()
        person = ctx.ID(1).getText()
        date = ctx.DATE().getText().split("/")
        initTime = ctx.TIME(0).getText().split(":")
        finTime = ctx.TIME(1).getText().split(":")
        reservation = Reservation(
            meetRoom,
            person, 
            datetime.datetime(year=int(date[2]),month=int(date[1]),day=int(date[0]),hour=int(initTime[0]),minute=int(initTime[1])), 
            datetime.datetime(year=int(date[2]),month=int(date[1]),day=int(date[0]),hour=int(finTime[0]),minute=int(finTime[1]))
            )
        # Check si existe la reservacion para la persona
        reservations = self.reservations.get(person)
        if reservations != None:
            for index in range(0, len(reservations)):
                posRes = reservations[index]
                # Misma reservacion
                if posRes.isThisReservation(reservation):    
                    if self.cancelations.get(person)==None:
                        self.cancelations[person] = [self.reservations[person].pop(index)]
                    else:
                        self.cancelations[person].append(self.reservations[person].pop(index)) 
                    print(f'Cancel reservation: {ctx.getText()}')
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by ConfRoomSchedulerParser#description.
    def visitDescription(self, ctx:ConfRoomSchedulerParser.DescriptionContext):
        return self.visitChildren(ctx)



del ConfRoomSchedulerParser