import cv2
image=cv2.inread("Image Drawing Function/python -iamge.png")
if image is None:
    print("Opps! Your image is not working")
else:
    print("Image loaded successfully!")
    pt1=(50,100)
    pt2=(300,500)
    color=(255,0,0)
    thickness=4
    cv2.line(image,pt1,pt2,color,thickness)

    cv2.imshow("Adding Text" ,image)
    cv2.waitKey(0)
    cv2.destoryAllWindow()

#inmread using this opencv 
import cv2

image =cv2.imread("Phase 1/python image.png")
 
if image is not None:
    cv2.imshow("Image showing",image)#open the window
    cv2.waitKey(0)#wait for the window
    cv2.destroyAllWindow()#close the window
else:
    print("Image loaded susccessfully")