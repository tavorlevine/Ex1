# imports
import json
from Elevator import Elevator


class Building:

    # constructor
    def __init__(self, file_name):
        self.elevators = []
        self.count = 0
        self.load_json(file_name)

    # this function read the Json file
    def load_json(self, file_name):
        try:
            with open(file_name, "r+") as f:
                my_d = json.load(f)
                elevs_list = my_d["_elevators"]
                i = 0
                for v in elevs_list:
                    elev = Elevator(v["_id"], v["_speed"], v["_minFloor"], v["_maxFloor"], v["_openTime"],
                                    v["_closeTime"], v["_startTime"], v["_stopTime"], i)
                    self.elevators.append(elev)
                    i = i + 1
                self.count = i
        except IOError as e:
            print(e)

    # Getters
    def numberOfElevator(self):
        return self.count

    def getElevator(self, i: int):
        return self.elevators.get(self, i)

    # toString function
    def toString(self):
        st = ""
        for elev in self.elevators:
            st += elev.toString()
        return st

