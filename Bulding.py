import json
from Elevator import Elevator


class Building:

    # def __init__(self,minFloor: int, maxFloor: int, elevList: []):
    #     self.minFloor = d.get("_minFloor")

    def __init__(self, file_name):
        self.elevators = []
        self.count = 0
        self.load_json(file_name)

    # def __init__(self, minFloor: int, maxFloor: int, elevators: {}):
    #     self.minFloor = minFloor
    #     self.maxFloor = maxFloor
    #     self.elevators = elevators

    def load_json(self, file_name):
        try:
            with open(file_name, "r+") as f:
                my_d = json.load(f)
                elevs_list = my_d["_elevators"]
                for v in elevs_list:
                    elev = Elevator(v["_id"], v["_speed"], v["_minFloor"], v["_maxFloor"], v["_openTime"], v["_closeTime"], v["_startTime"], v["_stopTime"])
                    self.elevators.append(elev)

        except IOError as e:
            print(e)

    # def load_json(self, file_name: str): NOTE
    #     try:
    #         with open(file_name, 'r+') as file:
    #             new_list = {}
    #             dict = json.load(file)
    #
    #             elev_list = dict["_elevators"]
    #             self.minFloor = dict["_minFloor"]
    #             self.maxFloor = dict["_maxFloor"]
    #             for v in elev_list:
    #                 el = Elevator(id=v["_id"], speed=v["_speed"], minFloor=v["_minFloor"], maxFloor=v["_maxFloor"], closeTime=v["_closeTime"], openTime=v["_openTime"], startTime=v["_startTime"], stopTime=v["_stopTime"])
    #                 self.elevators.update(el.id, el)
    #                 self.count = self.count + 1
    #     except IOError as el:
    #         print(el)

    # id=v["_id"], speed=v["_speed"], minFloor=v["_minFloor"], maxFloor=v["_maxFloor"], closeTime=v["_closeTime"], openTime=v["_openTime"], startTime=v["_startTime"], stopTime=v["_stopTime"]

    # def __init__(self, name: str, minFloor: int, maxFloor: int, numberOfElevator: int, elevator: []):
    #     self.name = name
    #     self.minFloor = minFloor
    #     self.maxFooor = maxFloor
    #     self.numberOfElevator = numberOfElevator
    #     self.elevator = elevator

    # def read_json(self, file_name: str):
    #     try:
    #         new_list = {}
    #         with open(file_name, 'r') as file:
    #           dict = json.load(file)
    #           elev_d = dict["_elevators"]
    #           self.minFloor = dict["_minFloor"]
    #           self.maxFloor = dict["_maxFloor"]
    #           for k,v in dict.items():
    #              e=Elevator(v)
    #              new_list[k]= e
    #           self.elevators= elev_d
    #     except IOError as e:
    #         print(e)





    def numberOfElevator(self):
        return self.count

    def getElevator(self, i: int):
        return self.elevators.get(self, i)

    def toString(self):
        st = ""
        for elev in self.elevators:
            st += elev.toString()
        return st


if __name__ == '__main__':
    b1 = Building(r"C:\Users\tavor\PycharmProjects\Ex1\data\Ex1_input\Ex1_Buildings\B1.json")
    print(b1.toString())
    print(b1.elevators[0].speed)
