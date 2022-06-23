#!/usr/local/bin/fish

gk-arithmetic --add [10,600] --sub [10,600] --mul [2,30] --div [2,30] --out yoav/arit1.tex
gk-arithmetic --add [10,600] --sub [10,600] --mul [2,30] --div [2,30] --out yoav/arit2.tex
gk-arithmetic --add [1,200] 
gk-equation-1 --out 'yoav/eq1.tex'
gk-equation-2 --out 'yoav/eq2.tex'
gk-equation-3 --out 'yoav/eq3.tex'
gk-clock --out 'yoav/clock.tex'

# gk-word-problems && latexmk -xelatex main.tex && lp main.pdf
# gk-frac-1 && latexmk -pdf main.tex && lp main.pdf
# gk-fun-square && latexmk -pdf main.tex && lp main.pdf

latexmk -pdf --outdir=yoav yoav/*.tex
