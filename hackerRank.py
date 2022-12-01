def zad1():
    n = int(input())
    i = 0
    arr=[]
    while i < n:
        print(i*i)
        i+=1
    
def zad2(year):
    leap = False
    if year % 4==0:
        if year % 100 == 0:
            if year % 400 == 0:       
                leap=True
                return print(leap)
            else:
                return leap
        else:
            return True
    else:
        return leap

def zad3():
    n = 5
    i = 1
    string =''
    while i < n+1:
        string = string + (str(i))
        i+=1
    print(string)

# да се провери защото накрая завършва с {-truncated-}
# тва вече бачка ма програмата не ми го прие
def zad4():
    from itertools import groupby
    import sys
    sys.set_int_max_str_digits(10000)
    x = int(input(''))
    string = ''  
    for key,group in (groupby(str(x))):
        counter = len(list(group))
        grouped = (f'({counter}, {key})')
        string = string + grouped + " "
    print(string)


        
    
    
