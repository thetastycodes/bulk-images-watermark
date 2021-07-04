'''
Bulk Images Watermark
=====================

July, 2021
The Tasty Codes (T2C) teams.

help.thetastycodes@gmail.com
https://github.com/thetastycodes
'''

import os
from tkinter import *
from tkinter import filedialog as fd, simpledialog as sd
from PIL import Image, ImageDraw, ImageFont

def clear():
    global list_box
    global files
    list_box.delete(0, 'end')
    files.clear()


def watermark():
    global root
    global files

    global files
    global list_box

    if files:
        text = sd.askstring(title="Watermark",
                            prompt="Watermark text:")

        for i, f in enumerate(files):
            file_extension = os.path.splitext(f.name)[-1]
            im = Image.open(f.name)
            width, height = im.size

            draw = ImageDraw.Draw(im)
            font = ImageFont.truetype("arial.ttf", 18)
            text_width, text_height = draw.textsize(
                text, 
                font=font
            )

            # calculate x,y coordinates 
            # of the text
            margin_size = 9
            x = width - text_width - margin_size
            y = height - text_height - margin_size
            draw.text(
                (x, y), 
                text, 
                font=font, 
                fill="#fafe25"
            )
            im.save(f'./images/watermark-'
                    f'{i+1}{file_extension}')

        # Clear all files and list box
        clear()


def add_image_to_list():
    global root
    global files
    global list_box

    for i, f in enumerate(files):
        list_box.insert(i+1, f.name)

def open_images():
    global files
    filetypes = (
        ('png file', '*.png'),
        ('jpeg file', '*.jpeg'),
        ('jpg file', '*.jpg'),
    )

    # Show the open file dialog
    all_file = fd.askopenfiles(filetypes=filetypes)

    # Clear all files and list box
    # if files is exists
    if files:
        clear()
    
    for f in all_file:
        files.append(f)

    # Call create list after append all file
    add_image_to_list()


root = Tk()
root.title("Bulk Images Watermark")
root.geometry("300x200")
root.resizable(0, 0)

# Create menu
menu = Menu(root)
menu.add_command(label="Open Images...", command=open_images)
menu.add_command(label="Run", command=watermark)
menu.add_command(label="Clear", command=clear)
root.config(menu=menu)

# Create list box widget
list_box = Listbox(root, width=300)
list_box.pack()

# Create list files
files = []

if __name__ == '__main__':
    root.mainloop()