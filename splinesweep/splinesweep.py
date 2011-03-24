#!/usr/bin/python

#Splinesweep software.
#Version 1.0 - Withnail
#by Matthew Shotton
#licenced under GPLv3.0 see http://www.gnu.org/licenses/gpl-3.0.txt

import sys
from PyQt4 import QtGui

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
        layout = QtGui.QVBoxLayout()
        self._imagelabel = QtGui.QLabel()
        self._lineimagelabel = QtGui.QLabel()
        layout.addWidget(self._imagelabel)
        layout.addWidget(self._lineimagelabel)
        self.setLayout(layout)
        
    def setImage(self,image):
        print "Setting image"
        display_image = image.scaledToWidth(400)
        self._imagelabel.setPixmap(QtGui.QPixmap.fromImage(display_image))

    def setLineImage(self,image):
        print "Setting image"
        display_image = image.scaledToWidth(400)
        self._lineimagelabel.setPixmap(QtGui.QPixmap.fromImage(display_image))


class GUI(QtGui.QWidget):
    def __init__(self):
        super(GUI, self).__init__()
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
        self.setLayout(layout)
        self.setWindowTitle('Splinesweep v1.0 - \"Withnail\"')
        self.resize(300, 300)


app = QtGui.QApplication(sys.argv)
ex = GUI()
ex.show()
sys.exit(app.exec_())
