import cv2
import matplotlib.pyplot as plt

def analyze_color_histogram(image_path):
    """
    Function to read an input image and analyze its histogram based on BGR color levels.
    """
    # Step 1: Read the color image using OpenCV
    img = cv2.imread(image_path)
    
    if img is None:
        print(f"Error: Could not load the image from path '{image_path}'. Check the file name.")
        return

    # Step 2: Define the color channels and their labels
    # OpenCV natively loads images in BGR format order
    channels = ('b', 'g', 'r')
    channel_colors = ('blue', 'green', 'red')
    channel_labels = ('Blue Channel', 'Green Channel', 'Red Channel')

    # Step 3: Setup the Matplotlib plot layout
    plt.figure(figsize=(11, 5))
    plt.title("Color Level Histogram Analysis", fontsize=14, fontweight='bold')
    plt.xlabel("Pixel Intensity Value (0 - 255)", fontsize=11)
    plt.ylabel("Number of Pixels", fontsize=11)
    plt.grid(True, linestyle='--', alpha=0.5) # Adds a clean grid background

    # Step 4: Loop through each color channel and calculate the histogram
    for i, col in enumerate(channels):
        # Parameters: [image], [channel_index], mask, [histSize], [ranges]
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        
        # Plot the calculated histogram line matching its actual color channel
        plt.plot(hist, color=channel_colors[i], label=channel_labels[i], linewidth=2)
        plt.xlim([0, 256])

    # Step 5: Render the chart with labels
    plt.legend(loc='upper right', fontsize=10)
    plt.show()

# --- Call the function to execute ---
# Replace "your_image.jpg" with your actual file name
analyze_color_histogram("your_image.jpg")
