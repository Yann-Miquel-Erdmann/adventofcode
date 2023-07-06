listes = [[] for _ in range(9)]
with open("2022/adventofcode.com_2022_day_5_input.txt") as f:   
    for _ in range(8):
        line = f.readline()
        for i in range(9):
            if line[(i*4)+1].isalpha():
                listes[i].insert(0,line[(i*4)+1] )

    print(listes)    
    f.readline()
    f.readline()
    a = f.readline()
    while a:
        lst = a.split(" ")
        num, start, end = int(lst[1]), int(lst[3]), int(lst[5])
        for i in range(num):
            listes[end-1].append(listes[start-1][-num+i])
        for i in range(num):
            listes[start-1].pop()
        a = f.readline()
    
    print(listes)
    for liste in listes:
        if len(liste):
            print(liste[-1], end="")
    print()