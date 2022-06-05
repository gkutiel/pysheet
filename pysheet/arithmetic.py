from random import randint
from pysheet.tex import write_tex
from fire import Fire


def gen_worksheet(
        add=[5, 15],
        sub=[5, 15],
        mul=[2, 5],
        div=[2, 5]):

    NUM_COLS = 4

    def num(l, h):
        return randint(l, h)

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

    def row(exs):
        return '&'.join(exs)

    rows = [
        row([ex_add(num(*add), num(*add)) for _ in range(NUM_COLS)]),
        row([ex_sub(num(*sub), num(*sub)) for _ in range(NUM_COLS)]),
        row([ex_mul(num(*mul), num(*mul)) for _ in range(NUM_COLS)]),
        row([ex_div(num(*div), num(*div)) for _ in range(NUM_COLS)]),
        row([
            ex_add(num(*add), num(*add)),
            ex_sub(num(*sub), num(*sub)),
            ex_mul(num(*mul), num(*mul)),
            ex_div(num(*div), num(*div))])]

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
        file='arithmetic.tex',
        rows=rows, 
        commands=commands)


def main():
    Fire(gen_worksheet)


if __name__ == '__main__':
    main()
