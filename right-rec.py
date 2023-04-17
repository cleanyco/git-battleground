import math


def count_h(a, b, n):
    return (b - a) / n


def integral_func(curX):
    return 1 / math.log(curX)


n = float(input('Добрый день, введите количество отрезков n: '))
a = float(input('Введите границу интегрирования a: '))
b = float(input('Введите границу интегрирования b: '))

h = count_h(a, b, n)
x = [a + h]
for i in range(1, int(n)):
    x.append(x[i-1] + h)

print(x)

sum = 0
for i in range(len(x)):
    sum += integral_func(x[i]) * h

print(sum)