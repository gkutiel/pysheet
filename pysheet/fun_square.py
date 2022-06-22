from fire import Fire
from random import choice, randint, sample
from collections import defaultdict
from pprint import pprint

ops = {
    'x': lambda x, y: x * y,
    '+': lambda x, y: x + y,
}


start = r'''\nonstopmode
\documentclass[]{article}
\usepackage{array}
\newcolumntype{P}{ > {\Large\centering\arraybackslash}m{19pt}}

\begin{document}
\renewcommand{\arraystretch}{2.5}
\centering
'''


def table(n):
    return r'''
    \begin{tabular}{|P | *{''' + str(n-1) + r'''}{ | P}|}
    \hline
    '''


end = r'''
\end{tabular}
\end{document}'''


def fun_square(n=10, max_val=10, op='x', out='fun_square.tex'):
    n = n+1

    class Vals:
        def __init__(self, n, max_val):
            self.op = ops[op]
            self.rows = sample(range(1, max_val + 1), k=n)
            self.cols = sample(range(1, max_val + 1), k=n)

        def get(self, i, j):
            if i == 0:
                return self.cols[j]

            if j == 0:
                return self.rows[i]

            return self.op(
                self.rows[i],
                self.cols[j])

    def cells(n):
        cols = set(range(1, n))
        rows = set(range(1, n))
        cells = defaultdict(list)

        row, col = 0, choice(list(cols))
        cols.remove(col)
        cells[row].append(col)
        for i in range(2*n-3):
            if i % 2 == 0:
                row = choice(list(rows))
                rows.remove(row)
                cells[row].append(col)
            else:
                col = choice(list(cols))
                cols.remove(col)
                cells[row].append(col)

        return cells

    def rows(n, cells, max_val):
        vals = Vals(n, max_val)
        rows = [[''] * (n) for _ in range(n)]
        rows[0][0] = op

        for row in cells:
            for col in cells[row]:
                rows[row][col] = str(vals.get(row, col))

        pprint(rows)
        return '\n'.join([
            ' & '.join(
                rows[i]) + (r' \\ \hline \hline' if i == 0 else r' \\ \hline')
            for i in range(n)])

    max_val = max(max_val, n)
    c = cells(n)
    print(c)
    tex = f'{start}{table(n)}{rows(n, c, max_val)}{end}'
    with open(out, 'w') as f:
        f.write(tex)


def main():
    Fire(fun_square)


if __name__ == '__main__':
    main()
