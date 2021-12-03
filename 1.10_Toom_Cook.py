u = int(input('Введите первое число: '))
v = int(input('Введите второе число: '))

def value(a, x):
    y = 0
    for i in range(len(a)):
        y += a[i] * (x ** i)
    return y

def pres(a):
    x = []
    for i in range(len(str(a))):
        x.append(a % 10)
        a = a // 10
    return x


def Toom_Cook(u, v):
    if len(str(u)) != len(str(v)):
        print('Числа должны быть одинаковой длины!')
        return 0
    
    r = len(str(u))
    w = []
    ur = pres(u)
    vr = pres(v)
    for x in range(2 * r - 1):
        w.append(value(ur, x) * value(vr, x))
    print(w)

    #delta= []
    #for i in range(len(w)):
        #delta.append([w[i]])
    
    delta = []
    delta.append(w)
    delta.append([])

    max = len(w) - 1
    k = 1
    for j in range(1, len(w)):#Находим коэфиценты для интерполяционной формулы Ньютона
        i = 0
        while i < max:
            delta[j].append((delta[j-1][i+1] - delta[j-1][i]) // k)
            i += 1
        if i > 1:
            delta.append([])
        k += 1
        max -= 1
    
    c = []
    for i in range(len(delta)):
        c.append(delta[i][0])
    
    print(c)

    result = 0
    for i in range(len(c), 0):#Сразу считаем значение в x = 10 для получения числа
        k = len(c) - i - 2
        q = c[i]
        while k >= 0:
            q *= 10 - k
            k -= 1
        result += q
    return result

Toom_Cook(u, v)