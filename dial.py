#!/bin/env python3  
# dial.py
# This file places the definition of input dialogs, for the 4 algorithms.

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QInputDialog, QGridLayout, QLabel, QPushButton, QFrame 

from draw import *
from algo import *

# Constants
CONST_INFTY = 150
CONST_COLOR = ["Red", "Blue", "Green", "Black"]
TYPE_LINE = 1
TYPE_CIRCLE = 2
TYPE_ELLIPSE = 3

class InputDialogDDA(QWidget): 
	def __init__(self): 
		super(InputDialogDDA,self).__init__() 
		self.initUi() 
	def initUi(self): 
		self.setWindowTitle("Drawing Information: DDA") 
		self.setGeometry(400,400,300,260) 

		# Labels
		labelBeginX = QLabel("Begin Point, X:")
		labelBeginY = QLabel("Y:")
		labelEndX = QLabel("End Point, X:")
		labelEndY = QLabel("Y:")
		labelColor = QLabel("Color:")

		self.bxLabel = QLabel("0") 
		self.bxLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken) 
		self.byLabel = QLabel("0") 
		self.byLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken)
		self.exLabel = QLabel("0") 
		self.exLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken) 
		self.eyLabel = QLabel("0") 
		self.eyLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken) 
		self.colorLabel = QLabel("Blue") 
		self.colorLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken)

		bxButton=QPushButton("Set X") 
		bxButton.clicked.connect(self.selectBxNumber)
		byButton=QPushButton("Set Y") 
		byButton.clicked.connect(self.selectByNumber)
		exButton=QPushButton("Set X") 
		exButton.clicked.connect(self.selectExNumber)
		eyButton=QPushButton("Set Y") 
		eyButton.clicked.connect(self.selectEyNumber) 
		colorButton=QPushButton("Set Color") 
		colorButton.clicked.connect(self.selectColor)
		drawButton=QPushButton("Draw Now!")
		drawButton.clicked.connect(self.drawNow)
		
		mainLayout=QGridLayout() 
		mainLayout.addWidget(labelBeginX,0,0) 
		mainLayout.addWidget(self.bxLabel,0,1) 
		mainLayout.addWidget(bxButton,0,2) 
		mainLayout.addWidget(labelBeginY,0,3) 
		mainLayout.addWidget(self.byLabel,0,4) 
		mainLayout.addWidget(byButton,0,5) 
		mainLayout.addWidget(labelEndX,1,0) 
		mainLayout.addWidget(self.exLabel,1,1) 
		mainLayout.addWidget(exButton,1,2) 
		mainLayout.addWidget(labelEndY,1,3) 
		mainLayout.addWidget(self.eyLabel,1,4) 
		mainLayout.addWidget(eyButton,1,5) 
		mainLayout.addWidget(labelColor,2,0) 
		mainLayout.addWidget(self.colorLabel,2,1)
		mainLayout.addWidget(colorButton,2,2)
		mainLayout.addWidget(drawButton,3,0)
		self.setLayout(mainLayout) 

	def selectBxNumber(self): 
		number,ok = QInputDialog.getInt(self,"Input a Number","Please Input a Number:",int(self.bxLabel.text()), min = -CONST_INFTY, max = CONST_INFTY, step = 1) 
		if ok : 
			self.bxLabel.setText(str(number)) 
	def selectByNumber(self): 
		number,ok = QInputDialog.getInt(self,"Input a Number","Please Input a Number:",int(self.byLabel.text()), min = -CONST_INFTY, max = CONST_INFTY, step = 1) 
		if ok : 
			self.byLabel.setText(str(number)) 
	def selectExNumber(self): 
		number,ok = QInputDialog.getInt(self,"Input a Number","Please Input a Number:",int(self.exLabel.text()), min = -CONST_INFTY, max = CONST_INFTY, step = 1) 
		if ok : 
			self.exLabel.setText(str(number)) 
	def selectEyNumber(self): 
		number,ok = QInputDialog.getInt(self,"Input a Number","Please Input a Number:",int(self.eyLabel.text()), min = -CONST_INFTY, max = CONST_INFTY, step = 1) 
		if ok : 
			self.eyLabel.setText(str(number))
	def selectColor(self): 
		color,ok = QInputDialog.getItem(self,"Select Color","Please Select a Color:", CONST_COLOR) 
		if ok : 
			self.colorLabel.setText(color)
	def drawNow(self):
		x1 = int(self.bxLabel.text())
		y1 = int(self.byLabel.text())
		x2 = int(self.exLabel.text())
		y2 = int(self.eyLabel.text())
		color = self.colorLabel.text()
		pointList = DDA(x1, y1, x2, y2)
		draw(TYPE_LINE, pointList, 0, 0, color)

