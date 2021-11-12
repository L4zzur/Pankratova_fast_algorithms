# 2. Быстрое возведение в степень. 
def fast_exponentiation(x, y):
    y = bin(y)
    y = y[2:len(y)] # двоичная запись степени
    y = [int(i) for i in y[::-1]] # перевернутая двоичная запись степени

    q = x  # 1 start
    if y[0] == 1:
        z = x
    elif y[0] == 0:
        z = 1  # 1 end

    for i in range(1, len(y)): # 2
        q = q * q # 2.1
        if y[i] == 1:
            z = z * q # 2.2
    
    return z

def test():
    print('Начало тестов.')
    for i in range(34677):
        ii = fast_exponentiation(i, i)
        if ii != i ** i:
            print(f'Ошибка! {i ** i} не равно {ii} на числе i = {i}')
            exit()
        else:
            print(f'i = {i} - успех!')
    print('Тесты успешно пройдены!')

x = int(input('Введите число: '))
y = int(input('Введите степень: '))

print(f'Результат быстрого возведения в степень: {fast_exponentiation(x,y)}')
print(f'Результат простого возведения в степень: {x ** y}')
test()