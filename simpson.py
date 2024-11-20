import numpy as np

def simpson(a, b, f, eps):  
    # количество точек n должно быть нечётным 
    n = 11
    prev_res = 0
    sum_even = 0
    h = (b - a) / (n - 1)
    for i in range (2, n-1, 2):
        sum_even += f(a + i*h) 
    while True:
        sum_odd = 0
        for j in range (1, n, 2):
            sum_odd += f(a + j*h) 
        # применяем формулу Симпсона
        res = (h/3.0) * (f(a) + 4 * sum_odd + 2 * sum_even + f(b))
        # разность между различными разбиениями
        if abs(prev_res - res) < eps:
            break
        prev_res = res
        n = 2*n - 1
        h *= 0.5
        sum_even += sum_odd
    return res

print('Examples:')
print('\nf = sin(x), [a, b] = [0, pi], eps = 1e-4')
print('∫f(x)dx ≈ ', simpson(0, np.pi, np.sin, 1e-4))
print('\nf = sin(x), [a, b] = [0, pi], eps = 1e-7')
print('∫f(x)dx ≈ ', simpson(0, np.pi, np.sin, 1e-7))
print('\nf = exp(x), [a, b] = [0, 1], eps = 1e-6')
print('∫f(x)dx ≈ ', simpson(0, 1, np.exp, 1e-6))
print('\nf = 1/x, [a, b] = [2, 3], eps = 1e-3')
print('∫f(x)dx ≈ ', simpson(2, 3, lambda x: 1/x, 1e-3))

'''
СПРАВОЧНИК:
Метод Симпсона 
— это численный метод, который приближает интеграл функции 
путём разбиения интервала на подотрезки и использования парабол 
для аппроксимации функции на каждом подотрезке.
'''