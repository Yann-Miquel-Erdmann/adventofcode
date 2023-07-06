top = [0,0,0]
with open("2022/adventofcode.com_2022_day_1_input.txt" , "r") as f:
    val = 0
    for elem in f.readlines():
        if elem == "\n":
            # print(val)
            if val > top[2]:
                top.pop()
                if val > top[0]:
                    top.insert(0,val)
                elif val > top[1]:
                    top.insert(1,val)
                else:
                    top.append(val)
            
            val = 0

                    
        else:

            val += int(elem)
        

print(len(top))
print(sum(top))