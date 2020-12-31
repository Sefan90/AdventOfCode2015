lines = open("input.txt","r").readlines() 
pos = [0,0]
part1 = set()
for line in lines:
    for c in line:
        pos = getnewpos(pos,c)
        part1.add(str(pos[0])+","+str(pos[1]))
print(len(part1))

pos1 = [0,0]
pos2 = [0,0]
part2 = set()
for line in lines:
    for i, c in enumerate(line):
        if i%2 == 0:
            pos1 = getnewpos(pos1,c)
        else:
            pos2 = getnewpos(pos2,c) 
        part2.add(str(pos1[0])+","+str(pos1[1]))
        part2.add(str(pos2[0])+","+str(pos2[1]))
print(len(part2))