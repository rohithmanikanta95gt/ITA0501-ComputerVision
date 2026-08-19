import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the original color image
image_path = "your_image.jpg" 
img = cv2.imread(image_path)

if img is None:
    print(f"Error: Could not load the image '{image_path}'. Check your folder setup.")
else:
    # Convert from BGR to RGB for accurate Jupyter inline layout rendering
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # 2. Convert the image to HSV color space (highly recommended for color-level isolation)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # 3. Define the Color Level Ranges for subtraction
    # Example: Targeting skin tones/warm background elements. 
    # Adjust these ranges depending on what color you want to extract or subtract!
    lower_color = np.array([0, 20, 70], dtype="uint8")
    upper_color = np.array([20, 255, 255], dtype="uint8")
    
    # 4. Create a binary mask where isolated colors become White (255) and everything else is Black (0)
    mask = cv2.inRange(img_hsv, lower_color, upper_color)
    
    # 5. Subtract the background by performing a bitwise AND operation
    # This keeps only the pixels that fell within our defined color boundaries
    img_subtracted = cv2.bitwise_and(img_rgb, img_rgb, mask=mask)
    
    # 6. Render the original input image
    plt.figure(figsize=(7, 5))
    plt.imshow(img_rgb)
    plt.title("1. Original Input Image")
    plt.axis('off')
    plt.show()
    
    # 7. Render the binary color map mask
    plt.figure(figsize=(7, 5))
    plt.imshow(mask, cmap='gray')
    plt.title("2. Isolated Color Level Mask")
    plt.axis('off')
    plt.show()
    
    # 8. Render the final background subtraction output
    plt.figure(figsize=(7, 5))
    plt.imshow(img_subtracted)
    plt.title("3. Background Subtracted Result")
    plt.axis('off')
    plt.show()
