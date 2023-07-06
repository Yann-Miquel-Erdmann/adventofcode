register = 1
counter = 0
signal_s = 0
def cycle():
    global register,counter,signal_s
    if (counter)%40 in [register-1,register, register+1]:
        print("#",end="")
    else:
        print(".", end="")
    
    counter+=1

    if counter%40 == 0:
        print()
        
    
    

with open("2022/adventofcode.com_2022_day_10_input.txt") as f:
    for line in f.readlines():
        if line[0] == "n":
            cycle()
        else:
            cycle()
            cycle()
            register+=int(line.strip().split()[1])


