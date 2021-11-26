from math import log
n = int(input('Введите n: '))
w = int(input('Введите w: '))
a = input('Введите a: ')

def fft(n, w, a):
    m = int(w ** (n / 2) + 1)
    a = [int(i) for i in a] # число в список его цифр
    a.reverse()


    if log(n, 2) % 1 != 0:
        print('n не является степенью двойки')
        exit
    else:
        k = int(log(n, 2))

    s = []
    r = []
    for i in range(n):
        s.append(0)
        r.append(a[i])

    return k

print(fft(n, w, a))