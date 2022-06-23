#!/usr/local/bin/fish

gk-add -a 10 -b 1000 --out yoav/add.tex
gk-sub -a 10 -b 1000 --out yoav/sub.tex
gk-mul -a 2 -b 30 --out yoav/mul.tex
gk-div -a 2 -b 30 --out yoav/div.tex

latexmk -pdf --outdir=yoav yoav/*.tex
