from copy import deepcopy
message = open("message.txt","r").readlines()
lines = open("input.txt","r").readlines()
suedict = {}

for line in lines:
    line = line.split(",")
    suedict[line[0].split()[1].replace(":","")] = {line[0].split()[2].replace(":",""):int(line[0].split()[3]),line[1].split(":")[0].strip():int(line[1].split(":")[1].strip()),line[2].split(":")[0].strip():int(line[2].split(":")[1].strip())}
    #[line[0].split()[2]+" "+line[0].split()[3],line[1].strip(),line[2].strip()]

for line in message:
    line = line.strip().split(":")
    print(line)
    tmp = {}
    for k,v in suedict.items():
        if "cats" in line[0]:
            if "cats" in v.keys():
                if v["cats"] > int(line[1]):
                    tmp[k] = v
            else:
                tmp[k] = v
        elif "trees" in line[0]:
            if "trees" in v.keys():
                if v["trees"] > int(line[1]):
                    tmp[k] = v
            else:
                tmp[k] = v
        elif "pomeranians" in line[0]:
            if "pomeranians" in v.keys():
                if v["pomeranians"] < int(line[1]):
                    tmp[k] = v
            else:
                tmp[k] = v
        elif "goldfish" in line[0]:
            if "goldfish" in v.keys():
                if v["goldfish"] < int(line[1]):
                    tmp[k] = v
            else:
                tmp[k] = v
        elif line[0] in v.keys():
            if v[line[0]] == int(line[1]):
                tmp[k] = v
        elif line[0] not in v.keys():
            tmp[k] = v
    suedict = deepcopy(tmp)

print(suedict)