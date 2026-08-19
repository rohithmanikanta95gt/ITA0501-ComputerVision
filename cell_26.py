import cv2
import matplotlib.pyplot as plt

# 1. Load the original color image
image_path = "your_image.jpg" 
img = cv2.imread(image_path)

if img is None:
    print("Error: Could not load the image. Check the file name and extension.")
else:
    # Convert from BGR to RGB for accurate Jupyter display
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    face_detected_img = img_rgb.copy()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 2. FIX: Force OpenCV to load the local XML file we just downloaded
    local_model_path = "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(local_model_path)
    
    # Verify the local file loaded without being empty
    if face_cascade.empty():
        print("❌ Error: The local cascade file is empty or corrupted.")
    else:
        # 3. Detect faces in the image matrix
        faces = face_cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        print(f"Total Faces Detected: {len(faces)}")
        
        # 4. Loop through every detected face and draw a green bounding box
        for (x, y, w, h) in faces:
            cv2.rectangle(face_detected_img, (x, y), (x + w, y + h), (0, 255, 0), 4)
            
        # 5. Display the comparison side-by-side inline
        fig, axes = plt.subplots(1, 2, figsize=(16, 8))
        
        axes.imshow(img_rgb)
        axes.set_title("Original Image")
        axes.axis('off')
        
        axes.imshow(face_detected_img)
        axes.set_title(f"Face Detection Result ({len(faces)} found)")
        axes.axis('off')
        
        plt.tight_layout()
        plt.show()
