#!/usr/local/bin/fish

for i in (seq 1 9); 
	gk-add -a 10 -b 100 --out yael/yael_add_$i.tex
	gk-sub -a 10 -b 100 --out yael/yael_sub_$i.tex
	gk-mul -a 2 -b 6 --out yael/yael_mul_$i.tex
	gk-div -a 2 -b 6 --out yael/yael_div_$i.tex
	gk-frac-4 --max-lcm 6 --out yael/yael$i.tex
end

latexmk -pdf --outdir=yael yael/yael_*.tex

