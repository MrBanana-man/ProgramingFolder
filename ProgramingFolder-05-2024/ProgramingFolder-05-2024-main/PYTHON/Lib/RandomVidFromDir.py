import os
import random
import cv2

# Directory containing the .mp4 files
directory = r"C:\Users\crist\Desktop\BotContent\BackgroundVid"

# List all the .mp4 files in the directory
mp4_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.mp4')]

# Check if there are any .mp4 files in the directory
if not mp4_files:
    print("No .mp4 files found in the directory.")
else:
    # Choose a random .mp4 file from the list
    random_mp4 = random.choice(mp4_files)
    print("Randomly chosen .mp4 file path:", random_mp4)


# Path to the video file
video_path = random_mp4

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if the video file was successfully opened
if not cap.isOpened():
    print("Error: Could not open the video file.")
else:
    # Read and display frames from the video file until it's over
    while True:
        # Read a frame from the video file
        ret, frame = cap.read()

        # If the frame was read successfully, display it
        if ret:
            cv2.imshow('Video', frame)
        else:
            print("End of video.")
            break

        # Wait for a short duration and check for key press
        if cv2.waitKey(25) & 0xFF == ord('q'):
            print("Video playback interrupted.")
            break

# Release the video capture object and close the window
cap.release()
cv2.destroyAllWindows()
