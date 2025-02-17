# O(n)
n = int(input())
r = 0
for i in range(n+1):
    r = r + i

print(r)



# *OCP : 수정에는 닫혀있고 확정에는 열려있음 -> 어떻게? 클로져를 이용한 데코레이터를 사용하여