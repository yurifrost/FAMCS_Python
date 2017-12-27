import numpy as np

a = 4
c = 2

def f(x):
    return 4 * x + 1


def checkFunc(x):
    return float(f(x) - f(c)) / (x - c)


correct = 0
incorrect = 0

for x in np.random.uniform(0, 10, 100):
    if checkFunc(x) == a:
        correct += 1
    else:
        incorrect += 1
        print('Wrong: %.20f' % checkFunc(x))

print('Correct:', correct)
print('Incorrect:', incorrect)

# Все ошибки находятся в пределах погрешности вычислений