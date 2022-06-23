from functools import partial
from random import randint
from pysheet.tex import write_tex
from fire import Fire


def gen_worksheet(a, b, ex_func, out='arithmetic.tex'):

    NUM_ROWS, NUM_COLS = 5, 4

    def num(l, h):
        return randint(l, h)

    def row(exs):
        return '&'.join(exs)

    rows = [
        row([
            ex_func(
                num(a, b),
                num(a, b))
            for _ in range(NUM_COLS)])
        for _ in range(NUM_ROWS)]

    commands = '''
            \\newcommand{\\gkop}[3]{
                \\begin{array}{c@{\\;}r}
                    & #1 \\\\
                #2  & #3 \\\\
                \\hline{}
                \\end{array}
            }

            \\newcommand{\\gkadd}[2]{\\gkop{#1}{+}{#2}}
            \\newcommand{\\gksub}[2]{\\gkop{#1}{-}{#2}}
            \\newcommand{\\gkmul}[2]{\\gkop{#1}{\\times}{#2}}
            \\newcommand{\\gkdiv}[2]{\\gkop{#1}{\\div}{#2}}
    '''
    write_tex(
        file=out,
        rows=rows,
        commands=commands)


def ex_add(n: int, m: int):
    return f'\\gkadd{{{n}}}{{{m}}}'


def ex_mul(n: int, m: int):
    return f'\\gkmul{{{n}}}{{{m}}}'


def ex_sub(a: int, b: int):
    if a < b:
        a, b = b, a
    return f'\\gksub{{{a}}}{{{b}}}'


def ex_div(n: int, m: int):
    b = n
    a = b * m
    return f'\\gkdiv{{{a}}}{{{b}}}'


gen_add = partial(
    gen_worksheet,
    ex_func=ex_add)

gen_sub = partial(
    gen_worksheet,
    ex_func=ex_sub)

gen_mul = partial(
    gen_worksheet,
    ex_func=ex_mul)

gen_div = partial(
    gen_worksheet,
    ex_func=ex_div)


def add():
    Fire(gen_add)


def sub():
    Fire(gen_sub)


def mul():
    Fire(gen_mul)


def div():
    Fire(gen_div)
