from pyautogui import *
from timeit import default_timer as timer
import pyautogui 
import time 
import keyboard 
import random
import win32api, win32con
import cv2

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    button=pyautogui.locateOnScreen('a.png', region=(860,130,200,861), confidence=0.7)
    if button != None:
        location=pyautogui.center(button)
        print(location)
        print("I can see it")
        click(location[0],location[1])
        time.sleep(1)
        click(location[0],location[1])
        
        E=False
        start = 0
        while not E:
            if start == 0:
                start = timer()
            if pyautogui.pixelMatchesColor(368, 720, (255, 255, 255)) or pyautogui.pixelMatchesColor(368, 720, (64, 61, 57)):
                print("WHITE")
                time.sleep(1.5)
                click(27, 63)
                time.sleep(1.7)
                pyautogui.press('F5')
                time.sleep(2.1)
                E=True
            end = timer()    
            if (end-start)> 58:
                print("BLACK")
                pyautogui.press('F5')
                start = 0
                time.sleep(1)
        
    else:
        print("I am unable to see it")
        time.sleep(1)
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        arrow=pyautogui.locateOnScreen('arrow.png', region=(1160,870,60,60))
        if arrow != None:
            localarrow=pyautogui.center(arrow)
            print("Next Page")
            click(localarrow[0],localarrow[1])
            click(309, 680)
            time.sleep(1)
        if pyautogui.pixelMatchesColor(368, 720, (255, 255, 255)) or pyautogui.pixelMatchesColor(368, 720, (64, 61, 57)):
            print("MISSCLICK")
            time.sleep(0.5)
            click(27, 63)
            time.sleep(1)

        
