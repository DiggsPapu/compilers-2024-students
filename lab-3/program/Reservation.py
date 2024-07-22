import datetime

class Reservation:
    def __init__(self, meetingRoom, roomType, person, initTime, finTime, description=None) -> None:
        self.meetingRoom = meetingRoom
        self.roomType = roomType
        self.person = person
        self.initTime = initTime
        self.finTime = finTime
        self.description = description

    def isThisReservation(self, reservation):
        return (reservation.meetingRoom == self.meetingRoom and
                reservation.roomType == self.roomType and
                reservation.person == self.person and
                reservation.finTime - self.finTime == datetime.timedelta(0) and
                reservation.initTime - self.initTime == datetime.timedelta(0))
