import csv
from Elevator import Elevator


class CallForElevator:
    # INIT = 0
    # GOING2SRC = 1
    # GOING2DEST = 2
    # DONE = 3

    def __init__(self, time: int, src: int, dest: int, elev: int):
        # self.state = INIT
        self.time = time
        self.src = src
        self.dest = dest
        self.elev = elev
        if self.dest - self.src > 0:
            self.direc = 1
        else:
            self.direc = -1

    # def getState(self):
    #     return self.state

    def getSrc(self):
        return self.src

    def getDest(self):
        return self.dest

    def getDirec(self):
        return self.direc

    # def loadCSV(self, fileName):
    #     try:
    #         with open(fileName) as file:
    #          csvreader= csv.reader(file)
    #          for row in csvreader:
    #             c = CallForElevator(time=row[1], src=row[2], dest=row[3], elev=row[5])
    #     except IOError as e:
    #         print(e)

    def toString(self):
        st = "time:{}, src:{}, dest:{}, elevator:{}".format(self.time, self.src, self.dest, self.elev)


# if __name__ == "__main__":
#     c1 = CallForElevator.loadCSV(r"C:\Users\חן שטינמץ\PycharmProjects\Ex1\data\Ex1_Calls_case_2_a.csv")
#     print(c1.toString())
