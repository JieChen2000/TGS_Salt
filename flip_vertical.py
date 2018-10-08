# import the OpenCV package
import cv2
 
# load the image with imread()
imageSource = './pic.png'
img = cv2.imread(imageSource)
 
vertical_img = img.copy()
# flip img vertically,
vertical_img = cv2.flip( img, 1 )
 
# Laplacian or 2nd derivative                                                                                                                               
lap= cv2.Laplacian(img,cv2.CV_64F,scale = 1)
#first derivative along x axis                                                                                                                              
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)

# display the images on screen with imshow()                                                                                                                
cv2.imshow( "Original", img )
cv2.imshow( "Vertical flip", vertical_img )
cv2.imshow( "Lapalacian", lap )
cv2.imshow( "Sobelx", sobelx)

# wait time in milliseconds                                                                                                                                 
# this is required to show the image                                                                                                                        
# 0 = wait indefinitely                                                                                                                                     
cv2.waitKey(15000)

#close the windows                                                                                                                                          
cv2.destroyAllWindows()



#X = [np.array(cv2.imread(TRAIN_IMAGE_DIR + p, cv2.IMREAD_GRAYSCALE), dtype=np.uint8) for p in tqdm(train_fns)]                                             
#X_Laplacian=[np.array(cv2.Laplacian(cv2.imread(TRAIN_IMAGE_DIR + p, cv2.IMREAD_GRAYSCALE),cv2.CV_64F),dtype=np.uint8) for p in tqdm(train_fns)]            
#X = np.expand_dims(X,axis=3)                                                                                                                               
#X_Laplacian = np.expand_dims(X_Laplacian,axis=3)                                                                                                           
#X= np.concatenate((X, X_Laplacian),axis=3)
 


