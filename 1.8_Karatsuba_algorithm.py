# 7. Алгоритм быстрого умножения.
u = int(input('Введите первое число: '))
v = int(input('Введите второе число: '))

def present(x): # представление в виде x = x1*10^n + x0
    l = []
    l.append(int(x % (10**(len(str(x))/2))))
    l.append(int((x - l[0]) // (10**(len(str(x))/2))))
    l.append(int(len(str(x))/2))
    return l

A = present(u)[1] * present(v)[1]
B = present(u)[0] * present(v)[0]
C = (present(u)[1] + present(u)[0]) * (present(v)[1] + present(v)[0])
result = int(A * 10 ** len(str(u)) + (C - A - B) * 10 ** (len(str(u)) / 2) + B)

print(f'Результат быстрого умножения: {result}') # 3
print(f'Результат простого умножения: {u * v}')