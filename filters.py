import cv2
import numpy as np

kernel = 3
minDist = 300
param_1 = 70
param_2 = 30
minradius = 20
maxradius = 45

x_axis = 256
y_axis = 256

def filter(k):
    img_ori = cv2.imread('./'+str(k)+'.jpg')
    img_ori = cv2.resize(img_ori, (x_axis, y_axis), interpolation = cv2.INTER_CUBIC)
    
    img = cv2.imread('./'+str(k)+'.jpg',cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (x_axis, y_axis), interpolation = cv2.INTER_CUBIC)
    
    for i in range (0, x_axis):
        for j in range (0, y_axis):
            if img[i,j] > 155:
                img[i,j] = 255
                continue
            img[i,j] += 100
            
    for i in range (0, x_axis):
        for j in range (0, y_axis):
            for l in range(0,3):
                
                if img_ori[i,j,l] > 200:
                    img_ori[i,j,l] = 255
                    continue
                img_ori[i,j] += 50


    mBlurImg = cv2.medianBlur(img, kernel)
    cv2.imwrite('./output_blur/blur_'+str(k)+'.jpg',mBlurImg)
    cv2.imwrite('./output_img_ori/img_'+str(k)+'.jpg',img_ori)
    
    #circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT,1, minDist,param1=param_1,param2=param_2, minRadius=minradius, maxRadius=maxradius)

    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,minDist,param1=100,param2=1.5,minRadius=0,maxRadius=0)

    x = int(circles[0][0][0])
    y = int(circles[0][0][1])
    radius = int(circles[0][0][2])

    cv2.circle(img_ori,(x,y),radius,(0,255,0),1)

    cv2.circle(img_ori,(x,y),30,(0,0,255),1)
    cv2.imwrite('./output_img/img_'+str(k)+'.jpg',img_ori)


for k in range(1,6):
    filter(k)
