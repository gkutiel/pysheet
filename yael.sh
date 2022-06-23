#!/usr/local/bin/fish

gk-add -a 10 -b 100 --out yael/add.tex
gk-sub -a 10 -b 100 --out yael/sub.tex
gk-mul -a 2 -b 5 --out yael/mul.tex
gk-div -a 2 -b 5 --out yael/div.tex

latexmk -pdf --outdir=yael yael/*.tex
