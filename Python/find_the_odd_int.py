# my sol
from collections import Counter

def find_it(seq):
    d = Counter(seq)
    for x,y in d.items():
        if y % 2 == 1:
            return x


# pythonic
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
