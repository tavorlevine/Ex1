# imports
import csv
from CallForElevator import CallForElevator


class listCalls:

    # constructor
    def __init__(self, file_name):
        self.count = 0
        self.calls = []
        self.file = file_name
        self.loadCSV(self.file)

    # this function load the csv file
    def loadCSV(self, fileName):
        cl = []
        try:
            with open(fileName) as file:
                csvreader = csv.reader(file)
                for row in csvreader:
                    c = CallForElevator(header=row[0], time=float(row[1]), src=int(row[2]), dest=int(row[3]),
                                        parmeter=int(row[4]), elev=int(row[5]))
                    cl.append(c)
                    self.count = self.count + 1
                self.calls = cl
        except IOError as e:
            print(e)

    # this function write to the out file the data from the allocate function
    def writeToCSV(self, out):
        new_calls = []
        for team in self.calls:
            new_calls.append(team.__dict__.values())
        try:
            with open(out, 'w', newline="") as file:
                csvwriter = csv.writer(file)
                csvwriter.writerows(new_calls)
        except IOError as e:
            print(e)

