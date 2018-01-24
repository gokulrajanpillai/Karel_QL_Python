from Tkinter import *

# Initialize tkinter instance for rendering UI
tkinter = Tk()

# Number of blocks horizondally in the environment
DIM_X = 5

# Number of blocks vertically in the environment
DIM_Y = 5

# Length and breadth value of each block
BLOCK_DIM = 50

# Start state of Karel in the environment
KAREL_START_STATE = (0, 4)

# End state of Karel in the environment
KAREL_END_STATE = (4, 4)

# Possible actions in the environment
karel_actions = ["left", "right", "up", "down"]

# Canvas instance for rendering the environment
karel_canvas = Canvas(tkinter, width=DIM_X*BLOCK_DIM, height=DIM_Y*BLOCK_DIM)

# Current state(position) of Karel in the environment
karel_current_state = KAREL_START_STATE

# Array representing the walls/ blocks in the environment
walls = []

# UI element in the KarelEnvironment representing the Karel view
karel = None

# Variable to trigger reset of KarelEnvironment
should_restart = False

# Draw the tiles for the Karel environment, inside the canvas
def draw_tiles():
	for i in range(DIM_X):
		for j in range(DIM_Y):
			color = "white"
			if (i, j) == KAREL_END_STATE:
				color = "green"
			karel_canvas.create_rectangle(i*BLOCK_DIM, j*BLOCK_DIM, (i+1)*BLOCK_DIM, (j+1)*BLOCK_DIM, fill=color, width=1)

# Draw Karel for the Karel environment, inside the canvas
def draw_karel():
	# Rectangle in the Canvas representing Karel
	karel = karel_canvas.create_rectangle(karel_current_state[0]*BLOCK_DIM+BLOCK_DIM*2/10, karel_current_state[1]*BLOCK_DIM+BLOCK_DIM*2/10, karel_current_state[0]*BLOCK_DIM+BLOCK_DIM*8/10, karel_current_state[1]*BLOCK_DIM+BLOCK_DIM*8/10, fill="orange", width=1, tag="karel")

# Initialize the canvas
def initialize_canvas():
	karel_canvas.grid(row=0, column=0)

# Draw Karel environment
def draw_environment():
	draw_tiles()
	draw_karel()
	initialize_canvas()

# Restart environment with Karel back in its initial position
def restart_environment():
	karel_canvas.coords(karel, karel_current_state[0]*Width+Width*2/10, karel_current_state[1]*Width+Width*2/10, karel_current_state[0]*Width+Width*8/10, karel_current_state[1]*Width+Width*8/10)

# Move Karel with delta_x and delta_y
def move_karel(delta_x, delta_y):
	global karel_current_state, should_restart
	print("new_pos",delta_x, delta_y)
	print("karel_current_state: ",karel_current_state)
	new_karel_pos_x = karel_current_state[0]+delta_x
	new_karel_pos_y = karel_current_state[1]+delta_y
	if should_restart == True:
		restart_environment()
	if (new_karel_pos_x >= 0) and (new_karel_pos_x < DIM_X) and (new_karel_pos_y >= 0) and (new_karel_pos_y < DIM_Y) and not ((new_karel_pos_x, new_karel_pos_y) in walls):
		karel_canvas.coords(me, new_karel_pos_x*Width+Width*2/10, new_karel_pos_y*Width+Width*2/10, new_karel_pos_x*Width+Width*8/10, new_karel_pos_y*Width+Width*8/10)
		karel_current_state = (new_karel_pos_x, new_karel_pos_y)
	return karel_current_state

# Start Tkinter for rendering the UI for the KarelEnvironment
def start_tkinter():
    tkinter.mainloop()

# Initialize and start the environment
def init_and_start():
	draw_environment()
	start_tkinter()
