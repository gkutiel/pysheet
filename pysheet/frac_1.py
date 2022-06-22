import random
from fire import Fire
from pysheet.tex import write_tex
from functools import reduce
from collections import Counter


def gen_worksheet(out='frac_1.tex', k=4):
    primes = [1, 1, 2, 2, 3, 3, 5, 7]
    NUM_COLS = 4
    NUM_ROWS = 5

    def prod(l):
        return reduce(lambda a, b: a * b, l, 1)

    def eq():
        choices = [1]
        while choices[0] == choices[-1]:
            choices = sorted(random.choices(primes, k=k))

        l = k-2 if k > 4 else k - 1

        b = d = sorted(random.sample(choices, k=l))
        while b == d:
            d = sorted(random.sample(choices, k=l))

        a = list((Counter(choices) - Counter(d)).elements())
        return f'\\frac{{{prod(a)}}}{{{prod(b)}}} = \\frac{{}}{{{prod(d)}}}'

    def row():
        return ' & '.join([eq() for _ in range(NUM_COLS)])

    write_tex(
        file=out,
        align='l', 
        rows=[row() for _ in range(NUM_ROWS)], 
        vs='4.3cm', 
        hs='3.5cm')


def main():
    Fire(gen_worksheet)


if __name__ == '__main__':
    main()
