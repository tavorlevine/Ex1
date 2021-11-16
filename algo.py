import csv
import string

from Elevator import Elevator
from CallForElevator import CallForElevator
from Building import Building
from listCalls import listCalls
import math


class algo:

    def __init__(self, building: string, calls: string, out: string):
        # self.build = building
        # self.calls = calls
        self.output = out
        self.list = listCalls(calls)
        self.b = building(building)

    # if __name__ == "__main__":
    #     alg = algo(r"C:\Users\חן שטינמץ\PycharmProjects\Ex1\data\Ex1_input\Ex1_Calls\Calls_a.csv")
    #     calls = listCalls(file_name)
    #     allocate(calls)
    # if __name__ == '__main__':
    #    al = algo(r"C:\Users\חן שטינמץ\PycharmProjects\Ex1\data\Ex1_input\Ex1_Buildings\B1.json", r"C:\Users\חן שטינמץ\PycharmProjects\Ex1\data\Ex1_input\Ex1_Calls\Calls_b.csv", r"out.csv")
    #    al.allocate(al.list)

    def allocate(self, calls: listCalls, file):
        for c in calls:
            if self.Building.count == 1:
                c.elev = 0
            else:
                time = 9999999
                tempelev = -1
                for elev in Building.elevators:
                    if elev.list_c.count() == 0:
                        elevtime = self.timeFromTo(c, elev)
                        if elevtime < time:
                            time = elevtime
                            tempelev = elev.id
                    else:
                        if elev.list_c[-1].time + self.timeOneCall(elev.list_c[len(elev.list_c) - 2].dest,
                                                                   elev.list_c[-1],
                                                                   elev) < c.time:
                            elevtime = self.timeOneCall(elev.list_c[-1].dest, c, elev)
                            if elevtime < time:
                                time = elevtime
                                tempelev = elev.id
                        else:
                            list_2 = elev.list_c.reverse
                            for c2 in list_2:
                                if c2.time + self.timeOneCall(elev.list_c[c2.id - 1].dest, c2, elev) < c.time:
                                    elevtime = self.timeOneCall(c2.dest, c, elev)
                                    if elevtime < time:
                                        time = elevtime
                                        tempelev = elev.id
                                    break
                                elif c2.time < c.time:
                                    sumOfCall = len(elev.list_c) - elev.list_c.index(c2)
                                    elevtime = self.timeSumCalls(sumOfCall, c2.dest, c, elev)
                                    if elevtime < time:
                                        time = elevtime
                                        tempelev = elev.id
                                    break
            c.elev = tempelev
        calls.writeToCSV(self.output)


def timeFromTo(self, c: CallForElevator, elev: Elevator):
    if elev.list_c.count() == 0:
        stages = abs(0 - c.src)
        stages = stages + abs(c.src - c.dest)
        elevtime = (elev.speed / stages) + elev.stopTime + elev.startTime + elev.openTime + elev.closeTime
        return elevtime


def timeOneCall(self, pos: int, c: CallForElevator, elev: Elevator):
    stages = abs(pos - c.src)
    stages = stages + abs(c.src - c.dest)
    elevtime = (elev.speed / stages) + elev.stopTime + elev.startTime + elev.openTime + elev.closeTime
    return elevtime


def timeSumCalls(self, sum_2: int, pos: int, c: CallForElevator, elev: Elevator):
    stages = abs(pos - c.getSrc())
    stages = stages + abs(c.src - c.dest)
    elevtime = (elev.speed / stages) + (elev.stopTime + elev.startTime + elev.openTime) * sum_2 + elev.closeTime * (
            sum_2 - 1)
    return elevtime
