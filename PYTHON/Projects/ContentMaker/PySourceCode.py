import random
import cv2
import os


def getrandfile():
    if not mp4_files:
        print("No .mp4 files found in the directory.")
    else:
        # Choose a random .mp4 file from the list
        random_mp4 = random.choice(mp4_files)
        #* print("Randomly chosen .mp4 file path:", random_mp4)
    return random_mp4

def letterbox_video(input_video_path, output_video_path):
    # Open the input video file
    cap = cv2.VideoCapture(input_video_path)

    # Get the original video frame dimensions
    original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Calculate the target aspect ratio (9:16)
    target_aspect_ratio = 9 / 16

    # Calculate the new dimensions for letterboxing
    new_width = original_width
    new_height = int(new_width / target_aspect_ratio)

    # Calculate the size of the letterboxes
    letterbox_height = (new_height - original_height) // 2

    # Create a VideoWriter object to write the letterboxed video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, 30.0, (new_width, new_height))

    # Loop through the video frames
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Add black letterboxes at the top and bottom of the frame
        letterboxed_frame = cv2.copyMakeBorder(frame, letterbox_height, letterbox_height, 0, 0, cv2.BORDER_CONSTANT, value=(0, 0, 0))

        # Write the letterboxed frame to the output video
        out.write(letterboxed_frame)

        # Display the letterboxed frame (optional)
        # cv2.imshow("Letterboxed Video", letterboxed_frame)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

    # Release the VideoCapture and VideoWriter objects
    cap.release()
    out.release()
    print("Done Making Video")
    # Close all OpenCV windows (optional)
    # cv2.destroyAllWindows()

# Directory containing the .mp4 files
bmp4_directory = r"C:\Users\crist\Desktop\BotContent\BackgroundVid"
#This varible hold the information on all the files in the directory
mp4_files = [os.path.join(bmp4_directory, file) for file in os.listdir(bmp4_directory) if file.endswith('.mp4')]

input_video_path = getrandfile()
output_video_path = "output_video.mp4"

letterbox_video(input_video_path, output_video_path)
#print(getrandfile())





