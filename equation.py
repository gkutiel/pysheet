import numpy as np
import random
from random import randint
from fire import Fire
import json


def eq(a, x, b):
    if random.random() < 0.5:
        return f'{a}X + {b} = {a * x + b}'
    else:
        return f'{a}X - {b} = {a * x - b}'


def row(size=4):
    return ' & '.join([
        eq(a, x, b)
        for a, x, b
        in zip(
            np.random.randint(2, 5, size),
            np.random.randint(-5, 5, size),
            np.random.randint(1, 10, size))]) + '\\\\[\\vs]'


def gen_worksheet(num_rows=6):
    rows = [row() for _ in range(num_rows)]

    with open('main.tex', 'w') as f:
        f.write('''
            \\documentclass[12pt]{article}
            \\usepackage{fullpage}

            \\def \\hs {2.3cm}
            \\def \\vs {3cm}    
            \\begin{document}

            \\[
                \\begin{array}{l@{\hspace{\hs}}l@{\hspace{\hs}}l@{\hspace{\hs}}l@{\hspace{\hs}}}
                    ''' + ''.join(rows) + '''

                \\end{array}
            \\]

            \\end{document}    
        '''
                )


def main():
    Fire(gen_worksheet)


if __name__ == '__main__':
    main()
