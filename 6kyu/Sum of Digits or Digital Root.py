def digital_root(n):
    res = sum(list(map(int, str(n))))
    while len(str(res)) > 1:
        res = sum(list(map(int, str(res))))
    return res