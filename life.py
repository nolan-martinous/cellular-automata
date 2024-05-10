from grid import Grid
import rules

class Life:
	def __init__(self, width, height, cell_size):
		self.grid = Grid(width, height, cell_size)
		self.temp_grid = Grid(width, height, cell_size)
		self.rows = height // cell_size
		self.columns = width // cell_size
		self.run = False
		self.rule_list = ["conway's", 'day and night', 'replicator']
		self.rule_index = 0

	def draw(self, window):
		self.grid.draw(window)

	def count_live_neighbors(self, grid, row, column):
		live_neighbors = 0

		neighbor_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
		for offset in neighbor_offsets:
			new_row = (row + offset[0]) % self.rows
			new_column = (column + offset[1]) % self.columns
			if self.grid.cells[new_row][new_column] == 1:
				live_neighbors += 1

		return live_neighbors

	def update(self):
		if self.is_running():
			for row in range(self.rows):
				for column in range(self.columns):
					live_neighbors = self.count_live_neighbors(self.grid, row, column)
					cell_value = self.grid.cells[row][column]

					self.rule = self.rule_list[self.rule_index]

					if self.rule == "conway's":
						self.temp_grid.cells[row][column] = rules.conways(cell_value, live_neighbors)
					elif self.rule == 'day and night':
						self.temp_grid.cells[row][column] = rules.day_and_night(cell_value, live_neighbors)
					elif self.rule == 'replicator':
						self.temp_grid.cells[row][column] = rules.replicator(cell_value, live_neighbors)

			for row in range(self.rows):
				for column in range(self.columns):
					self.grid.cells[row][column] = self.temp_grid.cells[row][column]

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
			self.grid.toggle_cell(row, column)

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