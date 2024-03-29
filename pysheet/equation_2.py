import numpy as np
import random
from fire import Fire
from pysheet.tex import write_tex


def gen_worksheet(
    out='equation_2.tex',
    a=[2, 10], 
    x=[-10, 10], 
    b=[1, 10]):
    NUM_COLS = 3
    NUM_ROWS = 5

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
                np.random.randint(a[0], a[1], NUM_COLS),
                np.random.randint(x[0], x[1], NUM_COLS),
                np.random.randint(b[0], b[1], NUM_COLS),
                np.random.randint(a[0], a[1], NUM_COLS),
                np.random.randint(a[0], a[1], NUM_COLS),
                np.random.randint(x[0], x[1], NUM_COLS))])

    write_tex(
        file=out, 
        align='l', 
        rows=[row() for _ in range(NUM_ROWS)], 
        hs='2.7cm', 
        vs='4.1cm')


def main():
    Fire(gen_worksheet)


if __name__ == '__main__':
    main()
