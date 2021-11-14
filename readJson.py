# from Elevator import Elevator
# from Bulding import Building
import json

def read_file(self, file_name):
        try:
         with open(file_name, 'r') as file:
              new_list = {}
              dict = json.load(file)
              elev_d = dict["_elevators"]
             # for k,v in elev_d.items():
             #     e=Elevator()
        except IOError as e:
            print(e)
        print(elev_d)

if __name__ == '__main__':
     print("hello")
     read_file("B1.json")
