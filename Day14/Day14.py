lines = open("input.txt","r").readlines()
reindeer = {}
part1 = 0
part2 = 0

for line in lines:
    linelist = line.split()
    reindeer[linelist[0]] = [int(linelist[3]),int(linelist[6]),int(linelist[13]),0,0]

for i in range(2503):
    for k,v in reindeer.items():
        if i%(v[1]+v[2]) < v[1]:
            reindeer[k][3] += v[0]
        if v[3] > part1:
            part1 = v[3]
    for k,v in reindeer.items():
        if v[3] == part1:
            reindeer[k][4] += 1
        if v[4] > part2:
            part2 = v[4]

print(reindeer)
print(part1)
print(part2)