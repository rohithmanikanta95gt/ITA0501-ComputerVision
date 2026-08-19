import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Define canvas dimensions
width = 800
height = 600

# 2. Create a pure white background image canvas
img = np.ones((height, width, 3), dtype=np.uint8) * 255

# 3. User-defined text string (You can change this string to whatever you want)
text_to_display = "Computer Vision "

# 4. Configure text layout and properties
# Choose one of OpenCV's built-in font styles
font = cv2.FONT_HERSHEY_SIMPLEX

# Scale factor that determines the font size
font_scale = 1.2

# Text color in RGB format (e.g., Deep Purple / Maroon)
color = (128, 0, 128)

# Thickness of the stroke lines in pixels
thickness = 3

# 5. Calculate text size to center it perfectly on the canvas
(text_w, text_h), baseline = cv2.getTextSize(text_to_display, font, font_scale, thickness)

# Determine the bottom-left coordinate position (x, y) for the text
x_pos = int((width - text_w) / 2)
y_pos = int((height + text_h) / 2)

# 6. Overlay the text onto the canvas matrix
# Parameters: image, text, origin_point, font, scale, color, thickness, line_type
cv2.putText(img, text_to_display, (x_pos, y_pos), font, font_scale, color, thickness, cv2.LINE_AA)

# 7. Display the final canvas inline
plt.figure(figsize=(10, 7))
plt.imshow(img)
plt.title("Displayed Text String using OpenCV")
plt.axis('on')  # Shows pixel ruler lines to verify the alignment centering
plt.show()
