#!/usr/local/bin/fish
python main.py
latexmk -pdf main.tex
lp main.pdf
