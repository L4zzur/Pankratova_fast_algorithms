# 5. Вычисление НОДа(Бинарный алгоритм)
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

def gcd(a, b): # Вариант 2 (поиск НОД вычитанием)
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

print(f'Результат поиска вычитанием: {gcd(a, b)}')

def present(x): # представление в виде x = 2^i + x1
    i = 0
    x1 = 0
    while x != 1:
        if x % 2 == 0:
            x = x / 2
            i += 1
        else:
            x1 = x
            x = 1
    if x1 == 0:
        x1 = x
    l = []
    l.append(i)
    l.append(int(x1))
    return l

def binary_gcd_func(a, b):
    k = min(present(a)[0], present(b)[0]) # 2
    a = present(a)[1]
    b = present(b)[1]

    while a != b: # 3
        if a < b: # 3.1
            a, b = b, a
        c = a - b # 3.2
        a = present(c)[1] # 3.3
    
    return (2 ** k) * a

def test():
    print('Начало тестов.')
    for i in range(600, 639):
        for j in range(i-1, i+3):
            if binary_gcd_func(i, j) != gcd(i, j):
                print(f'Ошибка! {gcd(i, j)} не равно {binary_gcd_func(i, j)} на числе i = {i}')
                exit()
            '''else:
                print(f'i = {i}, j = {j} - успех!')'''
    print('Тесты успешно пройдены!')

print(f'Результат бинарного алгоритма: {binary_gcd_func(a, b)}') # 4
test()

