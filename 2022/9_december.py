T = [0,0]
H = [0,0]
pos = [[0,0] for _ in range(10)]
visited = set([(0,0)])

def show():
    with open("2022/test.txt", "a") as f:
        for y in range(15,-12, -1):
            for x in range(-10, 15):
                for i, elem in enumerate(pos):
                    if elem == [x,y]:
                        f.write(str(i))
                        break
                else:
                    if x==0 and y==0:
                        f.write("s")
                    else:
                        f.write(".")
            f.write("\n")
        f.write("\n\n")        

with open("2022/adventofcode.com_2022_day_9_input.txt") as f:
    for line in f.readlines():
        direction, steps = line.strip().split()
        for _ in range(int(steps)):
            if direction == "R":
                pos[0][0] +=1
            elif direction == "L":
                pos[0][0] -=1
            elif direction == "U":
                pos[0][1] +=1
            elif direction == "D":
                pos[0][1] -=1
            
            for i in range(1,10):
                if 1< abs(pos[i-1][0] - pos[i][0]) or 1< abs(pos[i-1][1] - pos[i][1]):
                    if abs(pos[i-1][0] - pos[i][0]) < abs(pos[i-1][1] - pos[i][1]):
                        pos[i][0] = pos[i-1][0]
                        if pos[i-1][1] - pos[i][1]>0:
                            pos[i][1] += pos[i-1][1] - pos[i][1] -1
                        else:
                            pos[i][1] += pos[i-1][1] - pos[i][1] +1

                    elif abs(pos[i-1][0] - pos[i][0]) == abs(pos[i-1][1] - pos[i][1]):
                        
                        if pos[i-1][0] - pos[i][0]>0:
                            pos[i][0] += pos[i-1][0] - pos[i][0] -1
                        else:
                            pos[i][0] += pos[i-1][0] - pos[i][0] +1
                        
                        if pos[i-1][1] - pos[i][1]>0:
                            pos[i][1] += pos[i-1][1] - pos[i][1] -1
                        else:
                            pos[i][1] += pos[i-1][1] - pos[i][1] +1
                        
                    else:
                        pos[i][1] = pos[i-1][1]
                        if pos[i-1][0] - pos[i][0]>0:
                            pos[i][0] += pos[i-1][0] - pos[i][0] -1
                        else:
                            pos[i][0] += pos[i-1][0] - pos[i][0] +1
                            
            # show()

            visited.add(tuple(pos[9]))

# print(visited)
print(len(visited))
