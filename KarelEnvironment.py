import KarelController
from Tkinter import *

tk_ui = Tk()

# Dimension of the length and breadth of the cells in KarelEnvironment
BLOCK_DIM = 100

# Dimensions of KarelEnvironment
DIM_X = 5
DIM_Y = 5

# Actions that are available per instance of the system
karel_actions = ["up", "down", "left", "right"]

# Canvas element is the base UI on which all the other elements are drawn
karel_environment = Canvas(tk_ui, width=DIM_X*BLOCK_DIM, height=DIM_Y*BLOCK_DIM)

# UI element representing Karel
karel = None

# Initial position of Karel in the environment
karel_position = (0, DIM_Y-1)

# Value deciding whether Karel took the same number of steps to reach a point
# Used to find the terminal state of the algorithm
karel_score = 1

# Flag triggering restart of the KarelEnvironment in case Karel reached a terminal state
restart = False
walk_reward = -0.04

# Walls representing the obstacles
walls = [(1, 1), (2, 4)]

# Reward cells defined in the format (x-position, y-position, color, reward)
rewarding_cells = [(4, 1, "red", -1), (4, 4, "blue", 1)]

# Number of times Karel reached terminal state
terminal_count = 0

def render_environment():
    global rewarding_cells, walls, BLOCK_DIM, DIM_X, DIM_Y, karel_position
    for i in range(DIM_X):
        for j in range(DIM_Y):
            karel_environment.create_rectangle(i*BLOCK_DIM, j*BLOCK_DIM, (i+1)*BLOCK_DIM, (j+1)*BLOCK_DIM, fill="white", width=1)
    for (i, j, c, w) in rewarding_cells:
        karel_environment.create_rectangle(i*BLOCK_DIM, j*BLOCK_DIM, (i+1)*BLOCK_DIM, (j+1)*BLOCK_DIM, fill=c, width=1)
    for (i, j) in walls:
        karel_environment.create_rectangle(i*BLOCK_DIM, j*BLOCK_DIM, (i+1)*BLOCK_DIM, (j+1)*BLOCK_DIM, fill="black", width=1)

# Make Karel move from the current position to dx and dy direction
def move_karel(dx, dy):
    global karel_position, DIM_X, DIM_Y, karel_score, walk_reward, karel, restart, terminal_count
    if restart == True:
        restart_game()
    new_x = karel_position[0] + dx
    new_y = karel_position[1] + dy

    karel_score += walk_reward

    # Check whether the new position of Karel falls under the KarelEnvironment boundaries
    if (new_x >= 0) and (new_x < DIM_X) and (new_y >= 0) and (new_y < DIM_Y) and not ((new_x, new_y) in walls):
        karel_environment.coords(karel, new_x*BLOCK_DIM+BLOCK_DIM*2/10, new_y*BLOCK_DIM+BLOCK_DIM*2/10, new_x*BLOCK_DIM+BLOCK_DIM*8/10, new_y*BLOCK_DIM+BLOCK_DIM*8/10)
        karel_position = (new_x, new_y)

    # Check whether the new position made Karel move into a rewarding/ terminating cell
    for (i, j, c, w) in rewarding_cells:
        if new_x == i and new_y == j:
            karel_score -= walk_reward
            karel_score += w
            if karel_score > 0:
                KarelController.path_scores.append(karel_score)
                terminal_count += 1
                print "Success! score: ", karel_score
            else:
                print "Fail! score: ", karel_score
            restart = True
            return

def restart_game():
    global karel_position, karel_score, karel, restart
    karel_position = (0, DIM_Y-1)
    karel_score = 1
    restart = False
    karel_environment.coords(karel, karel_position[0]*BLOCK_DIM+BLOCK_DIM*2/10, karel_position[1]*BLOCK_DIM+BLOCK_DIM*2/10, karel_position[0]*BLOCK_DIM+BLOCK_DIM*8/10, karel_position[1]*BLOCK_DIM+BLOCK_DIM*8/10)

def has_restarted():
    return restart

def render_karel():
    global karel
    karel = karel_environment.create_rectangle(karel_position[0]*BLOCK_DIM+BLOCK_DIM*2/10, karel_position[1]*BLOCK_DIM+BLOCK_DIM*2/10,
                            karel_position[0]*BLOCK_DIM+BLOCK_DIM*8/10, karel_position[1]*BLOCK_DIM+BLOCK_DIM*8/10, fill="white", width=1, tag="karel")

def init_karel_environment_canvas():
    karel_environment.grid(row=0, column=0)

# Move karel up
def call_up(event):
    move_karel(0, -1)
# Move karel down
def call_down(event):
    move_karel(0, 1)
# Move karel left
def call_left(event):
    move_karel(-1, 0)
# Move karel right
def call_right(event):
    move_karel(1, 0)

# Define key actions for controlling Karel with arrow keys from keyboard
def define_keyboard_actions():
    # For moving around Karel manually with arrow keys
    tk_ui.bind("<Up>", call_up)
    tk_ui.bind("<Down>", call_down)
    tk_ui.bind("<Right>", call_right)
    tk_ui.bind("<Left>", call_left)

# Start game the environment
def start_rendering():
    tk_ui.mainloop()

def init_and_start():
    render_environment()
    render_karel()
    init_karel_environment_canvas()
    start_rendering()
    define_keyboard_actions()
