import time
import pyautogui

def screenshot():
    name = int(round(time.time() * 1000))
    name = 'C:/Users/Aaditya/OneDrive/Desktop/Python/python/.ipynb_checkpoints/screenshot data{}.png'.format(name)
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()

screenshot()
