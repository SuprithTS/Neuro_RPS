import cv2

def get_webcam_dimensions():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return None

    # Capture a single frame
    ret, frame = cap.read()

    # Check if the frame is captured successfully
    if not ret:
        print("Error: Could not capture frame.")
        return None

    # Get dimensions of the frame
    height, width, _ = frame.shape

    # Release the webcam
    cap.release()

    return width, height

# Get webcam dimensions
dimensions = get_webcam_dimensions()

# Print the dimensions
if dimensions:
    print(f"Webcam Dimensions: {dimensions[0]} x {dimensions[1]}")
