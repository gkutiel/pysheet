import numpy as np
from fire import Fire
from pysheet.tex import write_tex


def gen_worksheet(
    out='equation_3.tex',
    a=[2, 10], 
    x=[-10, 10], 
    b=[1, 10]):
    NUM_COLS = 3
    NUM_ROWS = 5

    def eq(a, x, b, c):
        if a == c:
            c += 1
        d = (a - c) * x + b
        return (
            f'{a}X + {b} = {c}X + {d}'
            if d > 0 else
            f'{a}X + {b} = {c}X {d}'
            if d < 0 else
            f'{a}X + {b} = {c}X')

    def row():
        return ' & '.join([
            eq(a, x, b, c)
            for a, x, b, c
            in zip(
                np.random.randint(a[0], a[1], NUM_COLS),
                np.random.randint(x[0], x[1], NUM_COLS),
                np.random.randint(b[0], b[1], NUM_COLS),
                np.random.randint(a[0], a[1], NUM_COLS))])

    write_tex(
        file=out,
        align='l', 
        rows=[row() for _ in range(NUM_ROWS)], 
        hs='2.7cm', 
        vs='4.3cm')


def main():
    Fire(gen_worksheet)


if __name__ == '__main__':
    main()
