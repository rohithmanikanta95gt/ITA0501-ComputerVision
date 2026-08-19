import cv2

# Step 1: Read the image in grayscale (required for standard equalization)
img_gray = cv2.imread("your_image.jpg", cv2.IMREAD_GRAYSCALE) 

if img_gray is None:
    print("Error: Could not load the image.")
else:
    # Step 2: Perform Histogram Equalization
    img_equalized = cv2.equalizeHist(img_gray)
    
    # Step 3: Create resizable windows
    cv2.namedWindow("Original Grayscale", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Equalized Image", cv2.WINDOW_NORMAL)
    
    # Set display sizes for your monitor
    cv2.resizeWindow("Original Grayscale", 600, 450)
    cv2.resizeWindow("Equalized Image", 600, 450)
    
    # Step 4: Display both images for comparison
    cv2.imshow("Original Grayscale", img_gray)
    cv2.imshow("Equalized Image", img_equalized)
    
    # Keep windows open until a key is pressed
    cv2.waitKey(0) 
    cv2.destroyAllWindows()
