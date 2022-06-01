a = input("Введите первое слово: ")
b = input("Введите второе слово: ")
c = input("Введите третье слово: ")
u = list()

for i in a:
    l = 0
    for j in b:
        if i == j:
            for k in c:
                if i == k and l != 0:
                    for y in u:
                        if y == i:
                            l = 1
                    if l == 0:
                        u.append(i)

for i in b:
    l = 0
    for j in a:
        if i == j:
            for k in c:
                if i == k and l != 1:
                    for y in u:
                        if y == i:
                            l = 1
                    if l == 0:
                        u.append(i)

for i in c:
    l = 0
    for j in b:
        if i == j:
            for k in a:
                if i == k and l != 1:
                    for y in u:
                        if y == i:
                            l = 1
                    if l == 0:
                        u.append(i)

print(u)