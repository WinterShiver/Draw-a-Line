#!/bin/env python3  
# draw.py
# This file provides drawing function based on plt, given pointList and the type of symmetry.
import matplotlib.pyplot as plt

# Constants
CONST_INFTY = 150
CONST_PAUSETIME = 5e-2
TYPE_LINE = 1
TYPE_CIRCLE = 2
TYPE_ELLIPSE = 3

def draw(type, pointList, centerX, centerY, pointColor = "blue"):
	# Axis Initialization
	plt.ion()
	drawAxis()
	# Decide Type
	if type == TYPE_LINE:
		draw1(pointList, pointColor)
	elif type == TYPE_CIRCLE:
		draw8(pointList, centerX, centerY, pointColor)
	elif type == TYPE_ELLIPSE:
		draw4(pointList, centerX, centerY, pointColor)
	plt.ioff()
	plt.draw()

def drawAxis():
	plt.xlim(-CONST_INFTY * 4 / 3, CONST_INFTY * 4 / 3) # Set the range 
	plt.ylim(-CONST_INFTY, CONST_INFTY)
	plt.xlabel("X-Axis") # Set the label
	plt.ylabel("Y-Axis")

def draw1(pointList, pointColor):
	for i in range(len(pointList)):
		[x, y] = pointList[i]
		plt.scatter(x, y, color = pointColor)
		plt.pause(CONST_PAUSETIME)

def draw8(pointList, centerX, centerY, pointColor):
	plt.scatter(centerX, centerY, color = pointColor)
	plt.pause(CONST_PAUSETIME)
	for i in range(len(pointList)):
		[x, y] = pointList[i]
		plt.scatter(x + centerX, y + centerY, color = pointColor)
		plt.scatter(-x + centerX, y + centerY, color = pointColor)
		plt.scatter(x + centerX, -y + centerY, color = pointColor)
		plt.scatter(-x + centerX, -y + centerY, color = pointColor)
		plt.scatter(y + centerX, x + centerY, color = pointColor)
		plt.scatter(-y + centerX, x + centerY, color = pointColor)
		plt.scatter(y + centerX, -x + centerY, color = pointColor)
		plt.scatter(-y + centerX, -x + centerY, color = pointColor)
		plt.pause(CONST_PAUSETIME)

def draw4(pointList, centerX, centerY, pointColor):
	plt.scatter(centerX, centerY, color = pointColor)
	plt.pause(CONST_PAUSETIME)
	for i in range(len(pointList)):
		[x, y] = pointList[i]
		plt.scatter(x + centerX, y + centerY, color = pointColor)
		plt.scatter(-x + centerX, y + centerY, color = pointColor)
		plt.scatter(x + centerX, -y + centerY, color = pointColor)
		plt.scatter(-x + centerX, -y + centerY, color = pointColor)
		plt.pause(CONST_PAUSETIME)
