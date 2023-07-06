import sys
dico = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
        'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}





def main():
    global end, matrix, w, h

    with open("2022/adventofcode.com_2022_day_12_input.txt") as f:
        matrix = list(map(lambda elem: list(elem.strip()), f.readlines()))
        start = []
        for y, line in enumerate(matrix):
            for x, elem in enumerate(line):
                if elem == "S" or elem == "a":
                    matrix[y][x] = "a"
                    start.append((x, y))

                elif elem == "E":
                    matrix[y][x] = "z"
                    end = (x, y)

        w, h = len(matrix[0]), len(matrix)

        
        best = w*h
        for elem in start:
            dist = [[None for _ in range(w)] for _ in range(h)]
            dist[elem[1]][elem[0]] = 0
            to_visit = [elem]
            for i in range(w*h):
                if i == len(to_visit):
                    print("end")
                    break
                
                if dist[to_visit[i][1]][to_visit[i][0]] > best:
                    break


                if to_visit[i] == end:
                    print(dist[to_visit[i][1]][to_visit[i][0]])
                    if dist[to_visit[i][1]][to_visit[i][0]] < best:
                        best = dist[to_visit[i][1]][to_visit[i][0]]
                    break
                


                if to_visit[i][0]+1 != w:
                    if dist[to_visit[i][1]][to_visit[i][0]+1] is None:
                        if dico[matrix[to_visit[i][1]][to_visit[i][0]+1]] - 1 <= dico[matrix[to_visit[i][1]][to_visit[i][0]]]:
                            dist[to_visit[i][1]][to_visit[i][0]+1] = dist[to_visit[i][1]][to_visit[i][0]] + 1
                            to_visit.append((to_visit[i][0]+1,to_visit[i][1]))                            

                if to_visit[i][1]+1 != h:
                    if dist[to_visit[i][1]+1][to_visit[i][0]] is None:
                        if dico[matrix[to_visit[i][1]+1][to_visit[i][0]]] - 1 <= dico[matrix[to_visit[i][1]][to_visit[i][0]]]:
                            dist[to_visit[i][1]+1][to_visit[i][0]] = dist[to_visit[i][1]][to_visit[i][0]] + 1
                            to_visit.append((to_visit[i][0], to_visit[i][1]+1))
                
                if to_visit[i][0] != 0:
                    if dist[to_visit[i][1]][to_visit[i][0]-1] is None:
                        if dico[matrix[to_visit[i][1]][to_visit[i][0]-1]] - 1 <= dico[matrix[to_visit[i][1]][to_visit[i][0]]]:
                            dist[to_visit[i][1]][to_visit[i][0]-1] = dist[to_visit[i][1]][to_visit[i][0]] + 1
                            to_visit.append((to_visit[i][0]-1, to_visit[i][1]))
                
                if to_visit[i][1] != 0:
                    if dist[to_visit[i][1]-1][to_visit[i][0]] is None:
                        if dico[matrix[to_visit[i][1]-1][to_visit[i][0]]] - 1 <= dico[matrix[to_visit[i][1]][to_visit[i][0]]]:
                            dist[to_visit[i][1]-1][to_visit[i][0]]  = dist[to_visit[i][1]][to_visit[i][0]] + 1
                            to_visit.append((to_visit[i][0],to_visit[i][1]-1))


        print(best)
if __name__ == "__main__":
    main()
