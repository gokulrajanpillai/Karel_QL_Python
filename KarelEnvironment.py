from Tkinter import *

ui_tkinter = Tk()

DIM_X = 5
DIM_Y = 5

BLOCK_DIM = 50

karel_actions = ["left", "right", "up", "down"]

karel_environment = Canvas(ui_tkinter, width=DIM_X, height=DIM_Y)

karel_position = ( 0, DIM_Y-1)

walls = []
destination = []

def draw_environment():
	for i in range(DIM_X):
		for j in range(DIM_Y):
			karel_environment.create_rectangle(i*BLOCK_DIM, j*BLOCK_DIM, (i+1)*BLOCK_DIM, (j+1)*BLOCK_DIM, fill="white", width=1)

draw_environment()
