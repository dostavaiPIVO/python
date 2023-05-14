len_str = int(input())
for i in range(len_str):
    x = input()
    if len(x) > 10:
        print(x[0] + str(len(x)-2) + x[-1])
    else:
        print(x)
