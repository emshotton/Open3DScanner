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
    



class ImageViewState:
    NONE=0
    CENTER=1
    TOP=2
    BOTTOM=3

class ImageView(QtGui.QLabel):

    def __init__(self):
        super(ImageView,self).__init__()
        self.setFixedWidth(400)
        self.resetScanParameters()
        self.__mousestate = ImageViewState.NONE
    
    def setImage(self,image):
        image = image.scaledToWidth(400)
#        for x in range(image.width()):
#            image.setPixel(x,self.__scantop,QtGui.qRgb(255,0,0))
#            image.setPixel(x,self.__scanbottom,QtGui.qRgb(0,255,0))
    
        self.setPixmap(QtGui.QPixmap.fromImage(image))

    def mousePressEvent(self, ev):
        x = ev.pos().x()
        y = ev.pos().y()
        print self.__scancenter-5
        print self.__scancenter+5
        print x
        if x > (self.__scancenter-5) and x < (self.__scancenter+5):
            self.__mousestate=ImageViewState.CENTER
            print "Center selected"
            return
        if y > self.height()/2:
            self.__mousestate=ImageViewState.BOTTOM
            print "Bottom seleceted"
            return
        if y < self.height()/2:
            self.__mousestate=ImageViewState.TOP 
            print "Top selected"
            return

    def mouseMoveEvent(self,ev):
        x = ev.pos().x()
        y = ev.pos().y()
#        print "X: "+str(ev.pos().x())+" Y: "+ str(ev.pos().y())        
        if self.__mousestate=ImageViewState.TOP:
            if y > self.height()/2:
                self.__scantop = self.height()/2
            else:
                self.__scantop = y

        elif self.__mousestate=ImageViewState.BOTTOM:
            if y < self.height()/2:
                self.__scanbottom = self.height()/2
            else:
                self.__scanbottom = y
    
        elif self.__mousestate=ImageViewState.CENTER:
            self.__scancenter = x
        #Do a repaint

    def mouseReleaseEvent(self,ev):
        self.__mousestate=ImageViewState.NONE 

    def setScanParameters(self,parameters):
        self.__scantop = parameters[0]
        self.__scanbottom = parameters[1]
        self.__scancenter = parameters[2]
        
    def resetScanParameters(self):
        self.__scantop = 0
        self.__scanbottom = self.height()-1
        self.__scancenter = self.width()/2



class ScanImageDisplay(QtGui.QWidget):
    def __init__(self):
        super(ScanImageDisplay,self).__init__()      
        self.__initUI()

    def __initUI(self):
        #init viewing area
        layout = QtGui.QGridLayout()
        self.__imagelabel = ImageView()
        self.__lineimagelabel = ImageView()
        layout.addWidget(self.__imagelabel)
        layout.addWidget(self.__lineimagelabel)
        self.setLayout(layout)
        #Init control area
        
    def setImage(self,image):
        print "Setting image"
        self.__imagelabel.setImage(image)

    def setLineImage(self,image):
        print "Setting image"
        self.__lineimagelabel.setImage(image)




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
