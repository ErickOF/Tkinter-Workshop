import tkinter as tk
from PIL import ImageTk,Image  


# Defining some constants
TITLE = 'Tkinter Workshop'
# Dimensions
HEIGHT, WIDTH = 400, 700
# Background color
BG_COLOR = 'blue'


# Create a main window
window = tk.Tk()

# Get screen dimensions
SCREEN_WIDTH = window.winfo_screenwidth()
SCREEN_HEIGHT = window.winfo_screenheight()

# Get new window position
WINDOW_POS_X = int((SCREEN_WIDTH/2) - (WIDTH/2))
WINDOW_POS_Y = int((SCREEN_HEIGHT/2) - (HEIGHT/2))

# Set title
window.title(TITLE)
# Set geometry
# WIDTHxHEIGHT+X+Y
window.geometry(f'{WIDTH}x{HEIGHT}+{WINDOW_POS_X}+{WINDOW_POS_Y}')
# Set if it's resizable
window.resizable(width=False, height=False)
# Set background
window.config(bg=BG_COLOR)


def load_image(img_path: str) -> ImageTk:
    """This function reads an image from a given path.

    Params
    ------------------------------------------------------------------
        img_path: str.
            path where image is stored.
    
    Returns
    ------------------------------------------------------------------
        an opened image to be used.
    """
    return ImageTk.PhotoImage(Image.open(img_path))


# Create a 300x300 canvas
canvas = tk.Canvas(window, width=700, height=400)  
canvas.place(x=0, y=0)

# Load image
img = load_image('src/imgs/background1.jpg')

# Set image to canvas
canvas.create_image(0, 0, anchor=tk.NW, image=img) 


# Call main loop
window.mainloop()
