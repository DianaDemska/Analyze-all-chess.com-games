from pyautogui import *
from timeit import default_timer as timer
import pyautogui 
import time 
import keyboard 
import random
import win32api, win32con
start = 0
E=False
while not E:
    if start == 0:
        start = timer()
    if pyautogui.pixelMatchesColor(368, 720, (255, 255, 255)) or pyautogui.pixelMatchesColor(368, 720, (64, 61, 57)):
        print("WHITE")
        time.sleep(1.5)
        click(27, 63)
        time.sleep(1.5)
        pyautogui.press('F5')
        time.sleep(1.5)
        E=True
    end = timer()    
    if (end-start)> 5:
                print("Hello")
