import tkinter as tk
from tkinter import messagebox


# Defining some constants
TITLE = 'Tkinter Workshop'
# Dimensions
HEIGHT, WIDTH = 400, 400
# Background color
BG_COLOR = 'blue'
# Label background
BG_LABEL = 'yellow'
# Text color
TEXT_COLOR = 'red'
# Button color
BG_BTN = 'yellow'
# Button text color
BTN_TEXT_COLOR = 'green'
# Text font
TEXT_FONT = 'Ubuntu Monospace'
# Text size
TEXT_SIZE = 30
# Button text size
BTN_TEXT_SIZE = 12


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


# Add label and settings
lbHelloWorld = tk.Label(window, text='Hello World!', bg=BG_LABEL,
                        fg=TEXT_COLOR, font=(TEXT_FONT, TEXT_SIZE),
                        width=21, anchor=tk.W)
# Centering label
lbHelloWorld.place(x=0, y=0)


# Function
def changeText(text):
    print(text)
    lbHelloWorld.config(text='New text')


# Add button
btnChangeText = tk.Button(window, text='Change text', bg=BG_BTN,
                          fg=BTN_TEXT_COLOR, font=(TEXT_FONT, BTN_TEXT_SIZE),
                          activebackground=BTN_TEXT_COLOR,
                          activeforeground=BG_BTN,
                          # Message box
                          #command=lambda: changeText('Param', 2, 3, []))
                          command=lambda: messagebox.showinfo('Title', 'Message'))
btnChangeText.place(x=275, y=360)


# Call main loop
window.mainloop()
