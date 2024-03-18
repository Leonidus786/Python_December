# pylint: disable=E1101, C0103


import cv2
import numpy as np
import pyautogui

# Define the HSV range for detecting green color
low_green = np.array([25, 52, 72])
high_green = np.array([102, 255, 255])

# Open the default camera (camera index 0)
cap = cv2.VideoCapture(0)

# Variable to store the previous y-coordinate for comparison
prev_y = 0

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask to identify regions with the specified green color range
    mask = cv2.inRange(hsv, low_green, high_green)

    # Find contours in the mask
    contours, hierarchy = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Process each contour
    for i in contours:
        # Calculate the area of the contour
        area = cv2.contourArea(i)

        # If the contour area is greater than 1000, consider it
        if area > 1000:
            # Get the bounding rectangle for the contour
            x, y, w, h = cv2.boundingRect(i)

            # Draw a rectangle around the detected object
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # If the object is moving upward, simulate a spacebar press
            if y < prev_y:
                pyautogui.press('space')

            # Update the previous y-coordinate
            prev_y = y

    # Display the frame with rectangles drawn around detected objects
    cv2.imshow('frame', frame)

    # Exit the program if the 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture object
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
