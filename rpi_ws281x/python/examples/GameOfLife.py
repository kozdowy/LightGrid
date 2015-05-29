from time import sleep
import time
import random
from LightGrid import LightGrid
from neopixel import Color
class Game(object):
	def __init__(self, state, infinite_board = True):
		self.state = state
		self.width = state.width
		self.height = state.height
		self.infinite_board = infinite_board

	def step(self, count = 1):
		for generation in range(count):
			new_board = [[False] * self.width for row in range(self.height)]

			for y, row in enumerate(self.state.board):
				for x, cell in enumerate(row):
					neighbours = self.neighbours(x, y)
					previous_state = self.state.board[y][x]
					should_live = neighbours == 3 or (neighbours == 2 and previous_state == True)
					new_board[y][x] = should_live

			self.state.board = new_board

	def neighbours(self, x, y):
		count = 0

		for hor in [-1, 0, 1]:
			for ver in [-1, 0, 1]:
				if not hor == ver == 0 and (self.infinite_board == True or (0 <= x + hor < self.width and 0 <= y + ver < self.height)):
					count += self.state.board[(y + ver) % self.height][(x + hor) % self.width]

		return count
	
	def display(self):
		self.state.display()

class State(object):
	def __init__(self, width, height):
		active_cells = []
		random.seed(time.time())
		
		#for y, row in enumerate(positions.splitlines()):
	#		for x, cell in enumerate(row.strip()):
		for i in range(width):
			for j in range(height):
				if random.randint(0, 10) >= 8:
					active_cells.append((j,i))
		board = [[False] * width for row in range(height)]
		#print board
		for cell in active_cells:
			#print cell[0], cell[1]
			board[cell[0]][cell[1]] = True

		self.board = board
		self.width = width
		self.height = height
		self.grid = LightGrid(height, width)
	
	def display(self):
		output = ''
		for y, row in enumerate(self.board):
			for x, cell in enumerate(row):
				if self.board[y][x]:
					#output += "0 " + str(y) + " " + str(x) + " FFFFFF\n"
					self.grid.setPixel(0, y, x, Color(255, 255 ,255))
				else:
					#output += "0 " + str(y) + " " + str(x) + " 000000\n"
					self.grid.setPixel(0, y, x, Color(0, 0, 0))
		self.grid.showGrid()

glider = """ oo.
	     o.o
	     o.. """
my_game = Game(State(width = 26, height = 20))
my_game.display()

while True:
	sleep(0.1)
	my_game.step(1)
	my_game.display()
	
