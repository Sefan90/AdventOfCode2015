line = open("input.txt","r").readlines()[0]
def rec(string):
    if ord(string[-1])+1 == 123:
        return rec(string[0:-1])+chr(97)
    else:
        return string[0:-1]+chr(ord(string[-1])+1)

def checker(string):
    tests = False
    pairs = 0
    lastpair = -1
    if "i" in string or "o" in string or "l" in string:
        return True
    else:
        for i in range(len(string)-1):
            if i < len(string)-2:
                if ord(string[i]) == ord(string[i+1])-1 == ord(string[i+2])-2:
                    tests = True
            if string[i] == string[i+1]:
                if lastpair == -1:
                    pairs +=1
                elif i == lastpair+1 and string[i] == string[lastpair+1]:
                    continue
                else:
                    pairs +=1
                lastpair = i
    if tests == True and pairs >= 2:
        return False
    else:
        return True


while checker(line) == True:
    line = rec(line)
print(line)
line = rec(line)
while checker(line) == True:
    line = rec(line)
print(line)