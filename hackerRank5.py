class HashedNum():
    def __init__(self,n,integer_list) -> None:
        self.n = n
        self.integer_list = integer_list
    def getHash(self):
        t = (self.n,self.integer_list)
        hash1 = hash(t)
        print(hash1)



n = int(input())
integer_list = map(int, input().split())

hash1 = HashedNum(n,integer_list)
x = hash(hash1)
print(x)