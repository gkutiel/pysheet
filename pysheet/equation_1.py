import numpy as np
import random
from fire import Fire
from pysheet.tex import write_tex


def gen_worksheet(a=[2, 10], x=[-10, 10], b=[1, 10]):
    def eq(a, x, b):
        if random.random() < 0.5:
            return f'{a}X + {b} = {a * x + b}'
        else:
            return f'{a}X - {b} = {a * x - b}'

    def row():
        NUM_COLS = 4
        return ' & '.join([
            eq(a, x, b)
            for a, x, b
            in zip(
                np.random.randint(a[0], a[1], NUM_COLS),
                np.random.randint(x[0], x[1], NUM_COLS),
                np.random.randint(b[0], b[1], NUM_COLS))])

    write_tex(align='l', rows=[row() for _ in range(6)], hs='2.5cm')


def main():
    Fire(gen_worksheet)


if __name__ == '__main__':
    main()
