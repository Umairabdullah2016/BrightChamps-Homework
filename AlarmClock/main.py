#Library Requirements: Pillow 
from PIL import Image, ImageTk
import tkinter as tk
import os
import datetime
import tkinter.font as tkfont


root = tk.Tk()
image = Image.open(r"AlarmClock/clock.png")
img = ImageTk.PhotoImage(image)

root.title("Alarm Clock")
label2 = tk.Label(root, image=img)
label2.pack()

# Initial time display
current_time = datetime.datetime.now().strftime("%H:%M:%S")
label1 = tk.Label(root, text=f"UK Time: {current_time}", font=("Arial", 50))
label1.pack()

def update_counter():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    label1.config(text=f"UK Time: {current_time}")
    root.after(1, update_counter)  # call again after 1 second

update_counter()
    
root.mainloop()