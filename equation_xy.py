import numpy as np
import random
from fire import Fire
from tex import write_tex


def gen_worksheet(a=[2, 6], x=[-2, 8], b=[1, 10], y=[-2, 8]):
    def eq1(a1, x, b):
        if random.random() < 0.5:
            return f'{a1}X + {b} &= &{a1 * x + b}'
        else:
            return f'{a1}X - {b} &= &{a1 * x - b}'

    def eq2(a2, x, a3, y):
        if random.random() < 0.5:
            return f'{a2}X + {a3}Y &= &{a2 * x + a3 * y}'
        else:
            return f'{a2}X - {a3}Y &= &{a2 * x - a3 * y}'

    def eqs(eq1, eq2):
        return f'\\begin{{array}}{{lcr}}{eq1}\\\\{eq2}\\end{{array}}'

    def row():
        return ' & '.join([
            eqs(eq1(a1, x, b), eq2(a2, x, a3, y))
            for a1, x, b, a2, a3, y
            in zip(
                np.random.randint(a[0], a[1], 3),
                np.random.randint(x[0], x[1], 3),
                np.random.randint(b[0], b[1], 3),
                np.random.randint(a[0], a[1], 3),
                np.random.randint(a[0], a[1], 3),
                np.random.randint(y[0], y[1], 3))])

    write_tex(align='l', rows=[row() for _ in range(6)], hs='2.2cm')


def main():
    Fire(gen_worksheet)


if __name__ == '__main__':
    main()
