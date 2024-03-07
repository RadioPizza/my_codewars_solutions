def square_sum(numbers):
    res = 0
    for number in numbers:
        res += number ** 2
    return res

square_sum = lambda l: sum(n*n for n in l)