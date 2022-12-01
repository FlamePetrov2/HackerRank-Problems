def count_substring(s,s1):
    counter = 0
    for i in range(0,len(s)-len(s1)+1):
        if s[i:i+len(s1)]==s1:
            counter+=1
    return counter

result = count_substring('ABCDCDC','CDC')
print(result)