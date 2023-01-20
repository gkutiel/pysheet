#!/usr/local/bin/fish

set i (date +'%d')
gk-add -a 10 -b 1000 --out yoav/add_$i.tex
gk-sub -a 10 -b 1000 --out yoav/sub_$i.tex
gk-mul -a 2 -b 30 --out yoav/mul_$i.tex
gk-div -a 2 -b 30 --out yoav/div_$i.tex

latexmk -pdf --outdir=yoav yoav/*.tex
