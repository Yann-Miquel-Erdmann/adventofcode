
def compare(elem1,elem2):
    if type(elem1) is type(elem2) is int:
        if elem1 < elem2:
            return True
        elif elem1 > elem2:
            return False
        else:
            return None
    
    elif type(elem1) is list and  type(elem2) is list:
        for i in range(min(len(elem1), len(elem2))):
            res = compare(elem1[i], elem2[i])
            if res == True:
                return True
            elif res == False:
                return False
            
        else:
            if len(elem1) < len(elem2):
                return True
            elif len(elem1) > len(elem2):
                return False
            else:
                return None
    
    else:
        if type(elem1) == int:
            return compare([elem1], elem2)
        else:
            return compare(elem1, [elem2])
            

def main():
    with open("2022/adventofcode.com_2022_day_13_input.txt") as f:
        lines = [eval(line) for line in f.readlines() if line != "\n"]
        a = 1
        b = 2
        for line in lines:
            if compare(line,[[2]]):
                a+=1
                b+=1
            elif compare(line,[[6]]):

                
                b+=1


        print(a,b,a*b)


if __name__ == '__main__':
    main()