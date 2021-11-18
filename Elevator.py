from CallForElevator import CallForElevator


class Elevator:

    def __init__(self, id_1: int, speed: float, minFloor: int, maxFloor: int, closeTime: float, openTime: float,
                 startTime: float, stopTime: float, index: int):
        self.id = id_1
        self.speed = speed
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.openTime = openTime
        self.closeTime = closeTime
        self.startTime = startTime
        self.stopTime = stopTime
        self.list_c = []
        # self.direct = 0
        self.index = index
        self.sum = 0

    def toString(self):
        st = "id:{}, speed:{}, minFloor:{}, maxFloor:{}, openTime:{}, closeTime:{}, startTime:{}, stopTime:{}".format(
            self.id, self.speed, self.minFloor, self.maxFloor, self.openTime, self.closeTime, self.startTime,
            self.stopTime)
        return st

    def addCalls(self, c: CallForElevator):
        self.list_c.append(c)
        self.sum = self.sum + 1
        # if len(self.list_c) == 1:
        #     self.direct = c.direc
        # if c.src < c.dest:
        #     self.direction = 1
        # else:
        #     self.direction = -1

    def getList(self):
        return self.list_c

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