class InputDialogBresenham(QWidget): 
	def __init__(self): 
		super(InputDialogBresenham,self).__init__() 
		self.initUi() 
	def initUi(self): 
		self.setWindowTitle("Drawing Information: Bresenham") 
		self.setGeometry(400,400,300,260) 

		# Labels
		labelBeginX = QLabel("Begin Point, X:")
		labelBeginY = QLabel("Y:")
		labelEndX = QLabel("End Point, X:")
		labelEndY = QLabel("Y:")
		labelColor = QLabel("Color:")

		self.bxLabel = QLabel("0") 
		self.bxLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken) 
		self.byLabel = QLabel("0") 
		self.byLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken)
		self.exLabel = QLabel("0") 
		self.exLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken) 
		self.eyLabel = QLabel("0") 
		self.eyLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken) 
		self.colorLabel = QLabel("Blue") 
		self.colorLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken)

		bxButton=QPushButton("Set X") 
		bxButton.clicked.connect(self.selectBxNumber)
		byButton=QPushButton("Set Y") 
		byButton.clicked.connect(self.selectByNumber)
		exButton=QPushButton("Set X") 
		exButton.clicked.connect(self.selectExNumber)
		eyButton=QPushButton("Set Y") 
		eyButton.clicked.connect(self.selectEyNumber) 
		colorButton=QPushButton("Set Color") 
		colorButton.clicked.connect(self.selectColor)
		drawButton=QPushButton("Draw Now!")
		drawButton.clicked.connect(self.drawNow)
		
		mainLayout=QGridLayout() 
		mainLayout.addWidget(labelBeginX,0,0) 
		mainLayout.addWidget(self.bxLabel,0,1) 
		mainLayout.addWidget(bxButton,0,2) 
		mainLayout.addWidget(labelBeginY,0,3) 
		mainLayout.addWidget(self.byLabel,0,4) 
		mainLayout.addWidget(byButton,0,5) 
		mainLayout.addWidget(labelEndX,1,0) 
		mainLayout.addWidget(self.exLabel,1,1) 
		mainLayout.addWidget(exButton,1,2) 
		mainLayout.addWidget(labelEndY,1,3) 
		mainLayout.addWidget(self.eyLabel,1,4) 
		mainLayout.addWidget(eyButton,1,5) 
		mainLayout.addWidget(labelColor,2,0) 
		mainLayout.addWidget(self.colorLabel,2,1)
		mainLayout.addWidget(colorButton,2,2)
		mainLayout.addWidget(drawButton,3,0)
		self.setLayout(mainLayout) 

	def selectBxNumber(self): 
		number,ok = QInputDialog.getInt(self,"Input a Number","Please Input a Number:",int(self.bxLabel.text()), min = -CONST_INFTY, max = CONST_INFTY, step = 1) 
		if ok : 
			self.bxLabel.setText(str(number)) 
	def selectByNumber(self): 
		number,ok = QInputDialog.getInt(self,"Input a Number","Please Input a Number:",int(self.byLabel.text()), min = -CONST_INFTY, max = CONST_INFTY, step = 1) 
		if ok : 
			self.byLabel.setText(str(number)) 
	def selectExNumber(self): 
		number,ok = QInputDialog.getInt(self,"Input a Number","Please Input a Number:",int(self.exLabel.text()), min = -CONST_INFTY, max = CONST_INFTY, step = 1) 
		if ok : 
			self.exLabel.setText(str(number)) 
	def selectEyNumber(self): 
		number,ok = QInputDialog.getInt(self,"Input a Number","Please Input a Number:",int(self.eyLabel.text()), min = -CONST_INFTY, max = CONST_INFTY, step = 1) 
		if ok : 
			self.eyLabel.setText(str(number))
	def selectColor(self): 
		color,ok = QInputDialog.getItem(self,"Select Color","Please Select a Color:", CONST_COLOR) 
		if ok : 
			self.colorLabel.setText(color)
	def drawNow(self):
		x1 = int(self.bxLabel.text())
		y1 = int(self.byLabel.text())
		x2 = int(self.exLabel.text())
		y2 = int(self.eyLabel.text())
		color = self.colorLabel.text()
		pointList = Bresenham(x1, y1, x2, y2)
		draw(TYPE_LINE, pointList, 0, 0, color)

