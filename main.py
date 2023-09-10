# a = int(input())
# print(a + 2 - (a % 2))



# task 1

# a = input()
# if len(a) > 5:
#     print(a[:3], a[-3:])
# else:
#     print(a[0] * len(a))



# list comprehension
# lst2 = [chislo ** 2 for chislo in range(1, 6) if chislo ** 2 % 2 == 0]
# print(lst2)
#
# -------------------
# bukvi = "abcdef"
# print('Лудоман'.join(i.upper()*2 for i in bukvi))



# task 2
# lst = []
# a = input()
# for i in a:
#     if i.isdigit():
#         lst.append(int(i))
# print(lst)
#
# print([int(i) for i in a if i.isdigit()])


# task 3
# a = int(input())
# print(format(a, ","))


# task 4
# x = [-1, 2, 3, -2, 5]
# print([i for i in x if i > 0])

# task 5
# a = [5, 7, 4, 3, 4]
# otvet = []
# for i in range(len(a) - 1):
#     if a[i] < a[i+1]:
#         otvet.append(a[i+1])
# print(otvet)


# task 6
# x = [3, 18, 4, 5, 1, 3]
# otv = []
# for i in range(2):
#     b = max(x)
#     otv.append(b)
#     x.remove(b)
# print(otv)
#
#
# x = [3, 18, 4, 5, 1, 3]
# print(sorted(x)[-2:][::-1])

# task 7

# x = input()
# if x[::-1] == x:
#     print("True")
# else:
#     print("False")
# способ 2
# print(x == x[::-1])



# task 8
#
# x = [1, 2, 4, 3, 5]
# m = x.index(max(x))
# mini = x.index(min(x))
# x[m], x[mini] = x[mini], x[m]
# print(x)


# task 9
import random
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(5):
    print(x.pop(random.randint(0, len(x) - 1)))
print(x)
