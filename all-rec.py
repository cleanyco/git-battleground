def count_h(a, b, n):
    return (b - a) / n


def integral_func(curX):
    return 1 / curX


n = float(input('Добрый день, введите количество отрезков n: '))
a = float(input('Введите границу интегрирования a: '))
b = float(input('Введите границу интегрирования b: '))

h = count_h(a, b, n)
x = [a]
for i in range(1, int(n)):
    x.append(x[i-1] + h)

sum = 0
for i in range(len(x)):
    sum += integral_func(x[i]) * h

print('Левых треугольников: ')
print(round(sum, 3))

x = [a + h]
for i in range(1, int(n)):
    x.append(x[i-1] + h)

sum = 0
for i in range(len(x)):
    sum += integral_func(x[i]) * h

print('Правых треугольников: ')
print(round(sum, 3))

x = [a]
for i in range(1, int(n)):
    x.append(x[i-1] + h)

sum = 0
for i in range(len(x)):
    sum += integral_func((x[i]) + h/2) * h


print('Средних треугольников: ')
print(round(sum, 3))