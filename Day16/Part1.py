from copy import deepcopy
message = open("message.txt","r").readlines()
lines = open("input.txt","r").readlines()
suedict = {}

for line in lines:
    line = line.split(",")
    suedict[line[0].split()[1].replace(":","")] = [line[0].split()[2]+" "+line[0].split()[3],line[1].strip(),line[2].strip()]

for line in message:
    line = line.strip()
    tmp = {}
    for k,v in suedict.items():
        if line in v:
            tmp[k] = v
        else:
            test = True
            for val in v:
                if line[0:-4] in val:
                    test = False
            if test == True:
                tmp[k] = v
    suedict = deepcopy(tmp)

print(suedict)