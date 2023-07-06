import time, sys
def main():
    global bestTimeLeft, best_score,count
    
    def search(name1,name2,tour, opened, time_left, visited_1, points, points_derive):
        global bestTimeLeft, best_score,count
        
        if all(opened):
            # print(time_left)
            if time_left> bestTimeLeft:
                bestTimeLeft = time_left
                best_score = points
            return points+(points_derive* (time_left-1))

        if time_left <= 0:
            return points


        if tour:
            name = name1
            pts = points

        else:
            pts = points + points_derive
            name = name2

        if time_left <= bestTimeLeft and points <= best_score:
            return 0

        if (min(name1,name2),max(name1,name2),*opened) in visited_points.keys():
            pt, tm = visited_points[(min(name1,name2),max(name1,name2),*opened)]
            if tm >= time_left and pt>= pts:
                return 0
            elif tm < time_left and pt< pts:
                if (min(name1,name2),max(name1,name2),*opened,tm) in pos.keys():
                    count[2]+=1
                    del pos[(min(name1,name2),max(name1,name2),*opened,tm)]

        visited_points[(min(name1,name2),max(name1,name2),*opened)] = (pts, time_left)



        if (min(name1,name2),max(name1,name2)) in visited_1.keys():
            count[0]+=1
            if visited_1[(min(name1,name2),max(name1,name2))] == hash(tuple(opened)):
                return 0


        if (min(name1,name2),max(name1,name2),*opened,time_left) in pos.keys():
            count[1]+=1
            return pos[(min(name1,name2),max(name1,name2),*opened,time_left)]
            
        best = 0

        visited = visited_1.copy()
        visited[min(name1,name2),max(name1,name2)] = hash(tuple(opened))

        if name in openable_valves.keys():
            if not opened[openable_valves[name][0]]:
                opened2 = opened[:]
                opened2[openable_valves[name][0]] = True
                
                best = search(name1,name2,not tour, opened2, time_left-int(tour),visited, pts, points_derive + openable_valves[name][1])
                
        
        
        for tunnel in valves[name]:
            if tour:
                val = search(tunnel,name2,not tour, opened, time_left-int(tour),visited, pts, points_derive)
            else:
                val = search(name1,tunnel,not tour, opened, time_left-int(tour),visited, pts, points_derive)

            if val >= best:
                best = val

        
        pos[(min(name1,name2),max(name1,name2),*opened,time_left)] = best

        return best



    def optimize_graph(node,visited):
        print(node,visited)
        if len(visited) and node in openable_valves.keys():
            return {node: len(visited)}
        
        visited2 = visited.copy()
        visited2.add(node)
        rep = {}
        for n in valves[node]:
            if n not in visited:
                res = optimize_graph(n, visited2)
                for key in res.keys():
                    if key in rep.keys():
                        if res[key] >  rep[key]:
                            rep[key] = res[key]
        
                    else:
                        rep[key] = res[key]
        return rep

            


    pos = {}
    visited_points = {}
    valves = {
    }
    valves_optimized = {}
    count = [0,0,0]
    bestTimeLeft = 0
    best_score = 0
    openable_cout = 0
    openable_valves = {}
    best_derive = 0
    with open("2022/adventofcode.com_2022_day_16_input.txt") as f:
        for line in f.readlines():
            name = line[6:8]
            flow, line = line[23:].split(";")
            tunnels = list(map(lambda x: x.strip() , line[23:].strip("\n").split(", ")))

            if int(flow):
                openable_valves[name] = (openable_cout, int(flow))
                openable_cout+=1
                best_derive+=int(flow)
            
            valves[name] = tunnels

    valves_optimized["AA"] =[(key,value) for key, value in optimize_graph("AA",set()).items()]
    for key in openable_valves.keys():
        valves_optimized[key] =[(key,value) for key, value in optimize_graph(key,set()).items()]

    print(valves_optimized)


    # t = time.perf_counter()
    # print(search("AA","AA", False, [False for _ in range(len(openable_valves))],26, {}, 0,0))
    # print((time.perf_counter()-t))
    # print(len(pos), len(visited_points))
    # print(sys.getsizeof(pos))
    # print(count)

if __name__ == '__main__':
    main()