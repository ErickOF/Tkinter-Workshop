import tkinter as tk


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
# Set icon
#window.iconbitmap('src/icons/py.ico')
# Set geometry
# WIDTHxHIGHT+X+Y
window.geometry(f'{WIDTH}x{HEIGHT}+{WINDOW_POS_X}+{WINDOW_POS_Y}')
# Set if it's resizable
window.resizable(width=False, height=False)
# Set background
window.config(bg=BG_COLOR)


# Add label
lbHelloWorld = tk.Label(window, text='Hello World!')
lbHelloWorld.place(x=150, y=20)


# Call main loop
window.mainloop()
