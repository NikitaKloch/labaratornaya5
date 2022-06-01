a = input("Введите предложение: "). split()
b = a

b = [s.replace('чя', 'ча') for s in a]
b = [s.replace('шя', 'ша') for s in a]

print(b)


