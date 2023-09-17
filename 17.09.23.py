# def func (lst: list) -> dict:
#     d = {'int' : 0,
#          'str' : 0,
#          'float' : 0,
#          'bool' : 0}
#     for i in lst:
#         if type(i) == int:
#             d['int'] += 1
#         elif type(i) == str:
#             d['str'] += 1
#         elif type(i) == float:
#             d['float'] += 1
#         elif type(i) == bool:
#             d['bool'] += 1
#     return d
# print(func([1, "Два", True, 3.14, "Четыре", False]))

# task ------------------------
# def func(x: int) -> list:
#     h = [0, 1]
#     while h[-1] < x:
#         h.append(h[-1]+h[-2])
#     return h[:-1]
#
#
# print(func(355))


# task --------------------------
# def func(x: list, xx:list):
#     return sorted(x + xx)
#
# print(func([1, 5, 8, 11,], [2, 5]))

# task ---------------------
# add 5
# minus 10
# div 2
# mul 6

# zero
# result
# exit


# d = {
#     "add": lambda x: c + x,
#     "minus": lambda x: c - x,
#     "div": lambda x: c // x,
#     "mul": lambda x: c * x,
# }
#
# c = 0
# while True:
#     zapros = input().split()
#     if len(zapros) == 1:
#         zapros = zapros[0] # ['zero'] -> 'zero'
#         if zapros == "exit":
#             break
#         elif zapros == "result":
#             print(c)
#         elif zapros == "zero":
#             c = 0
#     else:  # math operation
#         c = d[zapros[0]](int(zapros[1]))
#         # if zapros[0] == "add":
#         #     c = add(int(zapros[1]))


# task -------------------
#
# def is_sorted(x:list) -> bool:
#     return x == sorted(x)
#
# print(is_sorted([2, 3, 10]))
# print(is_sorted([3, 7, 1]))

# task ---------------------