a = int(input())
u = 0
for i in range(a):
    x = input().split()
    if int(x[0]) + int(x[1]) + int(x[2]) >= 2:
        u += 1
print(u)
        
