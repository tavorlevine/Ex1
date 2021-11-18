
class CallForElevator:

    def __init__(self, header, time: int, src: int, dest: int, parmeter: int, elev: int):
        self.header = header
        self.time = time
        self.src = src
        self.dest = dest
        self.parmeter = parmeter
        self.elev = elev
        # self. direc = 0

    # def getState(self):
    #     return self.state
    # def direction(self):
        # if self.dest - self.src > 0:
        #     self.direc = 1
        # else:
        #     self.direc = -1

    def getSrc(self):
        return self.src

    def getDest(self):
        return self.dest

    def getDirec(self):
        return self.direc

    def toString(self):
        st = "time:{}, src:{}, dest:{}, elevator:{}".format(self.time, self.src, self.dest, self.elev)
        return st

