import random
import numpy as np
from fire import Fire
from pysheet.tex import write_tex


def gen_worksheet(a=[1, 3], b=[2, 10]):
    NUM_COLS = 4
    NUM_ROWS = 5

    def eq(a, b, c, d):
        return f'\\frac{{{a}}}{{{b}}} + \\frac{{{c}}}{{{d}}} = '

    def row():
        return ' & '.join([
            eq(a, b, c, d)
            for a, b, c, d in zip(
                np.random.randint(a[0], a[1], NUM_COLS),
                np.random.randint(b[0], b[1], NUM_COLS),
                np.random.randint(a[0], a[1], NUM_COLS),
                np.random.randint(b[0], b[1], NUM_COLS))])

    write_tex(
        file='frac_2.tex',
        align='l', 
        rows=[row() for _ in range(NUM_ROWS)], 
        vs='4.3cm', 
        hs='3.5cm')


def main():
    Fire(gen_worksheet)


if __name__ == '__main__':
    main()
