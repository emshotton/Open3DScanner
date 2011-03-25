import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

#############################################################

class ImageViewState:
    NONE=0
    CENTER=1
    TOP=2
    BOTTOM=3

#############################################################

class ImageView(QtGui.QWidget):

    def __init__(self):
        super(ImageView,self).__init__()
        self.setFixedSize(400,300)
        self.resetScanParameters()
        self.image = QtGui.QImage()
        self.__mousestate = ImageViewState.NONE
    
    def setImage(self,image):
        image = image.scaledToWidth(400)
        self.image = image
        self.repaint()

    def paintEvent(self,ev):
        print "Painting"
        painter = QtGui.QPainter(self)
        painter.drawImage(0,0,self.image)
        painter.drawLine(0,self.__scantop,self.width(),self.__scantop)
        painter.drawLine(0,self.__scanbottom,self.width(),self.__scanbottom)
        painter.drawLine(self.__scancenter,0,self.__scancenter,self.width())
        painter.end()        

    def mousePressEvent(self, ev):
        x = ev.pos().x()
        y = ev.pos().y()
        print self.__scancenter-5
        print self.__scancenter+5
        print x
        if x > (self.__scancenter-5) and x < (self.__scancenter+5):
            self.__mousestate=ImageViewState.CENTER
        elif y > self.height()/2:
            self.__mousestate=ImageViewState.BOTTOM
        elif y < self.height()/2:
            self.__mousestate=ImageViewState.TOP 
        self.updateAttributeLines(ev.pos())
        return

    def mouseMoveEvent(self,ev):
        self.updateAttributeLines(ev.pos())      
        self.repaint()

    def updateAttributeLines(self,position):
        x = position.x()
        y = position.y()
        if self.__mousestate==ImageViewState.TOP:
            if y > self.height()/2:
                self.__scantop = self.height()/2
            else:
                self.__scantop = y

        elif self.__mousestate==ImageViewState.BOTTOM:
            if y < self.height()/2:
                self.__scanbottom = self.height()/2
            else:
                self.__scanbottom = y
    
        elif self.__mousestate==ImageViewState.CENTER:
            self.__scancenter = x
        #Do a repaint
        self.repaint()
        self.emit(QtCore.SIGNAL("scanParametersChanged"), [self.__scantop,self.__scanbottom,self.__scancenter])

    def mouseReleaseEvent(self,ev):
        self.__mousestate=ImageViewState.NONE 

    def setScanParameters(self,parameters):
        print "Setting scan attirbutes"
        self.__scantop = parameters[0]
        self.__scanbottom = parameters[1]
        self.__scancenter = parameters[2]
        self.repaint()
        
    def resetScanParameters(self):
        self.__scantop = 0
        self.__scanbottom = self.height()-1
        self.__scancenter = self.width()/2

#############################################################

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
        self.connect(self.__imagelabel,QtCore.SIGNAL("scanParametersChanged"),self.__lineimagelabel.setScanParameters)
        #Init control area
        
    def setImage(self,image):
        print "Setting image"
        self.__imagelabel.setImage(image)

    def setLineImage(self,image):
        print "Setting image"
        self.__lineimagelabel.setImage(image)

#    def setScanTop(top):
#        """"TODO""""
#
#    def setScanBottom(top):
#        """"TODO""""
#
#    def setScanCenter(top):
#        """"TODO""""
#############################################################



