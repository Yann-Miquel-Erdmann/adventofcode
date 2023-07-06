with open("2022/adventofcode.com_2022_day_6_input.txt") as f:
    text = f.read()[:-1]

    for i in range(13,len(text)):
        if len(set(text[i-14:i])) == 14:
            print(i)
            break

