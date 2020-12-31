lines = open("input.txt","r").readlines() 
part1 = 0
part2 = 0
for line in lines:
    dimensions = line.split("x")
    #2*l*w + 2*w*h + 2*h*l
    l = int(dimensions[0])*int(dimensions[1])
    w = int(dimensions[1])*int(dimensions[2])
    h = int(dimensions[2])*int(dimensions[0])
    if l <= w and l <= h:
        part1 += l
    elif w <= l and w <= h:
        part1 += w
    elif h <= l and h <= w:
        part1 += h
    part1 += 2*l + 2*w + 2*h

    l = int(dimensions[0])
    w = int(dimensions[1])
    h = int(dimensions[2])
    if l <= h and  w <= h:
        part2 += l*w*h+l+l+w+w
    elif l <= w and h <= w:
        part2 += l*w*h+l+l+h+h
    elif w <= l and h <= l:
        part2 += l*w*h+h+h+w+w
print(part1)
print(part2)