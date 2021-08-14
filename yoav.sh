#!/usr/local/bin/fish
gk-equation-1 && latexmk -pdf main.tex && lp main.pdf
gk-equation-2 && latexmk -pdf main.tex && lp main.pdf
gk-equation-3 && latexmk -pdf main.tex && lp main.pdf

gk-frac-1 && latexmk -pdf main.tex && lp main.pdf
