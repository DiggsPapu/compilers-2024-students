import datetime
from Reservation import Reservation
from antlr4 import *
if "." in __name__:
    from .ConfRoomSchedulerParser import ConfRoomSchedulerParser
else:
    from ConfRoomSchedulerParser import ConfRoomSchedulerParser

class ConfRoomSchedulerVisitor(ParseTreeVisitor):
    def __init__(self) -> None:
        self.reservations = {}
        self.cancelations = {}
        
    def visitProg(self, ctx:ConfRoomSchedulerParser.ProgContext):
        return self.visitChildren(ctx)

    def visitReserveStat(self, ctx:ConfRoomSchedulerParser.ReserveStatContext):
        return self.visitChildren(ctx)

    def visitCancelStat(self, ctx:ConfRoomSchedulerParser.CancelStatContext):
        return self.visitChildren(ctx)

    def visitRescheduleStat(self, ctx:ConfRoomSchedulerParser.RescheduleStatContext):
        return self.visitChildren(ctx)

    def visitBlank(self, ctx:ConfRoomSchedulerParser.BlankContext):
        return self.visitChildren(ctx)
    
    def visitListStat(self, ctx:ConfRoomSchedulerParser.ListStatContext):
        keys = self.reservations.keys()
        for key in keys:
            reservations = self.reservations[key]
            for index in range(len(reservations)):
                reservation = reservations[index]
                print(f"reservation #{index}:\n     meeting room: {reservation.meetingRoom}\n     type: {reservation.roomType}\n     person: {reservation.person}\n    time: {reservation.initTime}-{reservation.finTime}\n    description: {reservation.description}")
        return self.visitChildren(ctx)

    def visitReserve(self, ctx:ConfRoomSchedulerParser.ReserveContext):
        roomType = ctx.roomType().getText()
        meetRoom = ctx.ID(0).getText()
        person = ctx.ID(1).getText()
        date = ctx.DATE().getText().split("/")
        initTime = ctx.TIME(0).getText().split(":")
        finTime = ctx.TIME(1).getText().split(":")
        description = None
        if ctx.description() is not None:
            description = ctx.description().getText()
        reservation = Reservation(
            meetRoom,
            roomType,
            person, 
            datetime.datetime(year=int(date[2]), month=int(date[1]), day=int(date[0]), hour=int(initTime[0]), minute=int(initTime[1])), 
            datetime.datetime(year=int(date[2]), month=int(date[1]), day=int(date[0]), hour=int(finTime[0]), minute=int(finTime[1])),
            description
        )
        rangeHours = reservation.finTime - reservation.initTime
        if rangeHours > datetime.timedelta(hours=0):
            if datetime.timedelta(hours=0) < rangeHours <= datetime.timedelta(hours=5):
                reservations = self.reservations.get(person)
                if reservations is None:
                    print(f"Made reservation: {ctx.getText()}")
                    self.reservations[person] = [reservation]
                else:
                    available = True
                    for posRes in reservations:
                        if not (posRes.finTime <= reservation.initTime or posRes.initTime >= reservation.finTime):
                            available = False
                            break
                    if available:
                        print(f"Made reservation: {ctx.getText()}")
                        self.reservations[person].append(reservation)
                    else:
                        print(f"Can't make reservation (not available): {ctx.getText()}")
            else:
                print(f"Can't make reservation (reservation more than 5 hours long): {ctx.getText()}")
        else:
            print(f"Can't make reservation (reservation hours don't make sense): {ctx.getText()}")
        return self.visitChildren(ctx)

    def visitCancel(self, ctx:ConfRoomSchedulerParser.CancelContext):
        roomType = ctx.roomType().getText()
        meetRoom = ctx.ID(0).getText()
        person = ctx.ID(1).getText()
        date = ctx.DATE().getText().split("/")
        initTime = ctx.TIME(0).getText().split(":")
        finTime = ctx.TIME(1).getText().split(":")
        reservation = Reservation(
            meetRoom,
            roomType,
            person, 
            datetime.datetime(year=int(date[2]), month=int(date[1]), day=int(date[0]), hour=int(initTime[0]), minute=int(initTime[1])), 
            datetime.datetime(year=int(date[2]), month=int(date[1]), day=int(date[0]), hour=int(finTime[0]), minute=int(finTime[1]))
        )
        reservations = self.reservations.get(person)
        if reservations is not None:
            for index in range(len(reservations)):
                posRes = reservations[index]
                if posRes.isThisReservation(reservation):
                    if self.cancelations.get(person) is None:
                        self.cancelations[person] = [self.reservations[person].pop(index)]
                    else:
                        self.cancelations[person].append(self.reservations[person].pop(index))
                    print(f'Cancel reservation: {ctx.getText()}')
                    break
        return self.visitChildren(ctx)

    def visitDescription(self, ctx:ConfRoomSchedulerParser.DescriptionContext):
        return self.visitChildren(ctx)

    def visitReschedule(self, ctx:ConfRoomSchedulerParser.RescheduleContext):
        roomType = ctx.roomType().getText()
        meetRoom = ctx.ID(0).getText()
        person = ctx.ID(1).getText()
        
        # Current reservation details
        current_date = ctx.DATE(0).getText().split("/")
        current_initTime = ctx.TIME(0).getText().split(":")
        current_finTime = ctx.TIME(1).getText().split(":")
        
        # New reservation details
        new_date = ctx.DATE(1).getText().split("/")
        new_initTime = ctx.TIME(2).getText().split(":")
        new_finTime = ctx.TIME(3).getText().split(":")
        
        current_reservation = Reservation(
            meetRoom,
            roomType,
            person,
            datetime.datetime(year=int(current_date[2]), month=int(current_date[1]), day=int(current_date[0]), hour=int(current_initTime[0]), minute=int(current_initTime[1])),
            datetime.datetime(year=int(current_date[2]), month=int(current_date[1]), day=int(current_date[0]), hour=int(current_finTime[0]), minute=int(current_finTime[1]))
        )
        
        new_reservation = Reservation(
            meetRoom,
            roomType,
            person,
            datetime.datetime(year=int(new_date[2]), month=int(new_date[1]), day=int(new_date[0]), hour=int(new_initTime[0]), minute=int(new_initTime[1])),
            datetime.datetime(year=int(new_date[2]), month=int(new_date[1]), day=int(new_date[0]), hour=int(new_finTime[0]), minute=int(new_finTime[1]))
        )
        
        # Check if current reservation exists
        reservations = self.reservations.get(person)
        if reservations is not None:
            for index in range(len(reservations)):
                posRes = reservations[index]
                if posRes.isThisReservation(current_reservation):
                    # Remove current reservation
                    removed_reservation = self.reservations[person].pop(index)
                    
                    # Add new reservation
                    if self.is_available(meetRoom, new_reservation):
                        print(f"Reprogrammed reservation: {ctx.getText()}")
                        self.reservations[person].append(new_reservation)
                    else:
                        print(f"Can't reprogram reservation (not available): {ctx.getText()}")
                    break
            else:
                print(f"Original reservation not found: {ctx.getText()}")
        else:
            print(f"No reservations found for {person}: {ctx.getText()}")
        return self.visitChildren(ctx)

    def is_available(self, meetRoom, new_reservation):
        for person, reservations in self.reservations.items():
            for reservation in reservations:
                if reservation.meetingRoom == meetRoom:
                    if not (reservation.finTime <= new_reservation.initTime or reservation.initTime >= new_reservation.finTime):
                        return False
        return True

    def notify_upcoming_reservations(self, time_frame_minutes=30):
        current_time = datetime.datetime.now()
        notify_before = current_time + datetime.timedelta(minutes=time_frame_minutes)
        for person, reservations in self.reservations.items():
            for reservation in reservations:
                if current_time <= reservation.initTime <= notify_before:
                    print(f"Upcoming reservation for {person}: {reservation.description} in {reservation.meetingRoom} ({reservation.roomType}) from {reservation.initTime} to {reservation.finTime}")
