# 4 Приведение по модулю специального вида
def reduction(x, m):
    b = 10
    q, t, r = 1, 1, 1
    while b ** t <= m:
        t += 1
    r = x % (b ** t)
    q = (x - r) // (b ** t)
    c = 10 ** t - m
    while q > 0:
        qc = q * c
        r1 = qc % (b ** t)
        q1 = (qc - r1) // (b ** t)
        r = r + r1
        q = q1
    while r >= m:
        r = r - m

    return r

def test():
    print('Начало тестов.')
    for i in range(11, 10000):
        for j in range(i-10, i):
            ii = reduction(i, j)
            if ii != i % j:
                print(f'Ошибка! {i % j} не равно {ii} на числах i = {i}, j = {j}')
                exit()
            '''else:
                print(f'i = {i}, j = {j} - успех!')'''
    print('Тесты успешно пройдены!')

x = int(input('Введите число: '))
m = int(input('Введите модуль: '))

print(f'Результат алгоритма Барретта: {x} mod {m} = {reduction(x, m)}') # 5
print(f'Результат простого приведения по модулю: {x} mod {m} = {x % m}')
    
test()
