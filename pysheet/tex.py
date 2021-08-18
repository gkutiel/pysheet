def write_tex(
        cols=4,
        align='c',
        hs='4cm',
        vs='3.9cm',
        font_size='14pt',
        rows=[],
        commands='',
        file='main.tex'):
    array_def = (align + '@{\\hspace{\\hs}}') * cols
    with open(file, 'w') as f:
        f.write('''
            \\documentclass[''' + font_size + ''']{extarticle}
            \\usepackage{fullpage}
            \\usepackage{tikz}
            \\thispagestyle{empty}
            \\usepackage[margin=1.5cm]{geometry}            


            \\def \\hs {''' + hs + '''}
            \\def \\vs {''' + vs + '''}

            ''' + commands + '''

            \\begin{document}

            \\[
                \\begin{array}{''' + array_def + '''}
            ''' + '\\\\[\\vs]'.join(rows) + '''
                \\end{array}
            \\]

            \\end{document}    
        '''
                )


if __name__ == '__main__':
    write_tex(
        hs='5cm',
        vs='5cm',
        rows=['1 & 2 & 3 & 4', '1 & 2 & 3 & 4'])
