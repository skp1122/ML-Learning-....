## displaying image directly via opencv
import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
    
    img = cv2.imread('img.jpg')
    gray = cv2.imread('img.jpg',cv2.IMREAD_GRAYSCALE)

    cv2.imshow('Bird Image',img)
    cv2.imshow('Gray Bird Image',gray)

    # Wait for user input - q,then you will stop the loop
    key_pressed = cv2.waitkey(1) & 0xFF
    if key_pressed == ord('q'):
        break
    #cv2.waitKey(1000) ## 0 means waiting image for infinite time
    #cv2.destroyAllWindows() ## afer time given in waitkey,it will destroyed itself
cap.release()
cv2.destroyAllWindows()