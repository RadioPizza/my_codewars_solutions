def xo(s):
    x, o = 0, 0
    for i in s:
        if i in ('x', 'X'): x += 1
        if i in ('o','O'): o += 1
    return x == o