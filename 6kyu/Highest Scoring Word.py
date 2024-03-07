def high(x):
    scores = []
    for word in x.split():
        scores.append(score(word))
    return x.split()[scores.index(max(scores))]

def score(word):
    return sum([ord(word[i])-96 for i in range(len(word))])