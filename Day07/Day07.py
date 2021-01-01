from copy import deepcopy
lines = open("input.txt","r").readlines() 
wiredict = {}

while len(lines) != 0:
    print(len(lines))
    tmplines = []
    for line in lines:
        linelist = line.split()
        if linelist[1] == "->" and linelist[0].isdigit() == True:
            wiredict[linelist[2]] = int(linelist[0])
        elif (linelist[0] not in wiredict.keys() and linelist[0] != "NOT" and linelist[0].isdigit() == False) or (linelist[0] == "NOT" and linelist[1] not in wiredict.keys()):
            tmplines.append(line)
        elif linelist[1] == "->" and linelist[0].isdigit() == False:
            wiredict[linelist[2]] = wiredict[linelist[0]]
        elif linelist[1] == "AND" and (linelist[0] in wiredict.keys() or linelist[0].isdigit() == True) and (linelist[2] in wiredict.keys() or linelist[2].isdigit() == True):
            if linelist[0].isdigit() == True:
                if linelist[2].isdigit() == True:
                    wiredict[linelist[4]] = int(linelist[0]) & int(linelist[2])
                else:
                    wiredict[linelist[4]] = int(linelist[0]) & wiredict[linelist[2]]
            elif linelist[2].isdigit() == True:
                if linelist[0].isdigit() == True:
                    wiredict[linelist[4]] = int(linelist[0]) & int(linelist[2])
                else:
                    wiredict[linelist[4]] = wiredict[linelist[0]] & int(linelist[2])
            else:
                wiredict[linelist[4]] = wiredict[linelist[0]] & wiredict[linelist[2]]
        elif linelist[1] == "OR" and (linelist[0] in wiredict.keys() or linelist[2].isdigit() == True) and (linelist[2] in wiredict.keys() or linelist[2].isdigit() == True):
            if linelist[0].isdigit() == True:
                if linelist[2].isdigit() == True:
                    wiredict[linelist[4]] = int(linelist[0]) | int(linelist[2])
                else:
                    wiredict[linelist[4]] = int(linelist[0]) | wiredict[linelist[2]]
            elif linelist[2].isdigit() == True:
                if linelist[0].isdigit() == True:
                    wiredict[linelist[4]] = int(linelist[0]) | int(linelist[2])
                else:
                    wiredict[linelist[4]] = wiredict[linelist[0]] | int(linelist[2])
            else:
                wiredict[linelist[4]] = wiredict[linelist[0]] | wiredict[linelist[2]]
        elif linelist[1] == "LSHIFT":
            wiredict[linelist[4]] = wiredict[linelist[0]] << int(linelist[2])
        elif linelist[1] == "RSHIFT":
            wiredict[linelist[4]] = wiredict[linelist[0]] >> int(linelist[2])
        elif linelist[0] == "NOT":
            wiredict[linelist[3]] = 65535-wiredict[linelist[1]]
        else:
            tmplines.append(line)
    lines = deepcopy(tmplines)
print(wiredict["a"])
