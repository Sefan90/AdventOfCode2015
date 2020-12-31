lines = open("input.txt","r").readlines() 
part1 = 0
part2 = 0
for l in lines:
    for i, c in enumerate(l):
        if c == "(":
            part1 += 1
        if c == ")":
            part1 -= 1
            if part2 == 0 and part1 < 0:
                part2 = i + 1
print(part1)
print(part2)