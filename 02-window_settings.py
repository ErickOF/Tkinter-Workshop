import tkinter as tk


# Defining some constants
TITLE = 'Tkinter Workshop'
# Dimensions
HEIGHT, WIDTH = 400, 400
# Window position
WINDOW_POS_X, WINDOW_POS_Y = 150, 150
# Background color
BG_COLOR = 'blue'


# Create a main window
window = tk.Tk()

# Set title
window.title(TITLE)
# Set icon
#window.iconbitmap('src/icons/py.ico')
# Set geometry
# WIDTHxHEIGHT+X+Y
window.geometry(f'{WIDTH}x{HEIGHT}+{WINDOW_POS_X}+{WINDOW_POS_Y}')
# Set if it's resizable
window.resizable(width=False, height=False)
# Set background
window.config(bg=BG_COLOR)


# Call main loop
window.mainloop()
