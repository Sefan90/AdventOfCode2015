
while result < line:
    counter += 1
    result = counter
    if result%counter == 0:
        for i in range(1,counter):
            if counter%i == 0:
                result += i
    print(counter,result)
print(counter)