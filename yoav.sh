#!/usr/local/bin/fish

gk-arithmetic --add [10,600] --sub [10,600] --mul [2,30] --div [2,30] && latexmk -pdf main.tex && lp main.pdf
gk-equation-1 && latexmk -pdf main.tex && lp main.pdf
gk-equation-2 && latexmk -pdf main.tex && lp main.pdf
# gk-equation-3 && latexmk -pdf main.tex && lp main.pdf
gk-frac-1 && latexmk -pdf main.tex && lp main.pdf
#gk-clock && latexmk -pdf main.tex && lp main.pdf
#gk-word-problems && latexmk -xelatex main.tex && lp main.pdf
gk-fun-square -max-val 99 && latexmk -pdf main.tex && lp main.pdf
