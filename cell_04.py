import cv2
import matplotlib.pyplot as plt

# 1. Define the image file name (make sure it's in the same folder)
image_path = "your_image.jpg" 

# 2. Load the image
img = cv2.imread(image_path)

if img is None:
    print("Error: Could not load the image. Check the file name.")
else:
    # IMPORTANT: OpenCV loads images as BGR, but Matplotlib displays them as RGB.
    # We must convert it so the colors don't look blue/distorted in Jupyter.
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # 3. Display the image inline
    plt.figure(figsize=(6, 6))
    plt.imshow(img_rgb)
    plt.title("Input Image")
    plt.axis('off') # Hides the pixel ruler layout
    plt.show()

    # 4. Analyze and plot the histogram
    channels = ('b', 'g', 'r')
    channel_names = ('Blue Channel', 'Green Channel', 'Red Channel')

    plt.figure(figsize=(10, 4))
    plt.title("Color Level Histogram Analysis")
    plt.xlabel("Pixel Intensity Value (0 - 255)")
    plt.ylabel("Number of Pixels")

    for i, col in enumerate(channels):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=col, label=channel_names[i])
        plt.xlim([0, 256])

    plt.legend()
    plt.show()
