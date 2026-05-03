import cv2
import numpy as np

img = cv2.imread(r"image.jpeg")
if img is None:
    print("Error: Image not found!")
    exit()
img = cv2.resize(img, (400, 600))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 50, 150)
sketch = cv2.bitwise_not(edges)
sketch_color = cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)
color = cv2.bilateralFilter(img, d=9, sigmaColor=200, sigmaSpace=200)
cv2.imshow("Colored Sketch", sketch_color) 
cv2.waitKey(1000)  


for alpha in np.linspace(0, 1, 20):  
    blended = cv2.addWeighted(color, alpha, sketch_color, 1 - alpha, 0)
    cv2.imshow("Colored Sketch", blended)
    cv2.waitKey(200)  

cv2.waitKey(0)
cv2.destroyAllWindows()
