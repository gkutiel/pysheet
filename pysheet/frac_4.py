from itertools import product
from math import gcd, lcm
from random import randint as rnd
from random import sample

from fire import Fire

from pysheet.tex import write_tex


def gen_worksheet(
        out='frac_4.tex',
        max_lcm=18):

    NUM_COLS = 3
    NUM_ROWS = 4

    def simple(a, c):
        g = gcd(a, c)
        return a // g, c // g

    def ex(c, d):
        l = lcm(c, d)
        a = l // c
        b = l // d
        a *= rnd(1, (l - b) // a)
        b *= rnd(1, (l - a) // b)
        return simple(a, l), simple(b, l)

    def eq(i, j):
        a, c = i
        b, d = j
        e = lcm(c, d)
        return r'''
            \def\r{1.2cm}
            \begin{tikzpicture}
            \draw (0,0) circle (\r);
            \foreach \a in {0, ''' + f'{360/e:.01f}' + r''', ..., 360} {
                \draw[] (0,0) -- (\a:\r);
            }
            \end{tikzpicture}
        ''' + f'\\frac{{{a}}}{{{c}}} + \\frac{{{b}}}{{{d}}} = '

    ds = list(range(2, max_lcm // 2))
    denos = [
        p for p in product(ds, ds)
        if lcm(*p) <= max_lcm]

    def row():
        exs = [ex(*ds) for ds in sample(denos, k=NUM_COLS)]
        return ' & '.join([
            eq(i, j)
            for i, j in exs])

    write_tex(
        file=out,
        align='l',
        rows=[row() for _ in range(NUM_ROWS)],
        vs='3.5cm',
        hs='3cm')


def main():
    Fire(gen_worksheet)


if __name__ == '__main__':
    main()
