N = int(input('Задайте колко неща ще въведете: '))
insertL=[]
l=[]
for i in range(N):
    command = input('Дайте команда: ')
    if 'append' in command:
        for word in command.split():
            if word.isdigit():
                l.append(int(word))

    elif 'insert' in command:
        for word in command.split():
            if word.isdigit():
                insertL.append(int(word))
        num = insertL[1]
        index = insertL[0]
        l.insert(index,num)
        insertL.clear()

            
    elif 'print' in command:
        print(l)
    elif 'remove' in command:
        for word in command.split():
            if word.isdigit():
                l.remove(int(word))

    elif 'sort' in command:
        l.sort()
    elif 'pop' in command:
        l.pop()
    elif 'reverse' in command:
        l.reverse()
