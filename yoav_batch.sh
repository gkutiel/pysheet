#!/usr/local/bin/fish

for i in (seq 1 9); 
	gk-add -a 10 -b 1000 --out yoav/yoav_add_$i.tex
	gk-sub -a 10 -b 1000 --out yoav/yoav_sub_$i.tex
	gk-mul -a 2 -b 30 --out yoav/yoav_mul_$i.tex
	gk-div -a 2 -b 30 --out yoav/yoav_div_$i.tex
	gk-frac-4 --max-lcm 18 --out yoav/yoav_frac_$i.tex
end

latexmk -pdf --outdir=yoav yoav/yoav_*.tex

