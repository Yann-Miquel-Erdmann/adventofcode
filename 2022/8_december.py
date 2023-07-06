matrix = []
with open("2022/adventofcode.com_2022_day_8_input.txt") as f:
    for line in f.readlines():
        matrix.append(list(map(int, line.strip())))

big_score = [[1 for _ in range(len(matrix[0]))] for i in range(len(matrix))]

score = [[0 for _ in range(len(matrix[0]))] for i in range(len(matrix))]
for y in range(len(matrix)):
    for x in range(len(matrix[0])):
        if x==0:
            big_score[y][x] = 0
            
        elif matrix[y][x-1] < matrix[y][x]:
            offset = 1
            while score[y][x-offset] != 0 :
                if  matrix[y][x-offset] < matrix[y][x]:
                    offset += score[y][x-offset]
                    
                else:
                    break
            score[y][x] = offset
            big_score[y][x] *= offset
            
        else:
            score[y][x] = 1
# print(score)


score = [[0 for _ in range(len(matrix[0]))] for i in range(len(matrix))]
for y in range(len(matrix)):
    for x in range(len(matrix[0])-1,-1, -1):
        if x == len(matrix[0])-1:
            big_score[y][x] = 0

        elif matrix[y][x+1] < matrix[y][x]:
            offset = 1
            while score[y][x+offset] != 0 :
                if  matrix[y][x+offset] < matrix[y][x]:
                    offset += score[y][x+offset]
                    
                else:
                    break
            score[y][x] = offset
            big_score[y][x] *= offset
            
        else:
            score[y][x] = 1
# print(score)


score = [[0 for _ in range(len(matrix[0]))] for i in range(len(matrix))]
for x in range(len(matrix[0])):
    for y in range(len(matrix)):
        if y==0:
            big_score[y][x] = 0

        elif matrix[y-1][x] < matrix[y][x]:
            offset = 1
            while score[y-offset][x] != 0 :
                if  matrix[y-offset][x] < matrix[y][x]:
                    offset += score[y-offset][x]
                    
                else:
                    break
            score[y][x] = offset
            big_score[y][x] *= offset
            
        else:
            score[y][x] = 1
# print(score)
    
    

    
score = [[0 for _ in range(len(matrix[0]))] for i in range(len(matrix))]   
for x in range(len(matrix[0])):
    for y in range(len(matrix)-1,-1,-1):
        if y == len(matrix)-1:
            big_score[y][x] = 0
        elif matrix[y+1][x] < matrix[y][x]:
            offset = 1
            while score[y+offset][x] != 0 :
                if  matrix[y+offset][x] < matrix[y][x]:
                    offset += score[y+offset][x]
                    
                else:
                    break
            score[y][x] = offset
            big_score[y][x] *= offset
            
        else:
            score[y][x] = 1
# print(score)
    
    



 




        







print(max(map(max, big_score)))
# print(big_score)