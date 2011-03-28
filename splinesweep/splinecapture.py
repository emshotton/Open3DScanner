#!/usr/bin/python

import cv


class CameraCapture():
    
    def __init__(self):
        self.__capture = cv.CaptureFromCAM(0)
        self.working = True
        if not self.__capture:
            print "Camera not working"
            self.working = False
    
    def getImage(self):
        img = cv.QueryFrame(self.__capture)
        return img

    def createlineimage(self,image):
        print "Creating line image"
        for y in range(image.height()):
            max_value = 0
            max_position = 0
        for x in range(image.width()):
            pixel = image.pixel(x,y)
#            if QtGui.qRed(pixel) > max_value:
#                max_value = QtGui.qRed(pixel)
#                max_position = x
#            pixel = QtGui.qRgb(0,0,0)
#            image.setPixel(x,y,pixel)
#        pixel = QtGui.qRgb(max_value,0,0)
#        image.setPixel(max_position,y,pixel)


if __name__ == "__main__":
    capture = CameraCapture()
    image = capture.getImage()
    cv.SaveImage("image.png",image)
    




