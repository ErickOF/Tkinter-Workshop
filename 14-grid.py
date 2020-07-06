import tkinter as tk
import random


# Defining some constants
TITLE = 'Tkinter Workshop'
# Dimensions
HEIGHT, WIDTH = 465, 530
# Background color
BG_COLOR = 'blue'
# Gameboard
grid = []
# Gameboard dimensions 8x8
N, M = 8, 8
# pos (x, y)
pos = [0, 0]
# pos_enemy (x, y)
posEnemy = [random.randint(1, N - 1), random.randint(1, M - 1)]

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


# Init gameboard
grid = [[tk.Label(window, width=9, height=5, borderwidth=1, relief='solid') for j in range(M)] for i in range(N)]


def drawGrid(grid):
    """This function displays gameboard.
    """
    # Color to start drawing
    color = 'red'

    for i in range(N):
        for j in range(M):
            # Change label bg
            grid[i][j].config(bg=color)
            # Create grid
            grid[i][j].grid(row=i, column=j)

            # Change color
            color = 'white' if color == 'red' else 'red'
        # Change color
        color = 'white' if color == 'red' else 'red'


# Draw grid
drawGrid(grid)

# Draw player
player = tk.Label(window, width=9, height=5, bg='green')
player.grid(column=pos[0], row=pos[1])

# Draw enemy
enemy = tk.Label(window, width=9, height=5, bg='blue')
enemy.grid(column=posEnemy[0], row=posEnemy[1])


def fighting():
    global posEnemy

    if pos[0] == posEnemy[0] and pos[1] == posEnemy[1]:
        posEnemy = [random.randint(0, N - 1), random.randint(0, M - 1)]
        enemy.grid(column=posEnemy[0], row=posEnemy[1])


def left(e):
    if pos[0] > 0:
        pos[0] -= 1
        player.grid(column=pos[0], row=pos[1])

    fighting()

def right(e):
    if pos[0] < N - 1:
        pos[0] += 1
        player.grid(column=pos[0], row=pos[1])

    fighting()

def up(e):
    if pos[1] > 0:
        pos[1] -= 1
        player.grid(column=pos[0], row=pos[1])

    fighting()

def down(e):
    if pos[1] < M - 1:
        pos[1] += 1
        player.grid(column=pos[0], row=pos[1])

    fighting()

# Detect keys
window.bind('<Left>', left)
window.bind('<Right>', right)
window.bind('<Up>', up)
window.bind('<Down>', down)

# Call main loop
window.mainloop()
