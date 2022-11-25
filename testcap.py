import cv2
import numpy as np

# Create an object to read camera video
cap = cv2.VideoCapture(0)

video_cod = cv2.VideoWriter_fourcc(*'XVID')
video_output = cv2.VideoWriter('capture_product.avi', video_cod, 10, (640,480))

while(True):
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR)

    # define orange color range
    light_orange = np.array([5, 50, 50],np.uint8) #light_orange = np.array([5, 50, 50])
    dark_orange = np.array([15, 255, 255],np.uint8) #dark_orange = np.array([15, 255, 255])

    # Threshold the HSV image to get only orange colors
    mask = cv2.inRange(hsv, light_orange, dark_orange)

    # Bitwise-AND mask and original image
    output = cv2.bitwise_and(frame, frame, mask=mask)

    # Write the frame into the file 'capture_product.avi'
    video_output.write(output)

    # Display frame, saved in file
    cv2.imshow('output',output)

    # Press q on keyboard to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and video write objects
cap.release()
video_output.release()

# Closes all frames
cv2.destroyAllWindows()

print("The video was successfully saved")



