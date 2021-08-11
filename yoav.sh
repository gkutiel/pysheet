#!/usr/local/bin/fish
gk-equation
latexmk -pdf main.tex
lp main.pdf
