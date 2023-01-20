#!/usr/local/bin/fish

set i (date +'%d')
gk-add -a 10 -b 100 --out yael/add_$i.tex
gk-sub -a 10 -b 100 --out yael/sub_$i.tex
gk-mul -a 2 -b 5 --out yael/mul_$i.tex
gk-div -a 2 -b 5 --out yael/div_$i.tex

latexmk -pdf --outdir=yael yael/*.tex
