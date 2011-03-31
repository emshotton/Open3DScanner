import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

try:
    opencvworking = True
    import cv    
except ImportError:
    print "Unable to import OpenCV, webcam input won't work"
    opencvworking = False
    

#############################################################
class IplQImage(QtGui.QImage):
    """A class for converting iplimages to qimages"""
    
    def __init__(iplimage):
        #Rough-n-ready but it works dammit
        alpha = cv.CreateMat(iplimage.height,iplimage.width, cv.CV_8UC1)
        cv.Rectangle(alpha,(0,0),(iplimage.width,iplimage.height),cv.ScalarAll(255),-1)
        rgba = cv.CreateMat(iplimage.height,iplimage.width, cv.CV_8UC4)
        cv.Set(rgba, (1,2,3,4))
        cv.MixChannels([image, alpha],[rgba], [
        (0, 0),    # rgba[0] -> bgr[2]
        (1, 1),    # rgba[1] -> bgr[1]
        (2, 2),    # rgba[2] -> bgr[0]
        (3, 3)     # rgba[3] -> alpha[0]
        ])
        self.__imagedata = rgba.tostring()
        super(IplQImage,self).__init__(self.__imagedata, iplimage.width,iplimage.height, QtGui.QImage.Format_RGB32)
                

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
    
    def __toClassAttributes(self,attributes):
        #top bottom center
        #crappy hack but i'm drunk
        #WHY? Because fuck its why.
        newattr=[0,self.height(),self.width()/2]
        if self.__imageheight > 0 and self.__imagewidth>0:
            newattr[0]= attributes[0]*(float(self.__imageheight)/float(self.image.height()))
            newattr[1]= attributes[1]*(float(self.__imageheight)/float(self.image.height()))
            newattr[2]= attributes[2]*(float(self.__imagewidth)/float(self.image.width()))
        return newattr
    
    def __fromClassAttributes(self,attributes):
        newattr=[0,self.height(),self.width()/2]
        print self.image.height()
        print self.__imageheight
        if self.__imageheight > 0 and self.__imagewidth>0:
            newattr[0]= float(attributes[0])*float(float(self.image.height())/float(self.__imageheight))
            newattr[1]= float(attributes[1])*float(float(self.image.height())/float(self.__imageheight))
            newattr[2]= float(attributes[2])*float(float(self.image.width())/float(self.__imagewidth))
        return newattr
        

    def setImage(self,image):
        self.__imageheight = image.height()
        self.__imagewidth = image.width()
        
        self.image = image
        self.repaint()

    def paintEvent(self,ev):
        print "Painting"
        painter = QtGui.QPainter(self)
        painter.drawImage(0,0,self.image)
        painter.setPen(QtGui.QPen(QtGui.QColor(255,0,0)))
        painter.drawLine(0,self.__scantop,self.width(),self.__scantop)
        painter.setPen(QtGui.QPen(QtGui.QColor(0,255,0)))
        painter.drawLine(0,self.__scanbottom,self.width(),self.__scanbottom)
        painter.setPen(QtGui.QPen(QtGui.QColor(0,0,255)))
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
        self.connect(self.__lineimagelabel,QtCore.SIGNAL("scanParametersChanged"),self.__imagelabel.setScanParameters)
        #Init control area
        
    def setImage(self,image):
        if type(image) == type(QtGui.QImage()):
            self.__imagelabel.setImage(image)

        elif type(image) == type(cv.CvMat()):
            self.__imagelabel.setImage(IplQImage(image))

#        alpha = cv.CreateMat(image.height,image.width, cv.CV_8UC1)
#        cv.Rectangle(alpha,(0,0),(image.width,image.height),cv.ScalarAll(255),-1)
#        rgba = cv.CreateMat(image.height,image.width, cv.CV_8UC4)     
#        
#        cv.Set(rgba, (1,2,3,4))
#        cv.MixChannels([image, alpha],[rgba], [
#        (0, 0),    # rgba[0] -> bgr[2]
#        (1, 1),    # rgba[1] -> bgr[1]
#        (2, 2),    # rgba[2] -> bgr[0]
#        (3, 3)     # rgba[3] -> alpha[0]
#        ])
#
#        self.__iplimagedata = rgba.tostring()
#        qimage = QtGui.QImage(self.__iplimagedata, image.width,image.height, QtGui.QImage.Format_RGB32)
#        print qimage.numBytes()
#        qimage = qimage.scaledToWidth(400)
#        self.__imagelabel.setImage(qimage)
        

    def setLineImage(self,image):
        if type(image) == type(QtGui.QImage()):
            self.__lineimagelabel.setImage(image)

        elif type(image) == type(cv.CvMat()):
            self.__lineimagelabel.setImage(IplQImage(image))

#        print "Setting image"
#
#        alpha = cv.CreateMat(image.height,image.width, cv.CV_8UC1)
#        cv.Rectangle(alpha,(0,0),(image.width,image.height),cv.ScalarAll(255),-1)
#        rgba = cv.CreateMat(image.height,image.width, cv.CV_8UC4)     
        
##        cv.Set(rgba, (1,2,3,4))
#        cv.MixChannels([image, alpha],[rgba], [
#        (0, 0),    # rgba[0] -> bgr[2]
#        (1, 1),    # rgba[1] -> bgr[1]
#        (2, 2),    # rgba[2] -> bgr[0]
#        (3, 3)     # rgba[3] -> alpha[0]
#        ])
#
#        self.__ipllineimagedata = rgba.tostring()
#        qimage = QtGui.QImage(self.__ipllineimagedata, image.width,image.height, QtGui.QImage.Format_RGB32)
#        print qimage.numBytes()
#        qimage = qimage.scaledToWidth(400)
#        self.__lineimagelabel.setImage(qimage)

#    def setScanTop(top):
#        """"TODO""""
#
#    def setScanBottom(top):
#        """"TODO""""
#
#    def setScanCenter(top):
#        """"TODO""""
#############################################################


if __name__ == "__main__":    

    app =QtGui.QApplication(sys.argv)
    ex = ScanImageDisplay()
    if opencvworking == False:
        ex.setImage(QtGui.QImage(200,200,QtGui.QImage.Format_RGB32))
    else:
        capture = cv.captureFromCam(0)
    ex.show()
    sys.exit(app.exec_())
