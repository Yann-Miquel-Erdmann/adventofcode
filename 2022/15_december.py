import threading


def main():

    def search(sensor):
        for y in range(- sensor[2], sensor[2]+1):

            x1, y1 = sensor[0]-sensor[2]+abs(y) ,  sensor[1]+y
            if x1 in range(0,N+1) and y1 in range(N+1):
                
                for sens in sensors:
                    if abs(x1-sens[0]) + abs(y1-sens[1]) < abs(sens[2]):
                        break
                else:
                    print(x1*4000000+ y1)

            x1 = sensor[0]+sensor[2]-abs(y) 
            if x1 in range(0,N+1) and  sensor[1]+y in range(N+1):
                for sens in sensors:
                    if abs(x1-sens[0]) + abs(y1-sens[1]) < abs(sens[2]):
                        break
                else:
                    print(x1*4000000 + y1)

    N = 4000000
    outline = set()
    sensors = set()
    counter = 0
    with open("2022/adventofcode.com_2022_day_15_input.txt") as f:
        for line in f.readlines():
            S,B = line[12:].strip().split(":")
            sensor = tuple(map(int, S.split(", y=")))
            beacon = tuple(map(int, B[24:].split(", y=")))
            diff = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])+1
            # print(sensor, beacon,diff)
            sensors.add((sensor[0], sensor[1], diff))



    for sensor in sensors:
        threading.Thread(target=search, args=[sensor,]).start()
        # search(sensor)

    print("end")


if __name__ == '__main__':
    main()