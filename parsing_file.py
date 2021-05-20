import random 
from numpy.lib.format import header_data_from_array_1_0
def main():

    lines = []
    temp_list = []
    humidity_list=[]
    pressure_list = []
    number_of_sensors = 5
    sum = 0
    #mean and standard deviation
    mu = 0
    sigma = 1
    with open('scenario1_output.txt') as f:
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
                
      

                temp_list.append((temp/number_of_sensors)+random.gauss(mu, sigma))
                humidity_list.append((humidity/number_of_sensors)+random.gauss(mu, sigma))
                pressure_list.append((pressure/number_of_sensors)+random.gauss(mu, sigma))

        smallest = min(temp_list)
        largest  = max(temp_list)
        for i in temp_list :
            sum = sum + i  
        average = sum /30
        print(average)
               


main()