class InputDialogMpCircle(QWidget): 
	def __init__(self): 
		super(InputDialogMpCircle,self).__init__() 
		self.initUi() 
	def initUi(self): 
		self.setWindowTitle("Drawing Information: MpCircle") 
		self.setGeometry(400,400,300,260) 

		# Labels
		labelCenterX = QLabel("Center Point, X:")
		labelCenterY = QLabel("Y:")
		labelRadius = QLabel("Radius:")
		labelColor = QLabel("Color:")

		self.cxLabel = QLabel("0") 
		self.cxLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken) 
		self.cyLabel = QLabel("0") 
		self.cyLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken)
		self.rLabel = QLabel("1") 
		self.rLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken) 
		self.colorLabel = QLabel("Blue") 
		self.colorLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken)

		cxButton=QPushButton("Set X") 
		cxButton.clicked.connect(self.selectCxNumber)
		cyButton=QPushButton("Set Y") 
		cyButton.clicked.connect(self.selectCyNumber)
		rButton=QPushButton("Set R") 
		rButton.clicked.connect(self.selectRNumber)
		colorButton=QPushButton("Set Color") 
		colorButton.clicked.connect(self.selectColor)
		drawButton=QPushButton("Draw Now!")
		drawButton.clicked.connect(self.drawNow)
		
		mainLayout=QGridLayout() 
		mainLayout.addWidget(labelCenterX,0,0) 
		mainLayout.addWidget(self.cxLabel,0,1) 
		mainLayout.addWidget(cxButton,0,2) 
		mainLayout.addWidget(labelCenterY,0,3) 
		mainLayout.addWidget(self.cyLabel,0,4) 
		mainLayout.addWidget(cyButton,0,5) 
		mainLayout.addWidget(labelRadius,1,0) 
		mainLayout.addWidget(self.rLabel,1,1) 
		mainLayout.addWidget(rButton,1,2) 
		mainLayout.addWidget(labelColor,2,0) 
		mainLayout.addWidget(self.colorLabel,2,1)
		mainLayout.addWidget(colorButton,2,2)
		mainLayout.addWidget(drawButton,3,0)
		self.setLayout(mainLayout) 

	def selectCxNumber(self): 
		number,ok = QInputDialog.getInt(self,"Input a Number","Please Input a Number:",int(self.cxLabel.text()), min = -CONST_INFTY, max = CONST_INFTY, step = 1) 
		if ok : 
			self.cxLabel.setText(str(number)) 
	def selectCyNumber(self): 
		number,ok = QInputDialog.getInt(self,"Input a Number","Please Input a Number:",int(self.cyLabel.text()), min = -CONST_INFTY, max = CONST_INFTY, step = 1) 
		if ok : 
			self.cyLabel.setText(str(number)) 
	def selectRNumber(self): 
		number,ok = QInputDialog.getInt(self,"Input a Number","Please Input a Number:",int(self.rLabel.text()), min = 1, max = CONST_INFTY, step = 1) 
		if ok : 
			self.rLabel.setText(str(number)) 
	def selectColor(self): 
		color,ok = QInputDialog.getItem(self,"Select Color","Please Select a Color:", CONST_COLOR) 
		if ok : 
			self.colorLabel.setText(color)
	def drawNow(self):
		x = int(self.cxLabel.text())
		y = int(self.cyLabel.text())
		r = int(self.rLabel.text())
		color = self.colorLabel.text()
		pointList = MpCircle(r)
		draw(TYPE_CIRCLE, pointList, x, y, color)

