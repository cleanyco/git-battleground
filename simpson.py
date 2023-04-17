import math


def count_h(a, b, n):
    return (b - a) / n


def integral_func(curX):
    return math.sqrt(1 + 2 * (curX**2) - (curX**3))


n = float(input('Добрый день, введите количество отрезков n: '))
a = float(input('Введите границу интегрирования a: '))
b = float(input('Введите границу интегрирования b: '))

h = count_h(a, b, n)
x = [a]

for i in range(1, int(n) + 1):
    x.append(x[i-1] + h)
print(x)

sum = integral_func(x[0]) + integral_func(x[len(x) - 1])

i = 0
while i < len(x):
    if (i == 0) | (i == len(x)-1):
        i += 1
        continue
    if i % 2 == 0:
        sum += 2 * integral_func(x[i])
        print(str(2) + '*' + str(integral_func(x[i])))
        i += 1
    else:
        sum += 4 * integral_func(x[i])
        print(str(4) + '*' + str(integral_func(x[i])))
        i += 1
sum *= h/3
print(sum)
