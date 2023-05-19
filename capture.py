import numpy as np
import cv2
from PIL import ImageGrab as ig
import time

def process_img(og_img):

    processed_img = cv2.cvtColor(og_img, cv2.COLOR_BGR2GRAY)

last_time = time.time()  # Get the current time

while True:
    # Capture the screen image within the specified bounding box
    screen = ig.grab(bbox=(0, 40, 840, 580))

    # Calculate the time taken for the loop iteration
    print('Loop took {} seconds', format(time.time() - last_time))

    # Display the captured screen image using OpenCV
    cv2.imshow("test", cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2RGB))

    # Update the last_time variable to the current time
    last_time = time.time()

    # Check if the 'q' key is pressed to exit the loop
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()  # Close the OpenCV window
        break  # Exit the loop
