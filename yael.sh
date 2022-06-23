#!/usr/local/bin/fish
gk-arithmetic --add [10,200] --sub [1,30] --mul [2,11] --div [2,11] --out 'yael/arit1.tex'
gk-arithmetic --add [10,200] --sub [1,30] --mul [2,11] --div [2,11] --out 'yael/arit2.tex'
gk-equation-1 -a [1,1] -x [3,10] -b [1,2] --out 'yael/eq1.tex'
gk-clock --out 'yael/clock.tex'
gk-fun-square -n 5 -op '+' --out 'yael/squr.tex'

latexmk -pdf --outdir=yael yael/*.tex
