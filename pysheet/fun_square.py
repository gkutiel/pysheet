from fire import Fire
from random import choice, randint
from collections import defaultdict
from pprint import pprint


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
    rows = [[''] * (n) for _ in range(n)]
    rows[0][0] = '+'

    for row in cells:
        for col in cells[row]:
            rows[row][col] = str(randint(1, max_val))

    pprint(rows)
    return '\n'.join([
        ' & '.join(
            rows[i]) + (r' \\ \hline \hline' if i == 0 else r' \\ \hline')
        for i in range(n)])


start = r'''\nonstopmode
\documentclass[]{article}
\usepackage{array}
\newcolumntype{P}{ > {\Large\centering\arraybackslash}m{12pt}}

\begin{document}
\renewcommand{\arraystretch}{2}
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


def fun_square(n=10, max_val=20):
    c = cells(n)
    print(c)
    tex = f'{start}{table(n)}{rows(n, c, max_val)}{end}'
    with open('main.tex', 'w') as f:
        f.write(tex)


def main():
    Fire(fun_square)


if __name__ == '__main__':
    main()
