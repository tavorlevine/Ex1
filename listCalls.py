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
                    c = CallForElevator(header=row[0], time=float(row[1]), src=int(row[2]), dest=int(row[3]), parmeter=int(row[4]), elev=int(row[5]))
                    cl.append(c)
                    # rows.append(row)
                    self.count = self.count + 1
                self.calls = cl
                for i in self.calls:
                    print(i.toString())
        except IOError as e:
            print(e)

    def writeToCSV(self):
        new_calls = []
        for team in self.calls:
            new_calls.append(team.__dict__.values())
        try:
            with open("out.csv", 'w', newline="") as file:
                csvwriter = csv.writer(file)
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


if __name__ == '__main__':
    l1 = listCalls(r"C:\Users\חן שטינמץ\PycharmProjects\Ex1\data\Ex1_input\Ex1_Calls\Calls_b.csv")
    # print(l1)
    l1.calls[0].elev = 23
    l1.writeToCSV()

