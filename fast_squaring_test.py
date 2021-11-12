count = int(input("Количество проверок: "))
for n in range(count):
    n = str(n)
    k = len(n)
    x = [int(i) for i in n] # число в список его цифр
    x.reverse() # перевернутый список
    y = [0 for i in range (2 * k)] # 1. пустой список y

    for i in range(k): # 2
        uv = y[2 * i] + x[i] * x[i] # 2.1
        c = 0
        u = uv // 10
        v = uv % 10
        y[2 * i] = v
        for j in range(i + 1, k): # 2.2
            cuv = y[i + j] + 2 * x[i] * x[j] + c*10 + u
            c = cuv // 100
            v = cuv % 10
            u = (cuv - c * 100) // 10
            y[i + j] = v
        if c != 0: # 2.3
            y[i + k + 1] += c #c
        y[i + k] += u
    result = int(''.join([str(i) for i in reversed(y)])) 
    print(f'Быстрое: {result}. Обычное: {int(n) * int(n)}. Ошибка: {result != (int(n) * int(n))}')
    if result != (int(n) * int(n)):
        print(f'Ошибка на числе {n}.')
        break