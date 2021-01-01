import hashlib
line = open("input.txt","r").readlines()[0]
start = "99999"
counter = 0
while start[0:5] != "00000":
    counter += 1
    str2hash = line + str(counter)
    start = hashlib.md5(str2hash.encode()).hexdigest()
print(counter)


start = "999999"
counter = 0
while start[0:6] != "000000":
    counter += 1
    str2hash = line + str(counter)
    start = hashlib.md5(str2hash.encode()).hexdigest()
print(counter)