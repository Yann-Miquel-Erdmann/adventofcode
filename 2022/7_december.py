def counter(dico):
    global dir_sizes
    size = 0
    for elem in dico.values():
        if type(elem) is int:
            size+=elem
        else:
            size+=counter(elem)
    

    dir_sizes.append(size)
    return size

dico = {"/":{}}
path = []
dir_sizes = []
with open("2022/adventofcode.com_2022_day_7_input.txt") as f:
    for lines in f.readlines():
        line = lines.strip()
        if line[:4] == "$ cd":
            if line[5:] == "..":
                path.pop()
            else:
                path.append(line[5:])

        elif line[:4] == "$ ls":
            continue

        elif line[0].isnumeric():
            temp = dico
            for elem in path:
                temp = temp[elem] 
            
            file_size, name = line.split(" ")
            temp[name] = int(file_size)
        else:
            temp = dico
            for elem in path:
                temp = temp[elem]
            file_size, name = line.split(" ")
            temp[name] = {}



libre = 70000000 - counter(dico)
dir_sizes.sort()
print(libre, dir_sizes)
for elem in dir_sizes:
    if libre + elem >= 30000000:
        print(elem)
        break
