import pygame, random

NAVY = (31, 81, 255)
GREY = (55, 55, 55)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)

class Grid:
	def __init__(self, width, height, cell_size):
		self.rows = height // cell_size
		self.columns = width // cell_size
		self.cell_size = cell_size
		self.cells = [[0 for _ in range(self.columns)] for _ in range(self.rows)]

	def draw(self, window):
		for row in range(self.rows):
			for column in range(self.columns):
				if self.cells[row][column] == 0:
					color = GREY
				elif self.cells[row][column] == 1:
					color = NAVY
				elif self.cells[row][column] == 2:
					color = RED
				elif self.cells[row][column] == 3:
					color = GREEN
				elif self.cells[row][column] == 4:
					color = YELLOW
				elif self.cells[row][column] == 5:
					color = MAGENTA
				elif self.cells[row][column] == 6:
					color = WHITE
				elif self.cells[row][column] == 7:
					color = CYAN
				elif self.cells[row][column] == 'ANT':
					color = RED
				elif self.cells[row][column] == 'SELECT':
					color = GREEN
				elif self.cells[row][column] == 'WHITE':
					color = WHITE
				pygame.draw.rect(window, color, (column * self.cell_size, row * self.cell_size, self.cell_size -1, self.cell_size - 1))

	def fill_random(self):
		for row in range(self.rows):
			for column in range(self.columns):
				self.cells[row][column] = random.choice([1, 0, 0, 0])

	def clear(self):
		for row in range(self.rows):
			for column in range(self.columns):
				self.cells[row][column] = 0

	def toggle_cell(self, row, column):
		if 0 <= row < self.rows and 0 <= column < self.columns:
			self.cells[row][column] = not self.cells[row][column]