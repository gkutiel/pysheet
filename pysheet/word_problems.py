from random import choice, randint
from pysheet.tex import write_tex
from fire import Fire

names = {'יואב', 'יעל', 'טליה'}


def word_problem(*, x, a, b, first_name=None, second_name=None):
    if first_name is None:
        first_name = choice(list(names - set([second_name])))

    if second_name is None:
        second_name = choice(list(names - set([first_name])))

    return f'ל{first_name} יש {a} קופסאות, בכל קופסה מספר זהה של עוגיות. ל{second_name} יש {b} עוגיות. ל{first_name} ו{second_name} ביחד יש {a*x+b} עוגיות, כמה עוגיות יש ל{first_name} בכל קופסה?'


def word_problems(count=5, min_x=1, max_x=30, min_a=2, max_a=30, min_b=10, max_b=100):
    def problems():
        for i in range(count):
            x = randint(min_x, max_x)
            a = randint(min_a, max_a)
            b = randint(min_b, max_b)
            yield i+1, word_problem(x=x, a=a, b=b)

    with open('main.tex', 'w') as f:
        print(r''' 
            \nonstopmode
            \documentclass[]{article}
            % LIBS
            \usepackage{polyglossia,enumitem}
            \usepackage[cm]{fullpage}


            % HEBREW
            \setmainlanguage{hebrew}
            \newfontfamily\hebrewfont[Script=Hebrew]{Arial Hebrew}
            \let\hebrewfonttt\ttfamily
            \setlist[itemize,1]{label={\fontfamily{cmr}\fontencoding{T1}\selectfont\textbullet}}
            \setotherlanguage{english}

            \begin{document}
        ''', file=f)
        for i, p in problems():
            print(f'\\section*{{שאלה {i}}}', file=f)
            print(p, file=f)
            print(r'\section*{תשובה}', file=f)
            print(r'\vspace{1cm}', file=f)

        print(r'''
            \end{document}
        ''', file=f)


def main():
    Fire(word_problems)
