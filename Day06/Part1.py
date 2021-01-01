def changelights(lights,list1,list2,change):
    x1,y1 = list1
    x2,y2 = list2
    x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if change == "off":
                lights[i][j] = False
            elif change == "on":
                lights[i][j] = True
            else:
                lights[i][j] = not lights[i][j]
    return lights

lines = open("input.txt","r").readlines() 
lights = [[False for i in range(1000)] for j in range(1000)]

for line in lines:
    linelist = line.split()
    if linelist[1] == "on" or linelist[1] == "off":
        lights = changelights(lights,linelist[2].split(","),linelist[4].split(","),linelist[1])
    else:
        lights = changelights(lights,linelist[1].split(","),linelist[3].split(","),linelist[1])

part1 = 0
for i in range(len(lights)):
    for j in range(len(lights[i])):
        if lights[i][j] == True:
            part1 += 1

print(part1)