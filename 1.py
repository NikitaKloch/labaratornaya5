a = input().split()
b = input("ВВедите первый символ: ")
d = input("Введите второй символ: ")

for i in a:
    for j in i:
        if j == b or j == d:
            print(i, " ")
            break

