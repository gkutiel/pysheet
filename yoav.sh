#!/usr/local/bin/fish
gk-arithmetic --add [1,200] --sub [1,200] --mul [2,30] --div [2,30] && latexmk -pdf main.tex && lp main.pdf
# gk-equation-1 && latexmk -pdf main.tex && lp main.pdf
# gk-equation-2 && latexmk -pdf main.tex && lp main.pdf
# gk-equation-3 && latexmk -pdf main.tex && lp main.pdf

# gk-frac-1 && latexmk -pdf main.tex && lp main.pdf
