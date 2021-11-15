import csv
from Elevator import Elevator
from CallForElevator import CallForElevator
from Building import Building

class listCalls:

    def __init__(self, file_name):
        self.count = 0
        self.calls = []
        self.file = file_name
        self.loadCSV(self.file)

    def loadCSV(self, fileName):
        # rows = []
        cl = []
        try:
            with open(fileName) as file:
                csvreader = csv.reader(file)
                for row in csvreader:
                    c = CallForElevator(time=row[1], src=row[2], dest=row[3], elev=row[5])
                    cl.append(c)
                    # rows.append(row)
                    self.count = self.count + 1
                self.calls = cl
        except IOError as e:
            print(e)

    def writeToCSV(self, fileName):
        new_calls = []
        for team in self.calls:
            new_calls.append(team.__dict__.values())
        try:
            with open(fileName, 'w', newline="") as file:
                csvwriter= csv.writer(file)
                csvwriter.writerows(new_calls)
        except IOError as e:
            print(e)

    # def allocate(self, calls: listCalls, file):
    #     for c in calls:
    #         if self.Building.count == 1:
    #             c.elev = 0
    #         else:
    #             for elev in Building.elevators:
    #
    #
    #
    #     self.writeToCSV(calls.file)
