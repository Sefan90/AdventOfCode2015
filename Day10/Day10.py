line = open("input.txt","r").readlines()[0]
counter = 0
lastchar = ""
for _ in range(50):
    output = ""
    for c in line:
        if lastchar == "":
            lastchar = c
            counter += 1
        elif lastchar == c:
            counter += 1
        else:
            output += str(counter)+lastchar
            lastchar = c
            counter = 1
    output += str(counter)+lastchar
    lastchar = ""
    counter = 0
    line = output

print(len(output))