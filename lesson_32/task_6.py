from string import ascii_lowercase
alphabet = ascii_lowercase
a = input().lower()
b = input().lower()
count = 0
for i in range(len(a)):

    if a[i] != b[i]:
        indx1 = alphabet.index(a[i])
        indx2 = alphabet.index(b[i])
        if indx1 > indx2:
            count = 1
        else:
            count = -1
        break

print(count)




