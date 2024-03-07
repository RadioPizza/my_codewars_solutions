def narcissistic( value ):
    res = 0
    for i in str(value):
        res += pow(int(i), len(str(value)))
    if res == value: return True
    else: return False  