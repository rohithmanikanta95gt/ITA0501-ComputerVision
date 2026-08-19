import cv2
import matplotlib.pyplot as plt

def analyze_color_histogram(image_path):
    # Step 1: Read the color image
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Could not load the image.")
        return

    # Step 2: Define color channel names and their plotting colors
    # OpenCV loads images in BGR format
    channels = ('b', 'g', 'r')
    channel_names = ('Blue Channel', 'Green Channel', 'Red Channel')

    # Create a figure for plotting
    plt.figure(figsize=(10, 5))
    plt.title("Color Level Histogram Analysis")
    plt.xlabel("Pixel Intensity Value (0 - 255)")
    plt.ylabel("Number of Pixels")

    # Step 3: Loop through each channel and calculate its histogram
    for i, col in enumerate(channels):
        # cv2.calcHist parameters: [image], [channel_index], mask, [histSize], [ranges]
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        
        # Plot the histogram line matching its actual color
        plt.plot(hist, color=col, label=channel_names[i])
        plt.xlim([0, 256])

    # Show the legend/labels on the chart
    plt.legend()
    
    # Display the final graph
    plt.show()

# --- Execute the function ---
# Replace with your actual image file name
analyze_color_histogram("your_image.jpg")
