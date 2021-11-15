import csv
from Elevator import Elevator
from CallForElevator import CallForElevator
from Building import Building
from listCalls import listCalls
import math


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
                        tempelev= elev.id
                else:
                    if elev.list_c[-1].time + self.timeOneCall(elev.list_c[len(elev.list_c) -2].dest, elev.list_c[-1], elev) < c.time:
                        elevtime = self.timeOneCall(elev.list_c[-1].dest, c, elev)
                        if elevtime < time:
                            time = elevtime
                            tempelev = elev.id


    calls.writeToCSV(calls.file)

def timeFromTo(self,pos, c: CallForElevator, elev: Elevator):
    if elev.list_c.count() == 0:
        stages = abs(0 - c.src)
        stages = stages + abs(c.src-c.dest)
        elevtime= (elev.speed/stages) + elev.stopTime + elev.startTime + elev.openTime + elev.closeTime
        return elevtime

def timeOneCall(self,pos, c: CallForElevator, elev: Elevator):
        stages = abs(pos - c.src)
        stages = stages + abs(c.src-c.dest)
        elevtime= (elev.speed/stages) + elev.stopTime + elev.startTime + elev.openTime + elev.closeTime
        return elevtime
