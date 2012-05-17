#!/bin/env python
from __future__ import division
import itertools
import operator
import random

def compute(w, x):
    return reduce(operator.add, itertools.imap(operator.product, w, x))

def train(exp_set, w):
    ratio = 0.01
    for exp in exp_set:
        t, real = exp
        v = compute(w, x)
        delta = map(lambda e: ratio(real -v) * e)

if __name__ == '__main__':
    low = 0
    high = 100
    w = (0.3, 0.5, 0.7)
    exp_set = []
    for i in  range(0, 1000):
        t = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
        exp_set.append((t, compute(w, t)))
