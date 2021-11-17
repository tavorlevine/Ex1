import csv
import string

from Elevator import Elevator
from CallForElevator import CallForElevator
from Building import Building
from listCalls import listCalls
import math


class algo:

    def __init__(self, building: str, calls: str, out: str):
        # self.build = building
        # self.calls = calls
        self.output = out
        self.list = listCalls(calls)
        self.b = Building(building)
        self.allocate(self.list)

    # if __name__ == "__main__":

    #     calls = listCalls(file_name)
    #     allocate(calls)
    # if __name__ == '__main__':

    #    al.allocate(al.list)

    def allocate(self, list1: listCalls):
        for c in list1.calls:
            if self.b.count == 1:
                c.elev = 0
            else:
                time = 9999999
                tempelev = -1
                for elev in self.b.elevators:
                    if len(elev.list_c) == 0:
                        elevtime = timeFromTo(c, elev)
                        if elevtime < time:
                            time = elevtime
                            tempelev = elev.id
                    else:
                        # if elev.direction != c.direc:
                        #     if elev.id < self.b.count:
                        #         continue
                        #     else:
                        #         tempelev = elev.id
                        #         continue
                        if elev.list_c[len(elev.list_c) - 1].time + timeOneCall(elev.list_c[len(elev.list_c) - 2].dest,
                                                              elev.list_c[-1],
                                                              elev) < c.time:
                            elevtime = timeOneCall(elev.list_c[-1].dest, c, elev)
                            if elevtime < time:
                                time = elevtime
                                tempelev = elev.id
                        else:
                            list_2 = reverse_list(elev.list_c)
                            for c2 in list_2:
                                if list_2.index(c2) == (len(list_2) - 1):
                                    sumOfCall = len(elev.list_c) - elev.list_c.index(c2)
                                    elevtime = timeSumCalls(sumOfCall, c2.dest, c, elev)
                                elif c2.time + timeOneCall(list_2[list_2.index(c2) + 1].dest, c2, elev) < c.time:
                                    elevtime = timeOneCall(c2.dest, c, elev)
                                    if elevtime < time:
                                        time = elevtime
                                        tempelev = elev.id
                                    break
                                elif c2.time < c.time:
                                    sumOfCall = len(elev.list_c) - elev.list_c.index(c2)
                                    elevtime = timeSumCalls(sumOfCall, c2.dest, c, elev)
                                    if elevtime < time:
                                        time = elevtime
                                        tempelev = elev.id
                                    break
            c.elev = tempelev
            self.b.elevators[tempelev].addCalls(c)
        list1.writeToCSV(self.output)

# def allocate1 (self, list1: listCalls):
#     for c in list1.calls:
#         if (abs(c.dest - c.src) < self.b.min)


def timeFromTo(c: CallForElevator, elev: Elevator):
    # if len(elev.list_c) == 0:
    stages = abs(0 - c.src)
    stages = stages + abs(c.src - c.dest)
    elevtime = (elev.speed / stages) + elev.stopTime + elev.startTime + elev.openTime + elev.closeTime
    return elevtime


def timeOneCall(pos: int, c: CallForElevator, elev: Elevator):
    stages = abs(pos - c.src)
    stages = stages + abs(c.src - c.dest)
    elevtime = (elev.speed / stages) + elev.stopTime + elev.startTime + elev.openTime + elev.closeTime
    return elevtime


def timeSumCalls(sum_2: int, pos: int, c: CallForElevator, elev: Elevator):
    stages = abs(pos - c.getSrc())
    stages = stages + abs(c.src - c.dest)
    elevtime = (elev.speed / stages) + (elev.stopTime + elev.startTime + elev.openTime) * sum_2 + elev.closeTime * (
            sum_2 - 1)
    return elevtime
