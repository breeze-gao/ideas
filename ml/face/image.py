#!/bin/env python

import sys
import operator
import os.path

def get_mark(path):
    name = os.path.basename(path)
    t = name.split("_")
    return (t[1], t[2], t[3])


class Image:
    def __init__(self, path):
        self.path = path
        self._read()
        self.mark = get_mark(path)
    def _read(self):
        f = open(self.path)
        self.type = f.readline().rstrip()
        self.col, self.row = map(int, f.readline().rstrip().split(None, 2))
        self.max_value = int(f.readline().rstrip())
        self.data = f.read()
    def __str__(self):
        return "\t".join((self.path, self.type, str(self.col), str(self.row), str(self.max_value), str(self.mark), str(len(self.data))))

def mark(img):
    assert img.__class__.__name__ == 'Image'
    return img.mark
def data(img):
    assert img.__class__.__name__ == 'Image'
    return img.data

if __name__ == '__main__':
    img = Image("/home/easy/Documents/face/faces_4/an2i/an2i_up_neutral_open_4.pgm")
    print mark(img)
    print img
