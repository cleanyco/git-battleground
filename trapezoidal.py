def count_h(a, b, n):
    return (b - a) / n


def integral_func(curX):
    return 9 * (curX ** 2) - 4 * curX


def count_integral(x, h):
    sum = 0
    square = (integral_func(x[0]) + integral_func(x[len(x) - 1])) / 2
    print(square)

    for i in range(1, len(x) - 2):
        print(integral_func(x[i]))
        sum += integral_func(x[i])

    return (sum + square) * h


n = float(input('Добрый день, введите количество отрезков n: '))
a = float(input('Введите границу интегрирования a: '))
b = float(input('Введите границу интегрирования b: '))

h = count_h(a, b, n)
x = []
step = h
x.append(a)
for i in range(int(n + 1)):
    x.append(a + step)
    step += h

print(x)

res = count_integral(x, h)
print(res)