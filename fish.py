import random
from grid import Grid

class Fish:

	def __init__(self, row, column, reproduction_timer):
		self.row = row
		self.column = column
		self.reproduction_timer = reproduction_timer

		self.can_reproduce = False

	def reproduce_check(self);
		if self.reproduction_timer == 0:
			self.can_reproduce = True
		else:
			self.reproduction_timer -= 1

	def move(self):
		neighbor_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
		free_cells = []
		for offset in neighbor_offsets:
			new_row = (row + offset[0]) % self.rows
			new_column = (column + offset[1]) % self.columns
			if self.grid.cells[new_row][new_column] == 0:
				free_cells.append([new_row, new_column])
		if len(free_cells) > 0:
			destination_cell = random.choice(free_cells)
		else:
			destination_cell = (self.row, self.column)
		if self.can_reproduce == False:
			self.grid.cells[row, column] = 0
		else:
			self.can_reproduce = False


	def update(self):
		self.reproduce_check()
		self.move() 
