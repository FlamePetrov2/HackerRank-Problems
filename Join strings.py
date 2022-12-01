def splitAndJoin(line):
    s1=''
    for i in line:
        if i == " ":
            i = '-'
            s1+=i
        else:
            s1+=i
    return s1

line = input()
result = splitAndJoin(line)
print(result)  