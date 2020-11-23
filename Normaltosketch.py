import cv2
image = cv2.imread("/home/arun/Pictures/png/tom test images.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("/home/arun/Pictures/png/TomSketch(gray).png", gray_image)
inverted_image = 255 - gray_image
cv2.imwrite("/home/arun/Pictures/png/TomSketch(inverted).png", inverted_image)
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
cv2.imwrite("/home/arun/Pictures/png/TomSketch(blured).png", blurred)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imwrite("/home/arun/Pictures/png/TomSketch.png", pencil_sketch)

