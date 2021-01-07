from itertools import combinations

def prod(lista):
    output = 1
    for l in lista:
        output *= l
    return output

line = int(open("testinput.txt","r").readlines()[0])
counter = 2
factors = []
while counter * counter <= line:
    if line % counter:
        counter += 1
    else:
        line //= counter
        factors.append(counter)
if line > 1:
    factors.append(line)

part1 = [1]
for i in range(1,len(factors)):
    part1 += list(set([prod(c) for c in combinations(factors,i)]))

line = int(open("testinput.txt","r").readlines()[0])
part1 = sorted(list(set(part1)))
print(part1)
print(line)
print(part1[:-1])
while True:
    if sum(part1[:-1])*10 < line:
        break
    else:
        part1.pop()
print(part1)
print(part1[-1])
#850080 high
#198020 low
#340000 low
#400000