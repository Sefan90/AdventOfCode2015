from copy import deepcopy
lines = open("input.txt","r").readlines()
lights = [[char for char in line.strip()] for line in lines]

for _ in range(100):
    tmplist = [["." for char in line.strip()] for line in lines]
    for i in range(len(lights)):
        for c in range(len(lights[i])):
            neighbors = 0
            for x in [-1,0,1]:
                for y in [-1,0,1]:
                    if i+y >= 0 and i+y < len(lights) and c+x >= 0 and c+x < len(lights[i]):
                        if i+y == i and c+x == c:
                            continue
                        elif lights[i+y][c+x] == "#":
                            neighbors += 1
            if lights[i][c] == "#" and neighbors not in [2,3]:
                tmplist[i][c] = "."
            elif lights[i][c] == "." and neighbors == 3:
                tmplist[i][c] = "#"
            else:
                tmplist[i][c] = lights[i][c]
    lights = deepcopy(tmplist)
    
part1 = 0
for line in lights:
    for c in line:
        if c == "#":
            part1 += 1

print(part1)
