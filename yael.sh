#!/usr/local/bin/fish
latexmk -c && gk-arithmetic --add [1,200] && latexmk -pdf main.tex && lp main.pdf
latexmk -c && gk-equation-1 -a [1,1] -x [3,10] -b [1,2] && latexmk -pdf main.tex && lp main.pdf
latexmk -c && gk-clock && latexmk -pdf main.tex && lp main.pdf
gk-fun-square -n 5 -op '+' && latexmk -pdf main.tex && lp main.pdf

# latexmk -c && gk-word-problems --max-x 3  --max-a 3 --max-b 10 && latexmk -pdf main.tex && lp main.pdf
