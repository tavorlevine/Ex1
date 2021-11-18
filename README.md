# Ex1
In this project we went to implement an offline algorithm that receives a list of calls to elevator and returns an update list that any call in the list receives the best elevator for her. 
In the process, we made a research and read the following articles:
1.https://www.cs.huji.ac.il/~ai/projects/2014/The_intelevator/files/report.pdf 

2.https://www.geeksforgeeks.org/smart-elevator-pro-geek-cup 

3.https://thesai.org/Downloads/Volume10No2/Paper_3-Smart_Buildings_Elevator_with_Intelligent_Control.pdf

In order to write the algorithm we have implemented several classes:
### Building: 
this class recieve name of a json file and according to this json we create the building.
this class contain the methods: *load_json- read the json file. *numberOfElevator- return the sum of the elevator in the building. *getElevator- return a specific elevator. *toString.  
### Elevator:
contain the methods: *toString, *addCalls- add a new call to this elevator’s list of calls. *getList- return the elevator’s list of calls. *getTimeForOpen- return the elevator’s open time. *getTimeForClose- return the elevator’s close time. *getSpeed- return the elevator’s speed. *getTimeForStart- return the elevator’s start time. *getTimeForStop- return the elevator’s stop time. *getID- return the elevator’s id.
### CallForElevator: 
this object is exactly one call. this class contain the methods: *getSrc- return the call’s source. *getDest- return the call’s destination. *toString. 
### listCalls: 
this object receives a csv file name and loads him into a list that contains CallForElevator objects. this class contain the methods: *loadCSV- this function reads the csv file and creates the list of CallForElevator. *writeCSV-  this function writes the listCall to a new csv file.
### algo: 
this is the class of the algorithm. this class contain the methods: *allocate- pass over all the listCalls and set for any call the best elevator to her. *timeFromTo- calculate the work time of the elevator when she exits from floor 0 and go to the call’s source floor. *timeOneCall-  calculate the work time of the elevator when she exits from her current position and go to the call’s destination floor through the call’s source floor. *timeSumCalls- calculate the work time of the elevator when she exits from her current position and do few calls and also the calls that we sent for the function. *reverse_list- this function receive a list and creates this kist in reverse.   

the algorithm receive 3 strings that contain files name: 
1. json file that contains the building. 
2. csv file that contains the list of calls.
3. output file of csv kind.

The “init” function on the “algo” class receives all the 3 strings and creates a building and listCalls. in addition, this function calls for an allocate function that sets to the any call elevator’s id.
Let's detail how the allocate function works:
The function receives a listCalls object. We pass over all the calls. If we have in the building just one elevator- this is the best elevator. Otherwise, we pass over all the elevators in the building, and we try to find the best elevator. If the current elevator does not have any calls that we are already set to her- we send the call and the elevator to the timeFromTo function. Otherwise, we locate the last call that her end/start time is lower than the start time of the current call, and we send the call, the elevator and the current position of the elevator to the function timeOneCall/timeSumCalls to calculate the time work of the elevator.
In the end of the ‘for’ loop on the elevator we send to the call the elevator with the best time work. In the end of the ‘for’ loop on the calls we call the function “writeCSV” and write the updated list.
