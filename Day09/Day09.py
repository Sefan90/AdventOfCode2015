def rec_part1(dist, key, usedkeys):
    minkey = key
    minval = 0
    smallest = -1
    while minkey in usedkeys:
        smallest += 1
        if smallest == len(dist[key].values()):
            return 0
        minval = sorted(dist[key].values())[smallest]
        for k, v in dist[key].items():
            if v == minval:
                minkey = k
                break
    usedkeys.append(minkey)
    return dist[key][minkey] + rec_part1(dist, minkey, usedkeys)

def rec_part2(dist, key, usedkeys):
    maxkey = key
    maxval = 0
    smallest = len(dist[key].values())
    while maxkey in usedkeys:
        smallest -= 1
        if smallest == -1:
            return 0
        maxval = sorted(dist[key].values())[smallest]
        for k, v in dist[key].items():
            if v == maxval:
                maxkey = k
                break
    usedkeys.append(maxkey)
    return dist[key][maxkey] + rec_part2(dist, maxkey, usedkeys)


lines = open("input.txt","r").readlines() 
distdict = {}
for line in lines:
    linelist = line.split()
    if linelist[0] not in distdict.keys():
        distdict[linelist[0]] = {}
    distdict[linelist[0]][linelist[2]] = int(linelist[4])
    if linelist[2] not in distdict.keys():
        distdict[linelist[2]] = {}
    distdict[linelist[2]][linelist[0]] = int(linelist[4])

part1 = []
part2 = []
for k,v in distdict.items():
    part1.append(rec_part1(distdict,k,[k]))
    part2.append(rec_part2(distdict,k,[k]))

print(sorted(part1)[0])
print(sorted(part2)[-1])