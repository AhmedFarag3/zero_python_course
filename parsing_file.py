import numpy as np
from numpy.lib.format import header_data_from_array_1_0
def main():
    
    lines = []
    iteration_list = []
    temp_list = []
    humidity_list=[]
    pressure_list = []
    
    with open('loglistener.txt') as f:
        lines = f.readlines()

        for line in lines: 
            line = line.strip("\n")
            if not(line.find("Main") != -1 or line.find("reachable") != -1 or line.find("collected") != -1):
                data = line.split("#")
                data = data[1].split(",")
                listtostring = ' '.join([str(element) for (element) in data])
                listtostring = listtostring.split(" ")

                iteration_number = int(listtostring[0])
                temp     = float(listtostring[2])
                humidity = float(listtostring[5])
                pressure = float(listtostring[8])
                iteration_list.append(iteration_number)
                temp_list.append(temp)
                humidity_list.append(humidity)
                pressure_list.append(pressure)      
                print(temp_list)
                #print(f"iteration_number is : {iteration_number} temp is {temp} Humidity is {humidity}  pressure is {pressure}")


main()