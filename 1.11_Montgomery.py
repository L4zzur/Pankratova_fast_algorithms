m = int(input('Введите m: '))
x = int(input('Введите x: '))
y = int(input('Введите y: '))

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

def mp(x, y, m):
    k = len(str(m))

    m1 = -modinv(m, 10)
    while m1 < 0:
        m1 += 10

    print(m1)
    z = 0
    for i in range(k - 1, -1, -1):
        u = ((int(str(z)[0]) + int(str(x)[i])*int(str(y)[k - 1])) * m1) % 10
        z = int((z + int(str(x)[i]) * y + u * m) / 10)
    
    if z >= 10:
        z -= 10

    return z

print(f'Результат произведения Монтгомери: {mp(x, y, m)}')
print(f'Результат прямого вычисления: {(x * y * pow(10, -len(str(m)), m)) % m}')
    
    