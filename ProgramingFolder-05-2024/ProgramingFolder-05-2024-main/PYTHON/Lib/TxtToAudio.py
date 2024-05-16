from gtts import gTTS
import os

txt_file = None #dir to the .txt file that you want to read from
linemessage = str

output_directory = None #dir to the output folder
NumOutput = 0

with open(txt_file, 'r') as file:
    # Read the file line by line
    for line in file:
        linemessage = line.strip()
        gTTS(text = linemessage, lang='en', slow=False).save(os.path.join(output_directory, f"output{NumOutput}.mp3"))
        NumOutput += 1
        #* print(linemessage + " [line]")
