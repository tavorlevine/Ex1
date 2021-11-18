
class CallForElevator:

    # constructor
    def __init__(self, header, time: int, src: int, dest: int, parmeter: int, elev: int):
        self.header = header
        self.time = time
        self.src = src
        self.dest = dest
        self.parmeter = parmeter
        self.elev = elev

    # Getters.
    def getSrc(self):
        return self.src

    def getDest(self):
        return self.dest

    def getDirec(self):
        return self.direc

    # toString function
    def toString(self):
        st = "time:{}, src:{}, dest:{}, elevator:{}".format(self.time, self.src, self.dest, self.elev)
        return st

