#!/bin/env python3  
# algo.py
# This file provides tests for algo.py and draw.py.

import matplotlib.pyplot as plt
from time import sleep

import para
import draw
import algo

# Constants
CONST_INFTY = 150
CONST_PAUSETIME = 5e-2
TYPE_LINE = 1
TYPE_CIRCLE = 2
TYPE_ELLIPSE = 3

def test():
	# draw.draw(1, algo.MpCircle(40), 0, 0)
	# draw.draw(2, algo.DDA(0, 0, 10, 3), 0, 0)
	draw.draw(3, algo.MpEllipse(30, 30), 0, 0)

if __name__ == '__main__':
	test()
	# plt.savefig('test.png', dpi = 200, bbox_inches = extent)
	