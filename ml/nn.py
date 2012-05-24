#!/bin/env python
from __future__ import division
import itertools
import operator
import random
import math
import sys

def compute(w, x):
    return reduce(operator.add, itertools.imap(operator.mul, w, x))

def strain(exp_set, w, ratio=0.000001):
    for exp in exp_set:
        t, real = exp
        v = compute(w, t)
        delta = map(lambda e: ratio * (real -v) * e, t)
        w = map(operator.add, w, delta)
    return w

def train(exp_set, w, ratio=0.00001):
    ratio = ratio/1000
    delta = (0, 0, 0)
    for exp in exp_set:
      t, real = exp
      v = compute(w, t)
      delta = map(operator.add, delta, map(lambda e: ratio * (real - v) * e, t))
    return map(operator.add, w, delta)

def lsm(exp_set, w):
    sum = 0
    for exp in exp_set:
      t, real = exp
      v = compute(w, t)
      sum += math.pow(real - v, 2)
    return sum

if __name__ == '__main__':
    ratio = float(sys.argv[1])
    low = 0
    high = 100
    w = (0.3, 0.5, 0.7)
    exp_set = []
    for i in  range(0, 1000):
        t = [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
        exp_set.append([t, compute(w, t)])

    #add noisy
    exp_set[100][1] = 0
    exp_set[200][1] = 0
    exp_set[300][1] = 0
    exp_set[900][1] = 0
    times = 0
    old_error = 0
    error = 1
    w = (0.1, 0.1, 0.1)
    while old_error != error:
        times += 1
        print "iteration times: ", times
        print w
        old_error = error
        error = lsm(exp_set, w)
        print error
        w = strain(exp_set, w, ratio)
    print "iteration times: ", times
