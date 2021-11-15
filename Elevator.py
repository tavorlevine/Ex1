from CallForElevator import CallForElevator


class Elevator:
    # id = 0
    # minFloor = 0
    # maxFloor = 0
    # timeForOpen = 0
    # timeForClose = 0
    # speed = 0
    # startTime = 0
    # stopTime = 0
    def __init__(self, id_1: int, speed: float, minFloor: int, maxFloor: int, closeTime: float, openTime: float, startTime: float, stopTime: float):
        self.id = id_1
        self.speed = speed
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.openTime = openTime
        self.closeTime = closeTime
        #self.pos = pos
        #self.state = state
        self.startTime = startTime
        self.stopTime = stopTime
        self.list_c = []

    def toString(self):
        st = "id:{}, speed:{}, minFloor:{}, maxFloor:{}, openTime:{}, closeTime:{}, startTime:{}, stopTime:{}".format(self.id, self.speed, self.minFloor, self.maxFloor, self.openTime, self.closeTime, self.startTime, self.stopTime)
        return st

    def addCalls(self, c: CallForElevator):
        self.list_c.__add__(c)

    def getTimeForOpen(self):
        return self.openTime

    def getTimeForClose(self):
        return self.closeTime

    def getSpeed(self):
        return self.speed

    def getStartTime(self):
        return self.startTime

    def getStopTime(self):
        return self.stopTime

    def getId(self):
        return self.id
