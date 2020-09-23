from abc import ABC, abstractmethod
from random import randint
from fire import Fire
import json


class Num:
    def __init__(self, l, h):
        self.l = l
        self.h = h

    def get(self):
        return randint(self.l, self.h)


def ex_add(n: Num, m: Num):
    return f'\\gkadd{{{n.get()}}}{{{m.get()}}}'


def ex_mul(n: Num, m: Num):
    return f'\\gkmul{{{n.get()}}}{{{m.get()}}}'


def ex_sub(n: Num, m: Num):
    a, b = n.get(), m.get()
    if a < b:
        a, b = b, a
    return f'\\gksub{{{a}}}{{{b}}}'


def ex_div(n: Num, m: Num):
    b = n.get()
    a = b * m.get()
    return f'\\gkdiv{{{a}}}{{{b}}}'


ops = {
    'add': ex_add,
    'sub': ex_sub,
    'mul': ex_mul,
    'div': ex_div,
}


def row(r):
    exs = [ops[ex['op']](Num(*ex['a']), Num(*ex['b'])) for ex in r]
    return '&'.join(exs) + '\\\\[\\vs]'


def gen_worksheet(config_json='config.json'):
    with open(config_json) as f:
        rows = [row(r) for r in json.load(f)]

    with open('main.tex', 'w') as f:
        f.write('''
            \\documentclass[12pt]{article}
            \\usepackage{fullpage}

            \\def \\hs {3.5cm}
            \\def \\vs {3cm}
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

            \\begin{document}

            \\[
                \\begin{array}{c@{\\hspace{\\hs}}c@{\\hspace{\\hs}}c@{\\hspace{\\hs}}c@{\\hspace{\\hs}}}
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
