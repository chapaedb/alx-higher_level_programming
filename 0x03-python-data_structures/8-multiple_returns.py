#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    else:
        a = len(sentence)
        b = sentence[0]
    new_tup = (a, b)
    return new_tup
