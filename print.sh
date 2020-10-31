#!/usr/local/bin/fish
if test (count $argv) -gt 0
    set config $argv[1]
else
    set config 'config.json'
end
python main.py --config-json $config
latexmk -pdf main.tex
lp main.pdf
