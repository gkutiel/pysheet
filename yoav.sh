#!/usr/local/bin/fish
gk-basic --add [100, 200] --sub [100, 200] --div [2, 20] --mul [2, 20]
latexmk -pdf main.tex
lp main.pdf
