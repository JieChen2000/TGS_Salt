# import the OpenCV package
import cv2
 
# load the image with imread()
imageSource = '../pic.png'
img = cv2.imread(imageSource)
 
vertical_img = img.copy()
# flip img vertically,
vertical_img = cv2.flip( img, 1 )
 
# display the images on screen with imshow()
cv2.imshow( "Original", img )
cv2.imshow( "Vertical flip", vertical_img )
 
# wait time in milliseconds
# this is required to show the image
# 0 = wait indefinitely
cv2.waitKey(3000)
 
#close the windows
cv2.destroyAllWindows()

