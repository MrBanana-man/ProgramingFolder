#USELESS KEYBORD MOVER

import win32api
import win32con
import time
import random
from pyautogui import * 
import pyautogui
import numpy as np
import keyboard

time.sleep(2)

def smooth_move_to(x, y, steps=100):
    # Get the current mouse position
    cur_x, cur_y = win32api.GetCursorPos()
    
    # Calculate the step increments for x and y coordinates with random variation
    step_x = (x - cur_x) / steps
    step_y = (y - cur_y) / steps
    
    # Add random variation to each step
    step_x_with_variation = [step_x + random.uniform(-0.1, 0.1) for _ in range(steps)]
    step_y_with_variation = [step_y + random.uniform(-0.1, 0.1) for _ in range(steps)]
    
    # Perform the smooth movement
    for i in range(steps):
        new_x = int(cur_x + step_x_with_variation[i] * i)
        new_y = int(cur_y + step_y_with_variation[i] * i)
        win32api.SetCursorPos((new_x, new_y))
        time.sleep(0.01)  # Adjust this value to control the speed of movement

def click(x, y):
    # Smoothly move the mouse to the specified position
    smooth_move_to(x, y)
    
    # Perform a left mouse button click
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.1)  # Optional delay for visual effect
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


pyautogui.keyDown("b")
time.sleep(0.1)
pyautogui.keyUp("b")


target_x = 2941
target_y = 1081
    
click(target_x, target_y)
