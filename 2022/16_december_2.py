import time
def main():
    
    def generateAllBinaryStrings(n, arr, i):
        if i == n:
            # print(arr)
            arrangements.append(arr[:])
            return

        arr[i] = 0
        generateAllBinaryStrings(n, arr, i + 1)


        arr[i] = 1
        generateAllBinaryStrings(n, arr, i + 1)


    def search(name,to_visit,time_left, score):
        best = 0
        if len(to_visit) == 0:
            return score
        for elem in to_visit:
            if dist[name][elem]+1 < time_left:
                t = tuple(elt for elt in to_visit if elt != elem)
                count[0]+=1
                if (elem,t,time_left-dist[name][elem]-1) in pos.keys():
                    res = pos[(elem,t,time_left-dist[name][elem]-1)]
                    count[1]+=1

                else:
                    res = search(elem,
                    t,
                    time_left-dist[name][elem]-1, 
                    (time_left-dist[name][elem]-1)*flows[elem])

                if res > best:
                    best = res


        pos[(name,to_visit,time_left)] = best+score
        return best+score



            
    def adjacence_matrix(dico):

        matrix = [[INF for _ in range(N)] for _ in range(N)]
        for key,elem in sorted(dico.items(), key=lambda val:val[0]):  # ! sorted pas sur
            matrix[indice[key]][indice[key]] = 0
            for tunnel in elem:
                matrix[indice[key]][indice[tunnel]] = 1
        

        # print("\n".join(["\t".join(map(str,ligne)) for ligne in matrix]))
        return matrix

    def floydWarshall(graph):

        for k in range(N):

            # pick all vertices as source one by one
            for i in range(N):

                # Pick all vertices as destination for the
                # above picked source
                for j in range(N):

                    # If vertex k is on the shortest path from
                    # i to j, then update the value of dist[i][j]
                    dist[i][j] = min(dist[i][j],
                                        dist[i][k] + dist[k][j]
                                        )
        # print("\n".join(["\t".join(map(str,ligne)) for ligne in dist]))



    INF = 1000
    pos = {}
    valves = {
    }
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
                openable_valves[name] = int(flow)
                openable_cout+=1
                best_derive+=int(flow)
            
            valves[name] = tunnels
    
    
    indice = {val:i for i,val in enumerate(sorted(valves.keys()))}


    N = len(valves)
    t = time.perf_counter()

    adj = adjacence_matrix(valves)

    dist = list(map(lambda i: list(map(lambda j: j, i)), adj))

    print((time.perf_counter()-t))
    floydWarshall(adj)
    print((time.perf_counter()-t))


    resultats = []
    openable_indices =  [i for  val,i in indice.items() if val in openable_valves.keys()]
    N = len(openable_indices)
    flows = {openable_indices[i]: elem for i,elem in enumerate(openable_valves.values())}
    arrangements = []
    generateAllBinaryStrings(N,[0 for _ in range(N)],0)

    print((time.perf_counter()-t))


    for arrangement in arrangements:
        vals = list()
        for i,element in enumerate(openable_indices):
            if arrangement[i]:
                vals.append(element)
        
        resultats.append(search(0,tuple(vals), 26,0))
        
    print((time.perf_counter()-t))

    best = 0
    for i in range(len(arrangements)//2):

        if resultats[i] + resultats[-i-1] > best:
            best = resultats[i] + resultats[-i-1]
    
    print((time.perf_counter()-t))


    print(best)
    print(count)
    print(len(pos))
    # print(search("AA","AA", False, [False for _ in range(len(openable_valves))],[26, 26],26, {}, 0,0))
    # print((time.perf_counter()-t))
    # print(len(pos), len(visited_points))
    # print(sys.getsizeof(pos))
    # print(count)

if __name__ == '__main__':
    main()



   