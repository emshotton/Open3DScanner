#!/usr/bin/python

#Splinesweep software.
#Version 1.0 - Withnail
#by Matthew Shotton
#licenced under GPLv3.0 see http://www.gnu.org/licenses/gpl-3.0.txt

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
import scanview
import splinecapture

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




class GUI(QtGui.QWidget):
    def __init__(self):
        super(GUI, self).__init__()
        self.rotations = 300 
        if splinecapture.opencvworking == True:
            self.cameracapture = splinecapture.CameraCapture()        
        self.__initUI()
        self.__cameratimer =QtCore.QTimer()
        self.__cameratimer.setInterval(100)
        self.__cameratimer.start()
        self.connect(self.__cameratimer,QtCore.SIGNAL("timeout()"),self.updateScanDisplay)        
        
    def __initUI(self):
        layout = QtGui.QGridLayout()
        self.scandisplay = scanview.ScanImageDisplay()
        #img = QtGui.QImage(600,480,QtGui.QImage.Format_RGB32)
        #img.load("1.png")
        #self.scandisplay.setImage(img)
        #createlineimage(img)
        #self.scandisplay.setLineImage(img)
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

    def updateScanDisplay(self):
        if splinecapture.opencvworking == True:
            image= self.cameracapture.getImage()
            self.scandisplay.setLineImage(splinecapture.createLineImage(image))     
        else:
            image = QtGui.QImage(640,480,QtGui.QImage.Format_RGB32)
        self.scandisplay.setImage(image)


app = QtGui.QApplication(sys.argv)
ex = GUI()
ex.show()
sys.exit(app.exec_())
