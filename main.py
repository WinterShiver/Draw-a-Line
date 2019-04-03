#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QInputDialog, QGridLayout, QLabel, QPushButton, QFrame 
from matplotlib.widgets import Button,RadioButtons
import matplotlib.pyplot as plt
import sys

from draw import *
from algo import *
from dial import *

def pressEvent(label):
    app = QApplication(sys.argv)
    if label == "DDA":
        myshow = InputDialogDDA() 
    elif label == "Bresenham":
        myshow = InputDialogBresenham()
    elif label == "Mid-Point Circle":
        myshow = InputDialogMpCircle()
    elif label == "Mid-Point Ellipse":
        myshow = InputDialogMpEllipse()
    else:
        pass
    myshow.show()
    sys.exit(app.exec_())

if __name__=="__main__": 
    # Initialize
    fig = plt.figure()
    # Multiple Button
    rax = plt.axes([0.65, 0.8, 0.25, 0.15])
    algoList = ("DDA", "Bresenham", "Mid-Point Circle", "Mid-Point Ellipse")
    radio = RadioButtons(rax, algoList)
    radio.on_clicked(pressEvent)
    # Draw
    ax = plt.axes([0.15, 0.15, 0.6, 0.6])
    fig.add_axes(ax)
    drawAxis()
    plt.show()
    
    '''
    # Button DDA
    pointDDA = plt.axes([0,0.03,0.1,0.03])
    global buttonDDA
    buttonDDA = Button(pointDDA, "DDA")
    buttonDDA.on_clicked(pressDDA)
    '''