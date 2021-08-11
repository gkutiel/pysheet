def write_tex(
        cols=4,
        align='c',
        hs='3.5cm',
        vs='3cm',
        rows=[],
        commands='',
        file='main.tex'):
    array_def = (align + '@{\\hspace{\\hs}}') * cols
    with open(file, 'w') as f:
        f.write('''
            \\documentclass[12pt]{article}
            \\usepackage{fullpage}

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
