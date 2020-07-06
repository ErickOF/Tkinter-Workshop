import tkinter as tk
from PIL import ImageTk, Image
from time import sleep
from threading import Thread


# Global vars
running = True

# Defining some constants
TITLE = 'Tkinter Workshop'
# Dimensions
HEIGHT, WIDTH = 400, 400
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

def animate(frames: list):
    """This function makes an animation from an images list.

    Params
    ------------------------------------------------------------------
        frames: list.
            list of image preloaded.
    """
    global running

    # Current frame
    i = 0
    # Number of frames
    frames_number = len(frames)

    # Create canvas
    canvas = tk.Canvas(window, width=400, height=400)  
    canvas.place(x=0, y=0)

    # Set image
    animation = canvas.create_image(0, 0, anchor=tk.NW, image=frames[0])

    # Run while app is executing
    while running:
        canvas.itemconfig(animation, image=frames[i])
        # Next frame
        i += 1

        # If current image is greater than image number
        if i == frames_number:
            # Restart
            i = 0

        # Sleep time
        sleep(0.1)

def close_window():
    """This function is called when a close event is given.
    """
    global running
    running = False
    exit(0)


# Animation 1 path name
animation_path = 'src/animations/animation1/frame'
paths = [animation_path + str(i) + '.gif' for i in range(7)]
frames = [load_image(path) for path in paths]

# Create animation
animation_t = Thread(target=animate, args=(frames,))
animation_t.start()


# Protocol when image is closed
window.protocol('WM_DELETE_WINDOW', close_window)

# Call main loop
window.mainloop()
