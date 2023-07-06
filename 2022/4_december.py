with open("2022/adventofcode.com_2022_day_4_input.txt") as f:
    count = 0
    for line in f.readlines():
        r1,r2 = line.split(",")
        r1 = list(map(int, r1.split("-")))
        r2 = list(map(int, r2.split("-")))
        
        if r1[0]<=r2[0]<=r1[1] or r1[0]<=r2[1]<=r1[1] or r2[0]<=r1[1]<=r2[1] or r2[0]<=r1[0]<=r2[1]:
            count+=1

print(count)