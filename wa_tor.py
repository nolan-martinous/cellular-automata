from grid import Grid
import random

class Wator:
	def __init__(self, width, height, cell_size):
		self.grid = Grid(width, height, cell_size)
		self.energy_grid = Grid(width, height, cell_size)
		self.reproduce_grid = Grid(width, height, cell_size)
		self.rows = height // cell_size
		self.columns = width // cell_size
		self.run = False
		self.rule_list = ['standard']
		self.rule_index = 0

		self.fish_reproduce = 5
		self.shark_reproduce = 50
		self.energy_per_fish = 2
		self.shark_energy = 10

		for row in range(self.rows):
			for column in range(self.columns):
				self.reproduce_grid.cells[row][column] = -1
				self.energy_grid.cells[row][column] = -1

	def draw(self, window):
		self.grid.draw(window)

	def update(self):
		if self.is_running():
			for row in range(self.rows):
				for column in range(self.columns):

					# determine free adjacent cells
					free_cells = []
					neighbor_offsets = [(-1, 0), (0, -1), (0, 1), (1, 0)]
					for offset in neighbor_offsets:
						new_row = (row + offset[0]) % self.rows
						new_column = (column + offset[1]) % self.columns
						if self.grid.cells[new_row][new_column] == 0:
							free_cells.append([new_row, new_column])

					# if there is a free adjacent cell
					if len(free_cells) > 0:
						destination = random.choice(free_cells)
					else:
						destination = (row, column)

					# if cell is a fish
					if self.grid.cells[row][column] == 3:

							# if fish cant reproduce
							if self.reproduce_grid.cells[row][column] > 0:
								self.grid.cells[row][column] = 0
								reproduce_timer = self.reproduce_grid.cells[row][column] - 1
								self.reproduce_grid.cells[row][column] = -1

							# if fish can reproduce
							else:
								reproduce_timer = self.fish_reproduce
								self.reproduce_grid.cells[row][column] = self.fish_reproduce

							# movement 
							self.grid.cells[destination[0]][destination[1]] = 3
							self.reproduce_grid.cells[destination[0]][destination[1]] = reproduce_timer


					# if cell is a shark
					if self.grid.cells[row][column] == 1:

							# determine adjacent fish
							fish_cells = []
							neighbor_offsets = [(-1, 0), (0, -1), (0, 1), (1, 0)]
							for offset in neighbor_offsets:
								new_row = (row + offset[0]) % self.rows
								new_column = (column + offset[1]) % self.columns
								if self.grid.cells[new_row][new_column] == 3:
									fish_cells.append([new_row, new_column])

							energy = self.energy_grid.cells[row][column]

							# if there is an adjacent fish
							if len(fish_cells) > 0:
								destination = random.choice(fish_cells)
								energy += self.energy_per_fish
								if energy > self.shark_energy:
									energy = self.shark_energy

							# if shark runs out of energy
							if energy <= 0:
								self.grid.cells[row][column] = 0
								self.energy_grid.cells[row][column] = -1
								self.reproduce_grid.cells[row][column] = -1

							else:
								# if shark cant reproduce
								if self.reproduce_grid.cells[row][column] > 0:
									self.grid.cells[row][column] = 0
									reproduce_timer = self.reproduce_grid.cells[row][column] - 1
									self.reproduce_grid.cells[row][column] = -1
									self.energy_grid.cells[row][column] = -1

								# if shark can reproduce
								else:
									reproduce_timer = self.shark_reproduce
									self.reproduce_grid.cells[row][column] = self.shark_reproduce

								# movement 
								self.grid.cells[destination[0]][destination[1]] = 1
								self.reproduce_grid.cells[destination[0]][destination[1]] = reproduce_timer
								self.energy_grid.cells[destination[0]][destination[1]] = energy - 1





	def is_running(self):
		return self.run

	def start(self):
		self.run = True

	def stop(self):
		self.run = False

	def clear(self):
		if self.is_running() == False:
			self.grid.clear()

	def create_random_state(self):
		if self.is_running() == False:
			self.grid.fill_random()

	def toggle_cell(self, row, column):
		if self.is_running() == False:
			if self.grid.cells[row][column] == 0:
				self.grid.cells[row][column] = 3
				self.reproduce_grid.cells[row][column] = self.fish_reproduce
			elif self.grid.cells[row][column] == 3:
				self.grid.cells[row][column] = 1
				self.reproduce_grid.cells[row][column] = self.shark_reproduce
				self.energy_grid.cells[row][column] = self.shark_energy
			else:
				self.grid.cells[row][column] = 0
				self.reproduce_grid.cells[row][column] = 0

	def rule_down(self):
		if self.is_running() == False:
			if self.rule_index < len(self.rule_list) - 1:
				self.rule_index += 1
			else:
				self.rule_index = 0

	def rule_up(self):
		if self.is_running() == False:
			if self.rule_index > 0:
				self.rule_index -= 1
			else:
				self.rule_index = len(self.rule_list) - 1