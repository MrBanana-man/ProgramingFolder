import cv2
import numpy as np
import pyautogui
import time

def find_image_on_screen(reference_images):
    global settingspicFound, pictureFound, mospicFound  # Use global variables to modify outside the function
    
    while True:
        # Take a screenshot
        screenshot = pyautogui.screenshot()
        screenshot = np.array(screenshot)
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
        
        found_locations = []
        
        for reference_image_path in reference_images:
            # Load the reference image
            reference_image = cv2.imread(reference_image_path)
            
            # Perform template matching
            result = cv2.matchTemplate(screenshot, reference_image, cv2.TM_CCOEFF_NORMED)
            
            # Define a threshold for similarity
            threshold = 0.8
            
            # Get the location where the image matches
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            
            # Check if similarity is above threshold
            if max_val >= threshold:
                # If similarity is above threshold, add the location to the list
                found_locations.append((max_loc, reference_image_path))
        
        if found_locations:
            for location, reference_image_path in found_locations:
                if reference_image_path == r"C:\Users\crist\Desktop\settingspic.png":
                    print("settings picture found")
                elif reference_image_path == r"C:\Users\crist\Desktop\picture.png":
                    print("stem picture found")
                elif reference_image_path == r"C:\Users\crist\Desktop\mosPpicture.png":
                    print("mospoz picture found")
                
        else:
            print("No images found on the screen.")
        
        # Add a delay before the next iteration
        time.sleep(1)  # Adjust the delay as needed

#Add more pictures to the table
reference_image_paths = [r"C:\Users\crist\Desktop\picture.png", r"C:\Users\crist\Desktop\settingspic.png", r"C:\Users\crist\Desktop\mosPpicture.png"]
find_image_on_screen(reference_image_paths)

