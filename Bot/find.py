import pyautogui
import time
from PIL import Image
time.sleep(0.7)
iml = pyautogui.screenshot(region=(1450,220,190,150))
iml.save(r"C:\Users\nikiw\Desktop\Bot2\saveimage.png")
img = Image.open(r"C:\Users\nikiw\Desktop\Bot2\saveimage.png")
img.show()




