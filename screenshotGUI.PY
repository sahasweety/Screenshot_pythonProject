import time
import pyautogui
import tkinter as tk

def screenshot():
    name = int(round(time.time() * 1000))
    name = 'C:/Users/Aaditya/OneDrive/Desktop/Python/python/screenshot data/{}.png'.format(name)
    img = pyautogui.screenshot(name)
    img.show()


raat = tk.Tk()
frame = tk.Frame(raat)
frame.pack()

button =tk.Button(
    frame,
    text="Take screenshot ",
    command=screenshot)

button.pack(side=tk.LEFT)
close = tk.Button(
    frame,
    text="QUIT ",
    command=quit)
close.pack (side=tk.LEFT)

raat.mainloop()
