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
        self.colorchannel = 0
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
        self.controlwidget.splinegen_button = QtGui.QPushButton("Generate a spline")

        self.controlwidget.channel_combobox = QtGui.QComboBox()
        self.controlwidget.channel_combobox.addItem("Red")
        self.controlwidget.channel_combobox.addItem("Green")
        self.controlwidget.channel_combobox.addItem("Blue")
        
        self.controllayout.addWidget(self.controlwidget.rotation_label,0,0)
        self.controllayout.addWidget(self.controlwidget.rotation_spinbox,0,1)
        self.controllayout.addWidget(QtGui.QLabel("Color channel"),1,0)
        self.controllayout.addWidget(self.controlwidget.channel_combobox,1,1)
        self.controllayout.addWidget(self.controlwidget.splinegen_button,2,0,1,2)
    
        self.controlwidget.setLayout(self.controllayout)
        layout.addWidget(self.controlwidget,0,1,2,1)
        self.setLayout(layout)
        #Connecting signals/slots
        self.connect(self.controlwidget.rotation_spinbox,QtCore.SIGNAL("valueChanged(int)"),self.setRotations)
        self.connect(self.controlwidget.splinegen_button,QtCore.SIGNAL("pressed()"),self.updateSplineDisplay)
        self.connect(self.controlwidget.channel_combobox,QtCore.SIGNAL("activated(QString)"),self.setColorChannel)
                
    def setRotations(self,rotations):
        print "setting rotation: "+str(rotations)
        self.rotations = rotations
        self.__progressbar.setRange(0,self.rotations)

    def setColorChannel(self, channel):
        if channel == "Red":
            self.colorchannel = 0
            print "Setting channel to Red"

        elif channel == "Green":
            self.colorchannel = 1
            print "Setting channel to Green"

        elif channel == "Blue":
            self.colorchannel = 2
            print "Setting channel to Blue"

        else: print "OH GoD ThIS ShoUld NeVeR HappEN!!! Owls are probably nesting inside your computer"    

    def updateScanDisplay(self):
        if splinecapture.opencvworking == True:
            self.image= self.cameracapture.getImage()
        else:
            self.image = QtGui.QImage(640,480,QtGui.QImage.Format_RGB32)
            self.image.load("1.png")
        self.scandisplay.setImage(self.image)

    def updateSplineDisplay(self):
        self.scandisplay.setLineImage(createLineImage(self.image,self.colorchannel))     
        

def createLineImage(image,channel =0):
    for y in range(image.height()-1):
        max_value=0
        max_position =0
        for x in range(image.width()-1):
            pixel = (QtGui.qRed(image.pixel(x,y)),QtGui.qGreen(image.pixel(x,y)),QtGui.qBlue(image.pixel(x,y)))
            if pixel[channel] > max_value:
               max_position = x
               max_value = pixel[channel]
            image.setPixel(x,y,QtGui.qRgb(0,0,0))
        if channel == 0:
            image.setPixel(max_position,y,QtGui.qRgb(max_value,0,0))
        if channel == 1:
            image.setPixel(max_position,y,QtGui.qRgb(0,max_value,0))
        if channel == 2:
            image.setPixel(max_position,y,QtGui.qRgb(0,0,max_value))
    return image

app = QtGui.QApplication(sys.argv)
ex = GUI()
ex.show()
sys.exit(app.exec_())
