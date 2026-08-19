import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Define canvas dimensions
width = 800
height = 600

# 2. Create a pure white background image canvas
img = np.ones((height, width, 3), dtype=np.uint8) * 255

# 3. Define rectangle geometry and properties
# Top-left corner coordinates (x1, y1)
pt1 = (200, 150)

# Bottom-right corner coordinates (x2, y2)
pt2 = (600, 450)

# Rectangle color in RGB format (e.g., Pure Red)
color = (255, 0, 0)

# Line thickness in pixels (set to -1 if you want to completely fill the rectangle)
thickness = 5

# 4. Draw the rectangle onto the white canvas matrix
cv2.rectangle(img, pt1, pt2, color, thickness)

# 5. Display the final canvas inline
plt.figure(figsize=(10, 7))
plt.imshow(img)
plt.title("Generated Rectangle Shape using OpenCV")
plt.axis('on')  # Shows the pixel ruler to verify coordinates match pt1 and pt2
plt.show()
