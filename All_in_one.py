import cv2
import imutils

img = cv2.imread("sample1.jpg")# image reading here


resizeimg = imutils.resize(img,width=20) #image resize to expected size
cv2.imwrite("resizedimg.jpg",resizeimg)# save image that resized

grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # BGR to Gray 
cv2.imwrite("gray.jpg",grayImg)

thresImg = cv2.threshold(grayImg,180,255,cv2.THRESH_BINARY)[1] # trushold 
cv2.imwrite("trushold.jpg",thresImg)

gaussianBlurImg = cv2.GaussianBlur(img, (21,21),0) #Blur the image
cv2.imwrite("gaussianImage.jpg",gaussianBlurImg)
