# 6. Извлечение квадратного корня.
import math
a = int(input('Введите число: '))

def fast_root(a):
    x = a # 1

    x0 = x # 2
    x = int((int(a / x) + x) / 2)
    while True:
        if x >= x0: # 3
            break
        else:
            x0 = x
            x = int((int(a / x) + x) / 2)

    return x0

def test():
    print('Начало тестов.')
    for i in range(1, 34677):
        ii = fast_root(i)
        if ii != int(math.sqrt(i)):
            print(f'Ошибка! {int(math.sqrt(i))} не равно {ii} на числе i = {i}')
            exit()
        '''else:
            print(f'i = {i} - успех!')'''
    print('Тесты успешно пройдены!')

print(f'Результат быстрого извлечения корня: sqrt({a}) = {fast_root(a)}') 
print(f'Результат извлечения корня (библиотека math): sqrt({a}) = {int(math.sqrt(a))}') 
test()