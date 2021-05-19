def main():
    
    lines = []
    
    with open('loglistener.txt') as f:
        lines = f.readlines()

        for line in lines: 
            line = line.strip("\n")
            if not(line.find("Main") != -1 or line.find("reachable") != -1 or line.find("collected") != -1):
                data = line.split("#")
                data = data[1].split(",")
                temp = float(data[0].split(": ")[1])
                humidity = data[1].split(": ")[1]
                pressure = data[2].split(": ")[1]
                print(f"temp is {temp} Humidity is {humidity} pressure is {pressure}")


main()

