import numpy as np
from fire import Fire
from pysheet.tex import write_tex


def gen_worksheet():
    NUM_COLS = 2
    NUM_ROWS = 3

    command = r'''
        \newcommand\clock[2]{
            \begin{tikzpicture}
                \draw[line width=0.2cm] (0,0) circle (3cm);

                % Center dot
                \draw[fill=black] (0,0) circle (0.1cm);        

                % Minutes ticks
                \foreach \i in {1,...,60}{
                    \def\angle{\i*6}
                    \draw[thin] (\angle:3cm) -- (\angle:2.7cm);
                } 
                
                % 5 minutes ticks
                \foreach \i in {1,...,12}{
                    \def\angle{\i*-30+90}
                    \draw[thin] (\angle:3cm) -- (\angle:2.5cm);
                    \node at (\angle:2.2cm) {\i};
                };

                \def\angle{90-#1*30-#2*.5}
                \draw[line width=0.1cm] (0,0) -- (\angle:1.6cm);
                
                % Minutes
                \def\angle{90-#2*6}
                \draw[line width=0.05cm] (0,0) -- (\angle:1.9cm);
            \end{tikzpicture}
        }
    '''

    def row():
        return '&'.join([
            f'\clock{{{h}}}{{{m*5}}}'
            for h, m in zip(
                np.random.randint(1, 13, NUM_COLS),
                np.random.randint(0, 12, NUM_COLS))
        ])

    write_tex(
        file='clock.tex',
        commands=command,
        rows=[row() for _ in range(NUM_ROWS)],
        vs='2cm',
        hs='5cm')


def main():
    Fire(gen_worksheet)


if __name__ == '__main__':
    main()
