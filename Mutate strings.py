def mutateString(s,i,c):
    l = list(s)
    l[i] = c
    s = ''.join(l)
    return s

s = input()
i,c = input().split()
s_new = mutateString(s, int(i), c)
print(s_new)