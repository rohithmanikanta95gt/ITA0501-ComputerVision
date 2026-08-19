import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. User-defined sizes (You can change these numbers to any size you want)
width = 800
height = 600
box_size = 100  # Size of the square boxes at the corners

# 2. Create a pure white image canvas
# np.ones creates a grid of 1s, multiplying by 255 makes it pure white
# dtype=np.uint8 is required for standard 8-bit color images
img = np.ones((height, width, 3), dtype=np.uint8) * 255

# 3. Define the Colors in RGB format (since we are plotting with Matplotlib)
COLOR_BLACK = [0, 0, 0]
COLOR_BLUE  = [0, 0, 255]
COLOR_GREEN = [0, 255, 0]
COLOR_RED   = [255, 0, 0]

# 4. Insert the boxes into the corners using NumPy array slicing [rows, columns]

# Top-Left Corner -> Black Box
img[0:box_size, 0:box_size] = COLOR_BLACK

# Top-Right Corner -> Blue Box
img[0:box_size, (width - box_size):width] = COLOR_BLUE

# Bottom-Left Corner -> Green Box
img[(height - box_size):height, 0:box_size] = COLOR_GREEN

# Bottom-Right Corner -> Red Box
img[(height - box_size):height, (width - box_size):width] = COLOR_RED

# 5. Display the final generated canvas image inline
plt.figure(figsize=(10, 7))
plt.imshow(img)
plt.title(f"Generated Canvas ({width}x{height}) with Corner Color Boxes")
plt.axis('on')  # 'on' shows the pixel ruler markings to prove the coordinates are perfect
plt.show()
