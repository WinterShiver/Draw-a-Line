#!/bin/env python3
# algo.py
# This file provides graphic algorithms, with all the functions return the list of points.

import matplotlib.pyplot as plt

def DDA(x1, y1, x2, y2):
	pointList = []
	if x1 == x2: # Special Case: Horizenal Line
		if y1 <= y2:
			# return [[x1, y] for y in np.arange(y1, y2 + 1)]
			return [[x1, y] for y in range(y1, y2 + 1)]
		else:
			pointList = [[x1, y] for y in range(y2, y1 + 1)]
			pointList.reverse()
			return pointList
	elif y2 - y1 <= x2 - x1: # abs(slope) <= 1
		return _DDA(x1, y1, x2, y2)
	else: # abs(slope) >= 1: Axis Reverse
		pointList = _DDA(y1, x1, y2, x2)
		return [[p[1], p[0]] for p in pointList]
		

def _DDA(x1, y1, x2, y2): # abs(slope) <= 1
	# Parameter of Drawing
	slope = (y2 - y1) / (x2 - x1)
	[x, y] = [x1, y1]
	pointList = []
	# Real DDA Algorithm
	if x1 < x2:
		while x <= x2:
			pointList.append([x, round(y)])
			[x, y] = [x + 1, y + slope]
	else:
		while x >= x2:
			pointList.append([x, round(y)])
			[x, y] = [x - 1, y - slope]
	return pointList


def Bresenham(x1, y1, x2, y2):
	pointList = []
	if x1 == x2: # Special Case: Horizenal Line
		if y1 <= y2:
			return [[x1, y] for y in range(y1, y2 + 1)]
		else:
			pointList = [[x1, y] for y in range(y2, y1 + 1)]
			pointList.reverse()
			return pointList
	elif abs(y2 - y1) <= abs(x2 - x1): # abs(slope) <= 1
		return _Bresenham(x1, y1, x2, y2)
	else: # abs(slope) >= 1: Axis Reverse
		pointList = _Bresenham(y1, x1, y2, x2)
		return [[p[1], p[0]] for p in pointList]

def _Bresenham(x1, y1, x2, y2): # abs(slope) <= 1
	# Parameter of Drawing
	slope = (y2 - y1) / (x2 - x1)
	# Initialize
	p = 2 * slope - 1
	[x, y] = [x1, y1]
	pointList = []
	if x1 < x2:
		if slope >= 0:
			# Real Bresenham Algorithm
			while True:
				pointList.append([x, y])
				if x == x2:
					return pointList
				if p <= 0:
					[x, y, p] = [x + 1, y, p + 2 * slope]
				else:
					[x, y, p] = [x + 1, y + 1, p + 2 * slope - 2]
		else: # Up-Down Symmetry
			pointList = _Bresenham(x1, -y1, x2, -y2)
			return [[p[0], -p[1]] for p in pointList]
	else:# Left-Right Symmetry
		pointList = _Bresenham(x2, y2, x1, y1)
		pointList.reverse()
		return pointList

def MpCircle(r):
	# Initialize
	[x, y] = [0, r]
	pointList = []
	p = 5 / 4 - r
	# Mid-Point Circle Algorithm
	while x <= y:
		pointList.append([x, y])
		if p < 0:
			[x, y, p] = [x + 1, y, p + 2 * x + 3]
		else:
			[x, y, p] = [x + 1, y - 1, p + 2 * x + 5 - 2 * y]
	return pointList

def MpEllipse(a, b): # From (0, b) to (a, 0)
	# Constants
	[aa, ab, bb] = [a * a, a * b, b * b]
	# Initialize 1
	[x, y] = [0, b]
	pointList = []
	p = bb - aa * b + aa / 4
	# Mid-Point Ellipse Algorithm 1
	while 2 * bb * x < 2 * aa * y:
		pointList.append([x, y])
		if p < 0:
			[x, y, p] = [x + 1, y, p + 2 * bb * x + 3 * bb]
		else:
			[x, y, p] = [x + 1, y - 1, p + 2 * bb * x + 3 * bb - 2 * aa * (y - 1)]
	# Initialize 2
	p = bb * (x + 1 / 2) * (x + 1 / 2) + aa * (y - 1) * (y - 1) - aa * bb
	# Mid-Point Ellipse Algorithm 1
	while y >= 0:
		pointList.append([x, y])
		if p > 0:
			[x, y, p] = [x, y - 1, p - 2 * aa * y + 3 * aa]
		else:
			[x, y, p] = [x + 1, y - 1, p - 2 * aa * y + 3 * aa + 2 * bb * (x + 1)]
	return pointList
	




def test():
	pass


if __name__ == '__main__':
	test()
