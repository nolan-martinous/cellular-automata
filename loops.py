from grid import Grid
import langston_loops_patterns
import langston_cneswc

class Loops:
	def __init__(self, width, height, cell_size):
		self.grid = Grid(width, height, cell_size)
		self.temp_grid = Grid(width, height, cell_size)
		self.rows = height // cell_size
		self.columns = width // cell_size
		self.run = False
		self.rule_list = ["Langston's"]
		self.rule_index = 0

	def draw(self, window):
		self.grid.draw(window)

	def cneswc(self, grid, row, column):
		c = self.grid.cells[row][column]

		neighbor_offsets = [(0, -1), (-1, 0), (0, 1), (1, 0)]
		offset_index = 0

		for offset in neighbor_offsets:
			new_row = (row + offset[0]) % self.rows
			new_column = (column + offset[1]) % self.columns
			if self.grid.cells[new_row][new_column] == None:
				self.grid.cells[new_row][new_column] = 0
			if offset_index == 0:
				n = self.grid.cells[new_row][new_column]
			elif offset_index == 1:
				e = self.grid.cells[new_row][new_column]
			elif offset_index == 2:
				s = self.grid.cells[new_row][new_column]
			elif offset_index == 3:
				w = self.grid.cells[new_row][new_column]
			offset_index += 1
			

		cneswc = '' + str(c) + str(n) + str(e) + str(s) + str(w)
		ceswnc = '' + str(c) + str(e) + str(s) + str(w) + str(n)
		cswnec = '' + str(c) + str(s) + str(w) + str(n) + str(e)
		cwnesc = '' + str(c) + str(w) + str(n) + str(e) + str(s)

		rule_list = langston_cneswc.langston_cnewsc()

		for rule in rule_list:
			if rule == cneswc or rule == ceswnc or rule == cswnec or rule == cwnesc:
				return int(rule_list[rule])

		return c
		

	def update(self):
		if self.is_running():
			for row in range(self.rows):
				for column in range(self.columns):
					next_state = self.cneswc(self.grid, row, column)
					if next_state != 0:
						print(str(next_state) + '\n')
					self.temp_grid.cells[row][column] = next_state

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

	def place_loop(self, row, column):
		original_column = column
		r_index = row
		c_index = original_column
		pattern = langston_loops_patterns.standard()
		for x in pattern:
			for y in x:
				self.grid.cells[r_index][c_index] = int(y)
				c_index += 1
			c_index = original_column
			r_index += 1

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