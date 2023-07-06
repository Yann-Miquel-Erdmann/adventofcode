def main():
    max_y = 0
    matrix = [[ 0 for i in range(400)] for _ in range(200)]
    with open("2022/adventofcode.com_2022_day_14_input.txt") as f:
        for line in f.readlines():
            pos = list(map(lambda elem: tuple(map(int,elem.split(","))),line.strip().split(" -> ")))
            for i in range(len(pos)-1):
                if pos[i][0] == pos[i+1][0]:
                    for y in range(min(pos[i][1],pos[i+1][1]) ,max(pos[i][1] , pos[i+1][1])+1):
                        matrix[y][pos[i][0]-300] = 1
                    if max(pos[i][1] , pos[i+1][1]) > max_y:
                        max_y = max(pos[i][1] , pos[i+1][1])

                else:
                    for x in range( min(pos[i][0],pos[i+1][0]) -300,max(pos[i][0] , pos[i+1][0])+1-300):
                        matrix[pos[i][1]][x] = 1
                    
                    if pos[i][1] > max_y:
                        max_y = pos[i][1]

    matrix[max_y+2] = [1 for i in range(400)]

    print(max_y)
    count = 0
    path = [(200,0)]

    while len(path):
        print(path[-1])
        # print(path[-1], matrix[path[-1][1]+1][path[-1][0]-1:path[-1][0]+2])
        if matrix[path[-1][1]+1][path[-1][0]] == 0:
            path.append((path[-1][0], path[-1][1]+1))

        elif matrix[path[-1][1]+1][path[-1][0]-1] == 0:
            path.append((path[-1][0]-1, path[-1][1]+1))

        elif matrix[path[-1][1]+1][path[-1][0]+1] == 0:
            path.append((path[-1][0]+1, path[-1][1]+1))

        else:
            count+=1
            matrix[path[-1][1]][path[-1][0]] = 2
            path.pop()
    



    print(count)


    
if __name__ == '__main__':
    main()