import datetime
class Reservation():
    def __init__(self, meetingRoom, person, initTime, finTime, description=None) -> None:
        self.meetingRoom = meetingRoom
        self.person = person
        self.initTime = initTime
        self.finTime = finTime
        self.desctiption = description
    def isThisReservation(self, reservation):
        
        return  reservation.meetingRoom == self.meetingRoom \
                and reservation.person==self.person \
                and reservation.finTime-self.finTime==datetime.timedelta(0) \
                and reservation.initTime-self.initTime==datetime.timedelta(0)