class InputDialogMpEllipse(QWidget): 
	def __init__(self): 
		super(InputDialogMpEllipse,self).__init__() 
		self.initUi() 
	def initUi(self): 
		self.setWindowTitle("Drawing Information: MpEllipse") 
		self.setGeometry(400,400,300,260) 

		# Labels
		labelCenterX = QLabel("Center Point, X:")
		labelCenterY = QLabel("Y:")
		labelA = QLabel("A(Rx):")
		labelB = QLabel("B(Ry):")
		labelColor = QLabel("Color:")

		self.cxLabel = QLabel("0") 
		self.cxLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken) 
		self.cyLabel = QLabel("0") 
		self.cyLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken)
		self.aLabel = QLabel("1") 
		self.aLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken) 
		self.bLabel = QLabel("1") 
		self.bLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken) 
		self.colorLabel = QLabel("Blue") 
		self.colorLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken)

		cxButton=QPushButton("Set X") 
		cxButton.clicked.connect(self.selectCxNumber)
		cyButton=QPushButton("Set Y") 
		cyButton.clicked.connect(self.selectCyNumber)
		aButton=QPushButton("Set A") 
		aButton.clicked.connect(self.selectANumber)
		bButton=QPushButton("Set B") 
		bButton.clicked.connect(self.selectBNumber)
		colorButton=QPushButton("Set Color") 
		colorButton.clicked.connect(self.selectColor)
		drawButton=QPushButton("Draw Now!")
		drawButton.clicked.connect(self.drawNow)
		
		mainLayout=QGridLayout() 
		mainLayout.addWidget(labelCenterX,0,0) 
		mainLayout.addWidget(self.cxLabel,0,1) 
		mainLayout.addWidget(cxButton,0,2) 
		mainLayout.addWidget(labelCenterY,0,3) 
		mainLayout.addWidget(self.cyLabel,0,4) 
		mainLayout.addWidget(cyButton,0,5) 
		mainLayout.addWidget(labelA,1,0) 
		mainLayout.addWidget(self.aLabel,1,1) 
		mainLayout.addWidget(aButton,1,2) 
		mainLayout.addWidget(labelB,1,3) 
		mainLayout.addWidget(self.bLabel,1,4) 
		mainLayout.addWidget(bButton,1,5) 
		mainLayout.addWidget(labelColor,2,0) 
		mainLayout.addWidget(self.colorLabel,2,1)
		mainLayout.addWidget(colorButton,2,2)
		mainLayout.addWidget(drawButton,3,0)
		self.setLayout(mainLayout) 

	def selectCxNumber(self): 
		number,ok = QInputDialog.getInt(self,"Input a Number","Please Input a Number:",int(self.cxLabel.text()), min = -CONST_INFTY, max = CONST_INFTY, step = 1) 
		if ok : 
			self.cxLabel.setText(str(number)) 
	def selectCyNumber(self): 
		number,ok = QInputDialog.getInt(self,"Input a Number","Please Input a Number:",int(self.cyLabel.text()), min = -CONST_INFTY, max = CONST_INFTY, step = 1) 
		if ok : 
			self.cyLabel.setText(str(number)) 
	def selectANumber(self): 
		number,ok = QInputDialog.getInt(self,"Input a Number","Please Input a Number:",int(self.aLabel.text()), min = 1, max = CONST_INFTY, step = 1) 
		if ok : 
			self.aLabel.setText(str(number)) 
	def selectBNumber(self): 
		number,ok = QInputDialog.getInt(self,"Input a Number","Please Input a Number:",int(self.bLabel.text()), min = 1, max = CONST_INFTY, step = 1) 
		if ok : 
			self.bLabel.setText(str(number)) 
	def selectColor(self): 
		color,ok = QInputDialog.getItem(self,"Select Color","Please Select a Color:", CONST_COLOR) 
		if ok : 
			self.colorLabel.setText(color)
	def drawNow(self):
		x = int(self.cxLabel.text())
		y = int(self.cyLabel.text())
		a = int(self.aLabel.text())
		b = int(self.bLabel.text())
		color = self.colorLabel.text()
		pointList = MpEllipse(a, b)
		draw(TYPE_ELLIPSE, pointList, x, y, color)