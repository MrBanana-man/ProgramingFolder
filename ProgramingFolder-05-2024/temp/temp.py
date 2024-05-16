import cv2

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

    # Close all OpenCV windows (optional)
    # cv2.destroyAllWindows()

# Example usage
input_video_path = r"C:\Users\crist\Downloads\video.mp4"
output_video_path = "output_video.mp4"
letterbox_video(input_video_path, output_video_path)

print("Done Making Video")