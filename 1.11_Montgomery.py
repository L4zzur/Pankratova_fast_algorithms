m = int(input('Введите m: '))
x = int(input('Введите x: '))
y = int(input('Введите y: '))
k = int(input('Введите k: '))


def gcd_extended(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        z, y, x = gcd_extended(b % a, a)
        return (z, x - (b // a) * y, y)

def modinv(a, m):
    z, x, y = gcd_extended(a, m)
    if z != 1:
        raise Exception('Обратного элемента по модулю не существует.')
    else:
        return x % m

def mp(x, y, m, k):
    m1 = -modinv(m, 10)
    while m1 < 0:
        m1 += 10

    print(m1)

    x_list = list(map(int, list(str(x))[::-1]))
    y_list = list(map(int, list(str(y))[::-1]))
    print(x_list)


    z = 0
    for i in range(k):
        z_list = list(map(int, list(str(z))[::-1]))
        u = ((z_list[0] + x_list[i]*y_list[0]) * m1) % 10
        z = int((z + x_list[i] * y + u * m) / 10)
    
    if z >= m:
        z -= m

    return z

if x >= m or y >= m:
    print('Входные условия не выполняются (x >= m или y >= m)')
else:
    print(f'Результат произведения Монтгомери: {mp(x, y, m, k)}')
    print(f'Результат прямого вычисления: {(x * y * pow(10, -len(str(m)), m)) % m}')
    
    