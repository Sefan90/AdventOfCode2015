lines = open("input.txt","r").readlines() 
part1 = 0
for line in lines:
    if line.count("a") + line.count("e") + line.count("i") + line.count("o") + line.count("u") >= 3:
        if line.count("ab") + line.count("cd") + line.count("pq") + line.count("xy") == 0:
            i = 0
            while i < len(line)-1:
                if line[i] == line[i+1]:
                    part1 += 1
                    break
                i += 1
print(part1)

part2 = 0
for line in lines:
        found = False
        for i in range(len(line)):
            if found == True:
                    break
            for j in range(len(line)):
                if found == True:
                    break
                if i != j and i+1 != j and i != j+1:
                    if line[i] == line[j] and line[i+1] == line[j+1]:
                        k = 0
                        while k < len(line)-2:
                            if line[k] == line[k+2]:
                                part2 += 1
                                found = True
                                break
                            k += 1
print(part2)