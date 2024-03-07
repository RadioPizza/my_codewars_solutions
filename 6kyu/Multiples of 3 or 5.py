def solution(number):
    l = []
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            l.append(i)
    return sum(l)