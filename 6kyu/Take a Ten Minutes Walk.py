def is_valid_walk(walk):
    return len(walk) == 10 and walk.count('w') == walk.count('e') and walk.count('n') == walk.count('s')