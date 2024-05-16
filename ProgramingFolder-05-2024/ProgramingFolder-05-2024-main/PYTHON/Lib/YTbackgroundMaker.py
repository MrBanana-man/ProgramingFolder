from moviepy.video.io.VideoFileClip import VideoFileClip
import moviepy.editor

def crop_video(input_video, output_video, target_ratio):
    # Load the video clip
    video_clip = moviepy.editor.VideoFileClip(input_video)
    
    # Calculate the dimensions for cropping
    video_width, video_height = video_clip.size
    target_width = int(video_height * target_ratio)
    crop_width = (video_width - target_width) / 2
    
    # Apply cropping
    cropped_clip = video_clip.crop(x1=crop_width, x2=video_width-crop_width)
    
    # Resize the video to fit the aspect ratio
    resized_clip = cropped_clip.resize(height=video_height)
    
    # Write the result to a new file
    resized_clip.write_videofile(output_video, codec='libx264', fps=video_clip.fps)

# Example usage
input_video = r"C:\Users\crist\Downloads\Satisfying Slime ASMR ｜ Relaxing Slime Videos Compilation No Talking No Music No Voiceover (online-video-cutter.com).mp4"
output_video = "output_video.mp4"
target_ratio = 9 / 16

crop_video(input_video, output_video, target_ratio)
