import numpy as np
import random
from fire import Fire


def gen_worksheet(a=[2, 5], x=[-5, 5], b=[1, 10]):
    def eq(a, x, b):
        if random.random() < 0.5:
            return f'{a}X + {b} = {a * x + b}'
        else:
            return f'{a}X - {b} = {a * x - b}'

    def row():
        return ' & '.join([
            eq(a, x, b)
            for a, x, b
            in zip(
                np.random.randint(a[0], a[1], 4),
                np.random.randint(x[0], x[1], 4),
                np.random.randint(b[0], b[1], 4))]) + '\\\\[\\vs]'

    rows = [row() for _ in range(6)]

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
