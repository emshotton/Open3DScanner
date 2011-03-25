#!/usr/bin/python

#Splinesweep software.
#Version 1.0 - Withnail
#by Matthew Shotton
#licenced under GPLv3.0 see http://www.gnu.org/licenses/gpl-3.0.txt

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

def createlineimage(image):
    print "Creating line image"
    for y in range(image.height()):
        max_value = 0
        max_position = 0
        for x in range(image.width()):
            pixel = image.pixel(x,y)
            if QtGui.qRed(pixel) > max_value:
                max_value = QtGui.qRed(pixel)
                max_position = x
            pixel = QtGui.qRgb(0,0,0)
            image.setPixel(x,y,pixel)
        pixel = QtGui.qRgb(max_value,0,0)
        image.setPixel(max_position,y,pixel)
    

class ScanImageDisplay(QtGui.QWidget):
    def __init__(self):
        super(ScanImageDisplay,self).__init__()      
        self.__initUI()

    def __initUI(self):
        #init viewing area
        layout = QtGui.QGridLayout()
        self.__imagelabel = QtGui.QLabel()
        self.__lineimagelabel = QtGui.QLabel()
        layout.addWidget(self.__imagelabel)
        layout.addWidget(self.__lineimagelabel)
        self.setLayout(layout)
        #Init control area
        
    def setImage(self,image):
        print "Setting image"
        display_image = image.scaledToWidth(400)
        self.__imagelabel.setPixmap(QtGui.QPixmap.fromImage(display_image))

    def setLineImage(self,image):
        print "Setting image"
        display_image = image.scaledToWidth(400)
        self.__lineimagelabel.setPixmap(QtGui.QPixmap.fromImage(display_image))


class GUI(QtGui.QWidget):
    def __init__(self):
        super(GUI, self).__init__()
        self.rotations = 300 
        self.__initUI()
        
    def __initUI(self):
        layout = QtGui.QGridLayout()
        self.scandisplay = ScanImageDisplay()
        img = QtGui.QImage()
        img.load("1.png")
        self.scandisplay.setImage(img)
        createlineimage(img)
        self.scandisplay.setLineImage(img)
        layout.addWidget(self.scandisplay)
        self.__progressbar = QtGui.QProgressBar()
        self.__progressbar.setRange(0,self.rotations)
        layout.addWidget(self.__progressbar)
        self.setWindowTitle('Splinesweep v1.0 - \"Withnail\"')
        #Initializing control widget        
        self.controlwidget = QtGui.QWidget()  
        self.controllayout = QtGui.QGridLayout()
        self.controlwidget.rotation_spinbox = QtGui.QSpinBox()
        self.controlwidget.rotation_spinbox.setRange(0,10000)
        self.controlwidget.rotation_spinbox.setValue(300)
        self.controlwidget.rotation_label = QtGui.QLabel("Number of rotations")
        self.controllayout.addWidget(self.controlwidget.rotation_label,0,0)
        self.controllayout.addWidget(self.controlwidget.rotation_spinbox,0,1)
        self.controlwidget.setLayout(self.controllayout)
        layout.addWidget(self.controlwidget,0,1,2,1)
        self.setLayout(layout)
        #Connecting signals/slots
        self.connect(self.controlwidget.rotation_spinbox,QtCore.SIGNAL("valueChanged(int)"),self.setRotations)
        

    def setRotations(self,rotations):
        print "setting rotation: "+str(rotations)
        self.rotations = rotations
        self.__progressbar.setRange(0,self.rotations)


app = QtGui.QApplication(sys.argv)
ex = GUI()
ex.show()
sys.exit(app.exec_())
