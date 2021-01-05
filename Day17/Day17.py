from itertools import combinations
lines = sorted([int(i) for i in open("input.txt","r").readlines()])
output = []
part1 = 0
part2list = []
part2min = 0 
part2 = 0

for i in range(1,len(lines)+1):
    output += list(combinations(lines,i))

for i in output:
    if sum(i) == 150:
        part1 += 1
        part2list.append(i)

part2min = min(map(len,part2list))

for i in part2list:
    if len(i) == part2min:
        part2 += 1

print(part1)
print(part2)