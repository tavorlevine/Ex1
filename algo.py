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
            for elev in Building.elevators:
                if elev.list_c.count() == 0:

                else:


    self.writeToCSV(calls.file)

def timeFromTo(self, c: CallForElevator, elev: Elevator):
    if elev.list_c.count() == 0
        stages= math.(c.src-c.dest)
        return ()

