# twoRolling dies with image 

import tkinter
from PIL import Image, ImageTk
import random

# th represents the main window
root = tkinter.Tk()
root.geometry('400x400')
root.title("Ranjit's  Roll the Dice")


# Adding label into the frame
l0 = tkinter.Label(root, text="")
l0.pack()

# adding label with different font and formatting
l1 = tkinter.Label(root, text="Hello from Ranjit mogane", fg = "light green",
        bg = "dark green",
        font = "Helvetica 16 bold italic")
l1.pack()

# images
dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']
# simulating the dice with random numbers between 0 to 6 and generating image
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# construct a label widget for image
label1 = tkinter.Label(root, image=image1)
label2 = tkinter.Label(root, image=image2)
label1.image = image1
label2.image = image2

# packing a widget in the parent widget 
label1.pack( expand=True)
label2.pack( expand=True)

# function activated by button
def rolling_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    label1.configure(image=image1)
    # keep a reference
    label1.image = image1
    label2.configure(image=image2)
    # keep a reference
    label2.image = image2


# adding button, and command will use rolling_dice function
button = tkinter.Button(root, text='Roll the Dice', fg='blue',bd=2, command=rolling_dice)

# pack a widget in the parent widget
button.pack( expand=True)

# call the mainloop of Tk

# keeps window open
root.mainloop()
