"""
Ручные вычисления:
    I = (6^3 - 2^3) / 3 - (6^2 - 2^2) / 2 = 53.(3)
"""

manual_calc = 53 + 1.0 / 3


def trapezoidal(f, a, b, n):
    """
    Вычисляет приближенное значение интеграла с помощью формулы трапеций
    f - подынтегральная функция
    a, b - пределы интегрирования
    n - количество частичных отрезков
    """
    h = float(b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    result *= h
    return result


def rectangular(f, a, b, n):
    """
    Вычисляет приближенное значение интеграла с помощью формулы прямоугольников
    f - подынтегральная функция
    a, b - пределы интегрирования
    n - количество частичных отрезков
    """
    h = float(b - a) / n
    result = f(a + 0.5 * h)
    for i in range(1, n):
        result += f(a + 0.5 * h + i * h)
    result *= h
    return result


trap_2 = trapezoidal(lambda x: x * (x - 1), 2, 6, 2)
trap_100 = trapezoidal(lambda x: x * (x - 1), 2, 6, 100)
rect_2 = rectangular(lambda x: x * (x - 1), 2, 6, 2)
rect_100 = rectangular(lambda x: x * (x - 1), 2, 6, 100)

print('Точное значение интеграла: {}\n'.format(manual_calc))

print('Аппроксимация трапециями:\n  2 трапеции: {}\n  100 трапеций: {}'
      .format(trap_2, trap_100))

print('Погрешность для аппроксимации трапециями:\n  2 трапеции: {}\n  100 трапеций: {}\n'
      .format(abs(trap_2 - manual_calc), abs(trap_100 - manual_calc)))

print('Аппроксимация прямоугольниками:\n  2 прямоугольника: {}\n  100 прямоугольников: {}'
      .format(rect_2, rect_100))

print('Погрешность для аппроксимации прямоугольниками:\n  2 прямоугольника: {}\n  100 прямоугольников: {}'
      .format(abs(rect_2 - manual_calc), abs(rect_100 - manual_calc)))
