lines = open("input.txt","r").readlines()

def rec(j, line):
    if line[j].isnumeric() or line[j] == "-":
        if line[j+1].isnumeric():
            tmp, k = rec(j+1,line)
            return line[j]+tmp, k
        else:
            return line[j], j
    else:
        return "", j

output = 0
for line in lines:
    i = 0
    while i < len(line):
        tmp, i = rec(i,line)
        if tmp != "":
            output += int(tmp)
        i += 1
print(output)

output = 0
for line in lines:
    i = 0
    skip = False
    lastpara = ""
    sumpara = 0
    para = 0
    hake = 0
    while i < len(line):
        if line[i] == "[":
            hake = True
        elif line[i] == "]" or line[i] == "{":
            hake = False
        if line[i] == "{" and skip == False:
            if sumpara != 0:
                 output += sumpara
                 sumpara = 0
            lastpara = line[i]
        elif line[i] == "{" and skip == False:
            para += 1
        elif (lastpara == "{" and line[i] == "}"):
            if skip == False:
                output += sumpara
                lastpara = ""
                sumpara = 0
            elif skip == True and para > 0:
                para -= 1
            else:
                skip = False
                lastpara = ""
                sumpara = 0
                para = 0
        elif lastpara == "{" and line[i] == "r" and line[i+1] == "e" and line[i+2] == "d" and hake == False:
            skip = True
        else:
            tmp, i = rec(i,line)
            if tmp != "" and lastpara == "":
                output += int(tmp)
            elif tmp != "" and lastpara != "":
                sumpara += int(tmp)
        i += 1
    output += sumpara

print(output)

#71790 low
#108862 high
#156051 high