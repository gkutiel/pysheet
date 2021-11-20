#!/usr/local/bin/fish
# gk-arithmetic && latexmk -pdf main.tex && lp main.pdf
# gk-equation-1 -a [1,1] -x [3,10] -b [1,2] && latexmk -pdf main.tex && lp main.pdf
# gk-clock && latexmk -pdf main.tex && lp main.pdf
gk-word-problems --max-x 3  --max-a 3 --max-b 10 && latexmk -xetex -pdf main.tex && lp main.pdf
