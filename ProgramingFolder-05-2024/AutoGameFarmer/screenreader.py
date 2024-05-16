import cv2
import numpy as np
import pyautogui
import time
import subprocess
import sys


def find_image_on_screen(reference_images):
    global settingspicFound, pictureFound, mospicFound 
    print("Code Started")
    
    while True:
        screenshot = pyautogui.screenshot()
        screenshot = np.array(screenshot)
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
        
        runningtask = False
        current_time = time.strftime("%H:%M")
        
        found_locations = []
        
        for reference_image_path in reference_images:
            # Load the reference image
            reference_image = cv2.imread(reference_image_path)
            
            # Perform template matching
            result = cv2.matchTemplate(screenshot, reference_image, cv2.TM_CCOEFF_NORMED)
            
            # Is the picture acurateeeeee? You tell me
            threshold = 0.8
            
            # Get the location where the image matches
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            
            # Check if similarity
            if max_val >= threshold:
                found_locations.append((max_loc, reference_image_path))
        
        if found_locations:
            for location, reference_image_path in found_locations:
                #Class ORANGE
                if reference_image_path == r"C:\Programing\ADOPTMEFARM\referencePic\beach.png":
                    if runningtask == False:
                        runningtask = True
                        print("Runnins task " + current_time)
                        subprocess.call([r"C:\Users\crist\AppData\Local\Programs\AutoHotkey\UX\AutoHotkeyUX.exe", r"C:\Programing\ADOPTMEFARM\autohotkeyFunc\beach.ahk"])
                        time.sleep(80)
                        runningtask = False
                        
                #Class BLUE
                elif reference_image_path == r"C:\Programing\ADOPTMEFARM\referencePic\boared.png":
                    if runningtask == False:
                        runningtask = True
                        print("Runnins task " + current_time)
                        subprocess.call([r"C:\Users\crist\AppData\Local\Programs\AutoHotkey\UX\AutoHotkeyUX.exe", r"C:\Programing\ADOPTMEFARM\autohotkeyFunc\boared.ahk"])
                        time.sleep(30)
                        runningtask = False
                        
                #Class ORANGE                        
                elif reference_image_path == r"C:\Programing\ADOPTMEFARM\referencePic\camping.png":
                    if runningtask == False:
                        runningtask = True
                        print("Runnins task " + current_time)
                        subprocess.call([r"C:\Users\crist\AppData\Local\Programs\AutoHotkey\UX\AutoHotkeyUX.exe", r"C:\Programing\ADOPTMEFARM\autohotkeyFunc\camping.ahk"])
                        time.sleep(80)
                        runningtask = False
                        
                #Class BLUE     
                elif reference_image_path == r"C:\Programing\ADOPTMEFARM\referencePic\drink.png":
                    if runningtask == False:
                        runningtask = True
                        print("Runnins task " + current_time)
                        subprocess.call([r"C:\Users\crist\AppData\Local\Programs\AutoHotkey\UX\AutoHotkeyUX.exe", r"C:\Programing\ADOPTMEFARM\autohotkeyFunc\drink.ahk"])
                        time.sleep(30)
                        runningtask = False
                        
                #Class BLUE
                elif reference_image_path == r"C:\Programing\ADOPTMEFARM\referencePic\eat.png":
                    if runningtask == False:
                        runningtask = True
                        print("Runnins task " + current_time)
                        subprocess.call([r"C:\Users\crist\AppData\Local\Programs\AutoHotkey\UX\AutoHotkeyUX.exe", r"C:\Programing\ADOPTMEFARM\autohotkeyFunc\eat.ahk"])
                        time.sleep(30)
                        runningtask = False
                        
                #Class ORANGE   
                elif reference_image_path == r"C:\Programing\ADOPTMEFARM\referencePic\pizza.png":
                    if runningtask == False:
                        runningtask = True
                        print("Runnins task " + current_time)
                        subprocess.call([r"C:\Users\crist\AppData\Local\Programs\AutoHotkey\UX\AutoHotkeyUX.exe", r"C:\Programing\ADOPTMEFARM\autohotkeyFunc\pizza.ahk"])
                        time.sleep(80)
                        runningtask = False
                        
                #Class ORANGE
                elif reference_image_path == r"C:\Programing\ADOPTMEFARM\referencePic\salon.png":
                    if runningtask == False:
                        runningtask = True
                        print("Runnins task " + current_time)
                        subprocess.call([r"C:\Users\crist\AppData\Local\Programs\AutoHotkey\UX\AutoHotkeyUX.exe", r"C:\Programing\ADOPTMEFARM\autohotkeyFunc\salon.ahk"])
                        time.sleep(80)
                        runningtask = False
                        
                #Class ORANGE
                elif reference_image_path == r"C:\Programing\ADOPTMEFARM\referencePic\school.png":
                    if runningtask == False:
                        runningtask = True
                        print("Runnins task " + current_time)
                        subprocess.call([r"C:\Users\crist\AppData\Local\Programs\AutoHotkey\UX\AutoHotkeyUX.exe", r"C:\Programing\ADOPTMEFARM\autohotkeyFunc\school.ahk"])
                        time.sleep(80)
                        runningtask = False
                        
                #Class BLUE  
                elif reference_image_path == r"C:\Programing\ADOPTMEFARM\referencePic\shower.png":
                    if runningtask == False:
                        runningtask = True
                        print("Runnins task " + current_time)
                        subprocess.call([r"C:\Users\crist\AppData\Local\Programs\AutoHotkey\UX\AutoHotkeyUX.exe", r"C:\Programing\ADOPTMEFARM\autohotkeyFunc\shower.ahk"])
                        time.sleep(30)
                        runningtask = False
                        
                #Class ORANGE
                elif reference_image_path == r"C:\Programing\ADOPTMEFARM\referencePic\sick.png":
                    if runningtask == False:
                        runningtask = True
                        print("Runnins task " + current_time)
                        subprocess.call([r"C:\Users\crist\AppData\Local\Programs\AutoHotkey\UX\AutoHotkeyUX.exe", r"C:\Programing\ADOPTMEFARM\autohotkeyFunc\sick.ahk"])
                        time.sleep(80)
                        runningtask = False
                        
                #Class BLUE
                elif reference_image_path == r"C:\Programing\ADOPTMEFARM\referencePic\sleep.png":
                    if runningtask == False:
                        runningtask = True
                        print("Runnins task " + current_time)
                        subprocess.call([r"C:\Users\crist\AppData\Local\Programs\AutoHotkey\UX\AutoHotkeyUX.exe", r"C:\Programing\ADOPTMEFARM\autohotkeyFunc\sleep.ahk"])
                        time.sleep(30)
                        runningtask = False
                
                elif reference_image_path == r"C:\Programing\ADOPTMEFARM\referencePic\AFK.png":
                    print("Roblox went afk " + current_time)
                    sys.exit()
                        
        else:
            #ADD ANTI AFK IF NEEDED
            print("No Tasks " + current_time)
        
        
        # Time between screen checks
        time.sleep(5)

#Add more pictures to the table/array whatever you wanna call it
reference_image_paths = [r"C:\Programing\ADOPTMEFARM\referencePic\AFK.png",r"C:\Programing\ADOPTMEFARM\referencePic\beach.png", r"C:\Programing\ADOPTMEFARM\referencePic\boared.png",
                         r"C:\Programing\ADOPTMEFARM\referencePic\camping.png", r"C:\Programing\ADOPTMEFARM\referencePic\drink.png", r"C:\Programing\ADOPTMEFARM\referencePic\eat.png",
                         r"C:\Programing\ADOPTMEFARM\referencePic\pizza.png", r"C:\Programing\ADOPTMEFARM\referencePic\salon.png", r"C:\Programing\ADOPTMEFARM\referencePic\school.png",
                         r"C:\Programing\ADOPTMEFARM\referencePic\shower.png", r"C:\Programing\ADOPTMEFARM\referencePic\sick.png", r"C:\Programing\ADOPTMEFARM\referencePic\sleep.png"]
find_image_on_screen(reference_image_paths)  

