monkeys =  [
    {"objects":[59, 74, 65, 86], "opration":lambda x:x*19,"throw":lambda x:6 if x%7 == 0 else 2 ,"count":0},
    {"objects":[62, 84, 72, 91, 68, 78, 51], "opration":lambda x:x+1,"throw":lambda x:2 if x%2 == 0 else 0,"count":0},
    {"objects":[78, 84, 96], "opration":lambda x:x+8,"throw":lambda x:6 if x%19 == 0 else 5,"count":0},
    {"objects":[97, 86], "opration":lambda x:x**2,"throw":lambda x:1 if x%3 == 0 else 0,"count":0},
    {"objects":[50], "opration":lambda x:x+6,"throw":lambda x:3 if x%13 == 0 else 1,"count":0},
    {"objects":[73, 65, 69, 65, 51], "opration":lambda x:x* 17,"throw":lambda x:4 if x%11 == 0 else 7,"count":0},
    {"objects":[69, 82, 97, 93, 82, 84, 58, 63], "opration":lambda x:x + 5,"throw":lambda x:5 if x%5 == 0 else 7,"count":0},
    {"objects":[81, 78, 82, 76, 79, 80], "opration":lambda x:x+ 3,"throw":lambda x:3 if x%17 == 0 else 4,"count":0},    
]


# monkeys =  [
#     {"objects":[79, 98], "opration":lambda x:x*19,"throw":lambda x:2 if x%23 == 0 else 3 ,"count":0},
#     {"objects":[54, 65, 75, 74], "opration":lambda x:x+6,"throw":lambda x:2 if x%19 == 0 else 0,"count":0},
#     {"objects":[79, 60, 97], "opration":lambda x:x**2,"throw":lambda x:1 if x%13 == 0 else 3,"count":0},
#     {"objects":[74], "opration":lambda x:x+3,"throw":lambda x:0 if x%17 == 0 else 1,"count":0},
# ]


for i in range(10000):
    print(i)
    for monkey in range(len(monkeys)):
        
        # print(f"{monkey=}")
        for obj in monkeys[monkey]["objects"]:
            # print(obj)
            obj = monkeys[monkey]["opration"](obj)
            obj = obj%9699690
            # print(obj)
            val = monkeys[monkey]["throw"](obj)
            # print(val)
            monkeys[val]["objects"].append(obj)
            # print()
            monkeys[monkey]["count"]+=1
        # print()
        monkeys[monkey]["objects"] = []    

scores = [elem["count"] for elem in monkeys]
print(scores)
scores.sort()
print(scores[-1]*scores[-2])