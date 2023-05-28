# ЗАДАЧА 1 (БЕЗ ЦИКЛА)
# slovar = {"key1": "value1",
#           "key2": "value2",
#           "key3": "value3",
#           "key4": "value4",
#           "key5": "value5"}
#
# keys = list(slovar.keys())
# val = list(slovar.values())
# print(keys, val)


# ЗАДАЧА 1 (С ЦИКЛОМ)
slovar = {"key1": "value1",
          "key2": "value2",
          "key3": "value3",
          "key4": "value4",
          "key5": "value5"}

keys = []
values = []

for i in slovar:
    keys.append(i)
    values.append(slovar[i])

print(keys, values)

