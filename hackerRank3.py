a=[]
k=0
for n in range(int(input())):
        name = input()
        score = float(input())
        a.append([score,name])
a.sort()
b=[]
while k < len(a):
    b.append(a[k][0])
    k+=1
b.sort()
names=[]
control=[]
# задаване на конролни точки за проверка (пример:37.21)
j=0
for i in b:
    if b[j-1] < b[j]:
        control.append(b[j])
        break
    j+=1
j=0
while j <= len(a)-1:
    if a[j][0] == control[0]:
        names.append(a[j][1])
        j+=1
    else:
        j+=1
names.sort()
for i in names:
    print(i)   

# Input:

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39    



# Ouput:

# Berry
# Harry




