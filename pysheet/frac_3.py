from fire import Fire
from random import randint


def tikz_range(step):
    return f'{{0,{step},...,360}}'


def frac(a, b):
    return f'$\\frac{{{a}}}{{{b}}}$'


def frac_node(a, b):
    return r'\node[below] at (a.south) {\Huge ' + frac(a, b) + r'};'


def tikz_slice(step):
    return r'\foreach \r in' + tikz_range(step) + r'\draw[-] (0:0) -- (\r:2);'


def rand_frac(min_denom=2, max_denom=10, min_step=20):
    b = max_denom + 1
    x = y = z = 0
    while b < min_denom or b > max_denom:
        x, y, z = randint(0, 3), randint(0, 2), randint(0, 1)
        b = 2**x*3**y*5**z

    x_, y_, z_ = 3-x, 2-y, 1-z
    a = randint(1, b-1)

    step = min_step-1
    while step < min_step:
        step = int(360/b/(2**randint(0, x_)*3**randint(0, y_)*5**randint(0, z_)))

    return a, b, step


def q():
    a, b, step = rand_frac()
    return r'\begin{tikzpicture}[x=1cm, y=1cm] \node[circle, draw, minimum size=4cm] at(0,0) (a) {};' + frac_node(a, b) + tikz_slice(step) + r'\end{tikzpicture}'


def gen_worksheet(out='frac_3.tex'):
    with open(out, 'w') as f:
        print(r'''
        \documentclass[]{article}
        \usepackage{fullpage}
        \usepackage{tikz}
        \begin{document}
        \renewcommand{\arraystretch}{12}
        \begin{tabular}{p{.33\textwidth}p{.33\textwidth}p{.33\textwidth}}
        ''', file=f)
        print(r' \\'.join(['&'.join([q() for _ in range(3)]) for _ in range(3)]), file=f)
        print(r'''
        \end{tabular}
        \end{document}
        ''', file=f)


def main():
    Fire(gen_worksheet)


if __name__ == '__main__':
    main()
