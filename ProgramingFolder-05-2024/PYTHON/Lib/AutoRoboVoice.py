from gtts import gTTS
import os

output_directory = r"C:\Programing\PYTHON\Projects\ContentMaker\Audio"

RobotText = 'Hello, I am a robot'
output_file = os.path.join(output_directory, 'output.mp3')


gTTS(text= RobotText, lang='en', slow=False).save(output_file)


