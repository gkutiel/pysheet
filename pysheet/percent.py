from random import randint


def gen(max_a=99, max_b=99):
    a = randint(1, max_a)
    b = randint(1, max_b)
    while a*b % 100:
        a = randint(1, max_a)
        b = randint(1, max_b)

    return a, b


def gen_worksheet(out='percent.tex'):
    with open(out, 'w') as f:
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
\setlength{\tabcolsep}{10pt} % Default value: 6pt
\renewcommand{\arraystretch}{5} % Default value: 1
\begin{tabular}{r r r r}
''', file=f)
        for i in range(10):
            print(r'\Huge', file=f)
            print(*[f'{a}\\% מ-{b}' for a, b, in [gen() for _ in range(4)]], sep='\t&\t\\Huge', end=r' \\',  file=f)
            print(file=f)
        print(r'''   
\end{tabular}

\end{document}
''', file=f)


if __name__ == '__main__':
    gen_worksheet()
