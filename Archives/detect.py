import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('Lane-2.jpg')

class ImageProcess:
    image_height =0
    image_width = 0

    def __init__(self,image):
        self.image_height =  image.shape[0]
        self.image_width = image.shape[1]
    
    def Preprocess(self,image):
        copy = self.GetCopy(image)
        gray = self.GetGrayScale(copy)
        blur = cv2.GaussianBlur(gray,(5,5),0)
        edgify = cv2.Canny(blur,50,150)
        return edgify

    def GetCopy(self,image):
        return np.copy(image) # do not use lane_image = image ( this does not create a copy but modifies origanl array)

    def GetGrayScale(self,image):
        return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    def ShowImage(self,image):
        cv2.imshow("Result ",image)
        cv2.waitKey(0)

    def ReigonOfIntrest(self,image):
        polygons = np.array([[(200,self.image_height),(1100,self.image_height),(550,250)]])
        mask = np.zeros_like(image)
        cv2.fillPoly(mask,polygons,255)
        masked_lane = cv2.bitwise_and(mask,image)
        return masked_lane


p = ImageProcess(image)
mask = p.ReigonOfIntrest(p.Preprocess(image))
p.ShowImage(mask)





