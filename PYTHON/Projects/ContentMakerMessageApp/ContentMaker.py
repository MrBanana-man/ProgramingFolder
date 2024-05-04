import os
import random
import cv2
from gtts import gTTS
from mutagen.mp3 import MP3
import pytesseract
from PIL import Image

def showVid():
    if not cap.isOpened():
        print("Error: Could not open the video file.")
    else:
        while True:
            ret, frame = cap.read()
            
            if ret:
                cv2.imshow('Video', frame)
            else:
                print("End of video.")
                break

            # If the "q" key is pressed the video player quits
            if cv2.waitKey(25) & 0xFF == ord('q'):
                print("Video playback interrupted.")
                cap.release()
                cv2.destroyAllWindows()


def getrandfile():
    if not mp4_files:
        print("No .mp4 files found in the directory.")
    else:
        # Choose a random .mp4 file from the list
        random_mp4 = random.choice(mp4_files)
        print("Randomly chosen .mp4 file path:", random_mp4)
    return random_mp4


def TexttoAudio():
    NumOutput = 0 
    #Gets each line in the .txt file and converts it to audio using gTTS
    with open(txt_file, 'r') as file:
        # Read the file line by line
        for line in file:
            linemessage = line.strip()
            gTTS(text = linemessage, lang='en', slow=False).save(os.path.join(audio_directory, f"output{NumOutput}.mp3"))
            NumOutput += 1
            #* print(linemessage + " [line]")

def getAudioLenght():
    # Check if there are any .mp3 files in the directory
    if not mp3_files:
        print("No .mp3 files found in the directory.")
    else:
        # Iterate through each .mp3 file and get its duration
        for mp3_file in mp3_files:
            try:
                audio = MP3(mp3_file)
                duration_milliseconds = int(audio.info.length * 1000)
                duration_seconds = duration_milliseconds // 1000
                duration_milliseconds = duration_milliseconds % 1000
                duration_seconds = duration_seconds % 60
                #print(f"File: {os.path.basename(mp3_file)}, Duration: {duration_seconds} seconds {duration_milliseconds} milliseconds")
            except Exception as e:
                print(f"Error processing file {mp3_file}: {e}")
    return duration_seconds, duration_milliseconds

def ImgtoText():
    # Perform OCR on the image
    output = pytesseract.image_to_string(Image.open(imagetotext_path))
    return output

#Reading the script
txt_file = r"C:\Programing\PYTHON\Projects\ContentMaker\MessageIndex.txt"
linemessage = str
wholemessage = ""

#Audio output directory
audio_directory = r"C:\Programing\PYTHON\Projects\ContentMaker\Audio"

# Get a list of all .mp3 files in the directory
mp3_files = [os.path.join(audio_directory, file) for file in os.listdir(audio_directory) if file.endswith('.mp3')]

# Directory containing the .mp4 files
bmp4_directory = r"C:\Users\crist\Desktop\BotContent\BackgroundVid"
#This varible hold the information on all the files in the directory
mp4_files = [os.path.join(bmp4_directory, file) for file in os.listdir(bmp4_directory) if file.endswith('.mp4')]
cap = cv2.VideoCapture(getrandfile())

# Path to the Tesseract executable (change this according to your installation)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Path to the image file
imagetotext_path = r"C:\Users\crist\Desktop\Cristian mest bild\Skärmbild 2024-05-02 130859.png"

#TexttoAudio()
#getAudioLenght()
#showVid()
#print(getAudioLenght())
#print(ImgtoText())