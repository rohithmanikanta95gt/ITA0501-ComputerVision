import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Define canvas dimensions
width = 800
height = 600

# 2. Create a pure white background image canvas
img = np.ones((height, width, 3), dtype=np.uint8) * 255

# 3. Define circle geometry and properties
# Center point coordinates of the circle (x, y)
center_coordinates = (400, 300)  # Exactly in the middle of our 800x600 canvas

# Radius of the circle in pixels
radius = 150

# Circle color in RGB format (e.g., Pure Blue)
color = (0, 0, 255)

# Line thickness in pixels (set to -1 if you want to completely fill the circle)
thickness = 5

# 4. Draw the circle onto the white canvas matrix
cv2.circle(img, center_coordinates, radius, color, thickness)

# 5. Display the final canvas inline
plt.figure(figsize=(10, 7))
plt.imshow(img)
plt.title("Generated Circle Shape using OpenCV")
plt.axis('on')  # Shows the pixel ruler to verify the center and radius markings
plt.show()
