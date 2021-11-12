# 3. Приведение чисел по модулю (Алгоритм Барретта).
def barrett(x, m):
    m = str(m)
    b=10
    l = len(m) # длина модуля
    m = int(m) # модуль в число

    if len(str(x)) > 2 * l:
        #print('Условие не выполняется (n > 2k)')
        return -1

    z = int((b ** (2 * l)) / m) 

    q = int(int(x / (b ** (l - 1)) * z) / (b ** (l + 1))) # 1

    r1 = x % (b ** (l + 1)) # 2
    r2 = (q * m) % (b ** (l + 1)) 

    if r1 >= r2: # 3
        r = r1 - r2
    else:
        r = b ** (l + 1) + r1 - r2

    while r >= m: # 4
        r = r - m
    
    return r

def test():
    print('Начало тестов.')
    for i in range(1, 1000):
        for j in range(1, 37):
            ii = barrett(i, j)
            if ii == -1:
                pass
            elif ii != i % j:
                print(f'Ошибка! {i % j} не равно {ii} на числах i = {i}, j = {j}')
                exit()
            '''else:
                print(f'i = {i}, j = {j} - успех!')'''
    print('Тесты успешно пройдены!')

x = int(input('Введите число: '))
m = int(input('Введите модуль: '))

if barrett(x, m) == -1:
    print('Условие не выполняется (n > 2k)')
else:
    print(f'Результат алгоритма Барретта: {x} mod {m} = {barrett(x, m)}') # 5
    print(f'Результат простого приведения по модулю: {x} mod {m} = {x % m}')
test()