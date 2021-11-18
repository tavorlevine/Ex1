# imports
import sys

from Elevator import Elevator
from CallForElevator import CallForElevator
from Building import Building
from listCalls import listCalls


class algo:

    # constructor
    def __init__(self, building: str, calls: str, out: str):
        # self.build = building
        # self.calls = calls
        self.output = out
        self.list = listCalls(calls)
        self.b = Building(building)
        self.allocate(self.list)

    # this function allocate elevator for each call and in the end send all the details to csv file
    def allocate(self, list1: listCalls):
        for c in list1.calls:
            if self.b.count == 1:  # if number of elevator in the building is 1
                c.elev = 0
            else:
                time = 9999999  # default max time
                tempelev = -1
                for elev in self.b.elevators:
                    if len(elev.list_c) == 0:
                        elevtime = timeFromTo(c, elev)
                        if elevtime < time:
                            time = elevtime
                            tempelev = elev.id
                    else:
                        timelastcall = elev.list_c[len(elev.list_c) - 1].time + timeOneCall(
                            elev.list_c[len(elev.list_c) - 2].dest,
                            elev.list_c[-1],
                            elev)
                        if timelastcall < c.time:
                            if (abs(elev.list_c[len(elev.list_c) - 1].dest - c.src) > 20) & (abs(c.src - c.dest)) < 10:
                                tempelev = elev.id
                                break
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
                                    if elevtime < time:
                                        time = elevtime
                                        tempelev = elev.id
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


# the function return how long does it take for the elevator from start position ( 0 flor) to the src of the first call
def timeFromTo(c: CallForElevator, elev: Elevator):
    stages = abs(0 - c.src)
    stages = stages + abs(c.src - c.dest)
    elevtime = (elev.speed / stages) + elev.stopTime + elev.startTime + elev.openTime + elev.closeTime
    return elevtime


# this function return how long does it take for elevator to make one call
# from current position until call destination
def timeOneCall(pos: int, c: CallForElevator, elev: Elevator):
    stages = abs(pos - c.src)
    stages = stages + abs(c.src - c.dest)
    elevtime = (elev.speed / stages) + elev.stopTime + elev.startTime + elev.openTime + elev.closeTime
    return elevtime


# this function returns how long does it take for the elevator to make a lot of calls
def timeSumCalls(sum_2: int, pos: int, c: CallForElevator, elev: Elevator):
    stages = abs(pos - c.getSrc())
    stages = stages + abs(c.src - c.dest)
    elevtime = (elev.speed / stages) + (elev.stopTime + elev.startTime + elev.openTime) * sum_2 + elev.closeTime * (
            sum_2 - 1)
    return elevtime


# this function returns the list in reverse order
def reverse_list(list1: []):
    list2 = []
    for i in range(len(list1)):
        list2.append(list1[-1 - i])
    return list2


# to start the algorithm
files = sys.argv
if len(files) > 3:
    b1, l1, o1 = files[1], files[2], files[3]
    algo(b1, l1, o1)


# if __name__ == "__main__":
#     b1 = r"C:\Users\tavor\PycharmProjects\Ex1\data\Ex1_input\Ex1_Buildings\B2.json"
#     l1 = r"C:\Users\tavor\PycharmProjects\Ex1\data\Ex1_input\Ex1_Calls\Calls_a.csv"
#     o1 = r"outb.csv"
#     algo(b1, l1, o1)
