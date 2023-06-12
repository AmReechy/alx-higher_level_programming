#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        t = len(sentence), None
        return t
    else:
        mult_tup = len(sentence), sentence[0]
        return mult_tup
