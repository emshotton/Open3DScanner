#!/usr/bin/python

import cv


class CameraCapture():
    
    def __init__(self,device=0):
        self.__capture = cv.CaptureFromCAM(device)
        self.working = True
        if not self.__capture:
            print "Camera not working"
            self.working = False
    
    def getImage(self):
        img = cv.QueryFrame(self.__capture)
        return img

class Spline():
    def __init__(self):
        self.spline = []
        self.colorspline = []

def createSpline(image,channel=0,camera_angle = 45,top_crop =0,bottom_crop =0,rotation_center=0,upper_threshold=255,lower_threshold=0):
    spline=[0]*image.height
    
    #Sanity check some of the inputs
    rotation_center = image.width/2
    bottom_crop = image.height-1 - bottom_crop
    if bottom_crop == top_crop or top_crop > bottom_crop:
        print "Error, the bottom crop value is less or equal to the top crop value"
        return

    #grab the spline
    for y in range(top_crop,bottom_crop):
        max_value = 0
        max_position = 0
        for x in range(image.width-1):
            pixel = cv.Get2D(image,y,x)
            if pixel[channel] > max_value and pixel[channel] < upper_threshold and pixel[channel] > lower_threshold:
                max_value = pixel[channel]
                max_position = x
        spline[y]=max_position

    #fill in any holes
    good_top = rotation_center
    good_bottom = rotation_center
    for y in range(len(spline)-1):
        #find any points that area too large or small
        if spline[y] == 0 or spline[y] == image.width:
            #find the next good point
            for z in range(y,len(spline)-1):
                if spline[z] > 0 and spline[z] < image.width:
                    good_bottom = spline[z]
                    break
            #set the bad point to the avearage of the two nearest good points (not perfect, but close enough)
            spline[y]=(good_top+good_bottom)/2 
        good_top=spline[y]

    colorspline = [(0,0,0)]*len(spline)
    #grab the color spline
    for y in range(len(spline)-1):
        colorspline[y+top_crop]=cv.Get2D(image,y,spline[y])

    #remove center offset
    for y in range(len(spline)-1):
        spline[y]=spline[y]-rotation_center

    #Package the result up in a Spline class
    result=Spline()
    result.spline = spline
    result.colorspline = colorspline
    
    return result

def createSplineColors(image,spline):
    if image.height != len(spline):
        print "The spline array must be the same size as the image height"
        return None
    colorspline = [(0,0,0,0)]*len(spline)
    for y in range(image.height-1):
        colorspline[y] = cv.Get2D(image,y,spline[y])
    return colorspline

def createLineImage(image,channel=0):
    print "Creating line image"
    for y in range(image.height-1):
        max_value = 0
        max_position = 0
        for x in range((image.width-1)):
            pixel = cv.Get2D(image,y,x)
            if pixel[channel] > max_value:
                max_value = pixel[channel]
                max_position = x
            pixel = cv.RGB(0,0,0)
            cv.Set2D(image,y,x,pixel)
        pixel = cv.RGB(max_value,0,0)
    cv.Set2D(image,y,max_position,pixel)
    return image


if __name__ == "__main__":
    capture = CameraCapture()
    
    image = capture.getImage()
    cv.SaveImage("image.png",image)    
    image = createLineImage(image,channel=0)
    spline = createSpline(image,channel=0)
    print str(len(spline.colorspline))+" "+str(len(spline.spline))
    cv.SaveImage("lineimage.png",image)
    




