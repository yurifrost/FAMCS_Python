
import math

n = int(input('N: '))
y_array = [float(input('y({i:d}): '.format(i=i))) for i in range(n + 1)]


def linear(y, t):
    t_i = math.floor(t)
    if t == n:
        return y[t_i]
    delta_y = y[t_i + 1] - y[t_i]
    return y[t_i] + delta_y * (t - t_i)


def check_func():
    t = float(input('Enter t [0, N]: '))
    while t >= 0 and t <= n:
        print(linear(y_array, t))
        t = float(input('Enter t [0, N]: '))


check_func()

# y(2.5) = 16.25
# y(3.1) = 20.099999999999998