#!/bin/env python
import numpy as np
import matplotlib.pyplot as plt

def gen_normal_points(mu, sigma, num):
  s1 = np.random.normal(mu, sigma, num)
  s2 = np.random.normal(mu, sigma, num)
  return s1, s2


if __name__ == '__main__':
#  plt.plot(np.arange(0, 5, 0.1), np.cos(np.arange(0, 5, 0.1) * np.pi), 'r.')  #plot as reb circle
  x1, y1 = gen_normal_points(1, 1, 1000)
  x2, y2 = gen_normal_points(5, 1, 1000)
  plt.plot(x1, y1, "r.")
  plt.plot(x2, y2, "b.")


  #draw a line
  x = np.arange(-4, 10, 0.1)
  y = x * (-1) + 5
  plt.plot(x, y, "g")

  #text
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("logistic regression")
  plt.text(-2, 7, "discrimitive line")
  plt.annotate("center", xy=(1, 1), xytext = (1, -4), \
    arrowprops=dict(facecolor='black', shrink=0.01, width = 1))

  #optional: set axis
  ax = plt.axis([-4, 12, -4, 12])
  plt.show()

