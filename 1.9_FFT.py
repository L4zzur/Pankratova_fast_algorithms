import math
a = input('Введите коэффициенты: ')
a = [int(i) for i in a.split()]
m = int(input('Введите модуль: '))

def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def primRoots(modulo):
    roots = []
    required_set = set(num for num in range (1, modulo) if gcd(num, modulo) == 1)

    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
        if required_set == actual_set:
            roots.append(g)           
    return roots

def bin_list(x, k):
    y = []
    for i in range(k):
        y.append(0)
    i = k - 1
    while x > 0:
        y[i] = x % 2
        x = x // 2
        i -= 1
    return y

def rev(x, k):
    nums = bin_list(x, k)
    nums.reverse()
    nums = int(''.join(str(i) for i in nums), 2)
    return nums

def fft(a, m):

    k = len(a).bit_length() - 1
    n = pow(2, k)
    if n != len(a):
        print('Длина входного массива не является степенью двойки.')
        exit()

    if primRoots(m) == []:
        print('Примитивных корней не существует.')
        exit()
    else:
        w = int(input(f'Выберите корень из списка {primRoots(m)}: '))
        if w not in primRoots(m):
            print('Введён не примитивный корень')
            exit()
    
    S = []
    R = []
    for i in a:
        R.append(i)
        S.append(0)
    
    for l in range(k - 1, -1, -1):
        for i in range(n):
            S[i] = R[i]
        for j in range(n):
            i = bin_list(j, k)
            i_0 = [x for x in i]
            i_1 = [x for x in i]

            i_0[l - 1] = 0
            i_1[l - 1] = 1

            i_0 = int(''.join(str(i) for i in i_0), 2)
            i_1 = int(''.join(str(i) for i in i_1), 2)

            deg = rev((j // pow(2, l)), k)

            R[j] = (S[i_0] + pow(w, deg) * S[i_1]) % m

    result = []
    for i in range(n):
        result.append(R[rev(i, k)])

    return result
    
print(f'Результат БПФ: {fft(a, m)}')
