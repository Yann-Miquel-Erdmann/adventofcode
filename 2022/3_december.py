import string

score = 0
with open("2022/adventofcode.com_2022_day_3_input.txt") as f:
    lines = f.readlines()
    for i in range(0, len(lines), 3):
        for elem in lines[i][:-1]:
            if elem in lines[i+1] and elem in lines[i+2]:
                score+=string.ascii_letters.index(elem)+1
                break
    
print(score)
