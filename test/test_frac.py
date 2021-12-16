from pysheet.frac import tikz_range, frac, tikz_slice, frac_node


def test_tikz_range():
    assert tikz_range(step=1) == r'{0,1,...,360}'
    assert tikz_range(step=10) == r'{0,10,...,360}'


def test_frac():
    assert frac(a=1, b=2) == r'\frac{1}{2}'
    assert frac(a=3, b=4) == r'\frac{3}{4}'


def test_tikz_slice():
    assert tikz_slice(step=10) == r'\foreach \r in{0,10,...,360}\draw[-] (0:0) -- (\r:2);'


def test_frac_node():
    assert frac_node(a=1, b=2) == r'\node[below] at (a.south) {\Huge $\frac{1}{2};'
