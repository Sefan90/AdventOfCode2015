def rec_part1(dist, key, usedkeys, first):
    output = 0
    for k in dist[key].keys():
        if k not in usedkeys:
            tmp = rec_part1(dist,k,usedkeys+[k],first)+dist[key][k]
            if output < tmp:
                output = tmp
    if output == 0:
        output = dist[key][first]
    return output

lines = open("input.txt","r").readlines()
happydict = {}

for line in lines:
    linelist = line.split()
    if linelist[0] not in happydict.keys():
        happydict[linelist[0]] = {linelist[10][:-1]:0}
    if linelist[10][:-1] not in happydict.keys():
        happydict[linelist[10][:-1]] = {linelist[0]:0}
    if linelist[10][:-1] not in happydict[linelist[0]].keys():
        happydict[linelist[0]][linelist[10][:-1]] = 0
    if linelist[0] not in happydict[linelist[10][:-1]].keys():
        happydict[linelist[10][:-1]][linelist[0]] = 0
    if linelist[2] == "gain":       
        happydict[linelist[0]][linelist[10][:-1]] += int(linelist[3])
        happydict[linelist[10][:-1]][linelist[0]] += int(linelist[3])
    else:
        happydict[linelist[0]][linelist[10][:-1]] -= int(linelist[3])
        happydict[linelist[10][:-1]][linelist[0]] -= int(linelist[3])

part1 = []
for k,v in happydict.items():
    part1.append(rec_part1(happydict,k,[k],k))
print(sorted(part1)[0])