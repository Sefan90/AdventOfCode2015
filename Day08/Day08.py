lines = open("input.txt","r").readlines() 
chars = 0
memchars = 0
part2 = 0
for line in lines:
    line = line.strip()
    chars += len(line)
    memchars += len(bytes(line, encoding='ascii').decode('unicode-escape'))-2 #Because all row start and end with a "
    #part2 += len(line)+4+(line.count('"')-2)+line.count('\\') #Both works
    part2 += len('"'+line.replace("\\","\\\\").replace('"','\\"')+'"')
print(chars-memchars)
print(part2-chars)

#8356 to high