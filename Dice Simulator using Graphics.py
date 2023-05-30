#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[1]:


import tkinter as tk
from PIL import Image, ImageTk
import random
import os

window = tk.Tk()
window.geometry("500x360")
window.title("Dice Roll")

# Specify the folder path for dice images
dice_folder = r"C:\Users\admin\Desktop\Test Jupyter\Dice"

# Get a list of all the dice image files in the folder
dice_images = [os.path.join(dice_folder, Dice) for Dice in os.listdir(dice_folder) if Dice.endswith(".png")]

# Create image placeholders
image1 = None
image2 = None

label1 = tk.Label(window, image=image1)
label2 = tk.Label(window, image=image2)

label1.place(x=40, y=100)
label2.place(x=300, y=100)

def dice_roll():
    global image1, image2

    # Load new dice images
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice_images)))
    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice_images)))

    label1.configure(image=image1)
    label2.configure(image=image2)

button = tk.Button(window, text="Roll", bg="green", fg="white", font="Times 20", command=dice_roll)
button.place(x=200, y=0)

window.mainloop()


# In[ ]:





# In[2]:





# In[ ]:




