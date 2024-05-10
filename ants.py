from grid import Grid

class Ants:
	def __init__(self, width, height, cell_size):
		self.grid = Grid(width, height, cell_size)
		self.temp_grid = Grid(width, height, cell_size)
		self.rows = height // cell_size
		self.columns = width // cell_size
		self.run = False
		self.rule_list = ["Langston's"]
		self.rule_index = 0
		self.ant_placed = False
		self.ant_location = []
		self.direction_selection = False
		self.direction = ''
		self.cell_under_ant = 0

	def draw(self, window):
		self.grid.draw(window)

	def update(self):
		if self.is_running():

			# if ant is on a black cell
			if self.cell_under_ant == 0:

				# if ant is facing right
				if self.direction == '+x':
					self.cell_under_ant = self.grid.cells[self.ant_location[0]-1][self.ant_location[1]]
					self.grid.cells[self.ant_location[0]-1][self.ant_location[1]] = 'ANT'
					self.grid.cells[self.ant_location[0]][self.ant_location[1]] = 'WHITE'
					self.ant_location = [self.ant_location[0]-1, self.ant_location[1]]
					self.direction = '-y'

				# if ant is facing left
				elif self.direction == '-x':
					self.cell_under_ant = self.grid.cells[self.ant_location[0]+1][self.ant_location[1]]
					self.grid.cells[self.ant_location[0]+1][self.ant_location[1]] = 'ANT'
					self.grid.cells[self.ant_location[0]][self.ant_location[1]] = 'WHITE'
					self.ant_location = [self.ant_location[0]+1, self.ant_location[1]]
					self.direction = '+y'

				# if ant is facing up
				elif self.direction == '-y':
					self.cell_under_ant = self.grid.cells[self.ant_location[0]][self.ant_location[1]-1]
					self.grid.cells[self.ant_location[0]][self.ant_location[1]-1] = 'ANT'
					self.grid.cells[self.ant_location[0]][self.ant_location[1]] = 'WHITE'
					self.ant_location = [self.ant_location[0], self.ant_location[1]-1]
					self.direction = '-x'

				# if ant is facing right
				elif self.direction == '+y':
					self.cell_under_ant = self.grid.cells[self.ant_location[0]][self.ant_location[1]+1]
					self.grid.cells[self.ant_location[0]][self.ant_location[1]+1] = 'ANT'
					self.grid.cells[self.ant_location[0]][self.ant_location[1]] = 'WHITE'
					self.ant_location = [self.ant_location[0], self.ant_location[1]+1]
					self.direction = '+x'

			# if ant is on a white cell
			else:

				# if ant is facing right
				if self.direction == '+x':
					self.cell_under_ant = self.grid.cells[self.ant_location[0]+1][self.ant_location[1]]
					self.grid.cells[self.ant_location[0]+1][self.ant_location[1]] = 'ANT'
					self.grid.cells[self.ant_location[0]][self.ant_location[1]] = 0
					self.ant_location = [self.ant_location[0]+1, self.ant_location[1]]
					self.direction = '+y'

				# if ant is facing left
				elif self.direction == '-x':
					self.cell_under_ant = self.grid.cells[self.ant_location[0]-1][self.ant_location[1]]
					self.grid.cells[self.ant_location[0]-1][self.ant_location[1]] = 'ANT'
					self.grid.cells[self.ant_location[0]][self.ant_location[1]] = 0
					self.ant_location = [self.ant_location[0]-1, self.ant_location[1]]
					self.direction = '-y'

				# if ant is facing up
				elif self.direction == '-y':
					self.cell_under_ant = self.grid.cells[self.ant_location[0]][self.ant_location[1]+1]
					self.grid.cells[self.ant_location[0]][self.ant_location[1]+1] = 'ANT'
					self.grid.cells[self.ant_location[0]][self.ant_location[1]] = 0
					self.ant_location = [self.ant_location[0], self.ant_location[1]+1]
					self.direction = '+x'

				# if ant is facing right
				elif self.direction == '+y':
					self.cell_under_ant = self.grid.cells[self.ant_location[0]][self.ant_location[1]-1]
					self.grid.cells[self.ant_location[0]][self.ant_location[1]-1] = 'ANT'
					self.grid.cells[self.ant_location[0]][self.ant_location[1]] = 0
					self.ant_location = [self.ant_location[0], self.ant_location[1]-1]
					self.direction = '-x'



	def is_running(self):
		return self.run

	def start(self):
		self.run = True

	def stop(self):
		self.run = False

	def clear(self):
		if self.is_running() == False:
			self.grid.clear()

	# change to randomly placing an ant and assigning start direction
	def create_random_state(self):
		pass

	def clear_select_cells(self):
		self.direction_selection = False
		self.grid.cells[self.ant_location[0]+1][self.ant_location[1]] = 0
		self.grid.cells[self.ant_location[0]-1][self.ant_location[1]] = 0
		self.grid.cells[self.ant_location[0]][self.ant_location[1]+1] = 0
		self.grid.cells[self.ant_location[0]][self.ant_location[1]-1] = 0

	# place an ant and pick a starting direction
	def place_ant(self, row, column):
		if self.is_running() == False:
			if self.ant_placed == False:
				self.ant_location = [row, column]
				self.cell_under_ant = self.grid.cells[row][column]
				self.grid.cells[row][column] = 'ANT'
				self.grid.cells[row+1][column] = 'SELECT'
				self.grid.cells[row-1][column] = 'SELECT'
				self.grid.cells[row][column+1] = 'SELECT'
				self.grid.cells[row][column-1] = 'SELECT'
				self.ant_placed = True
				self.direction_selection = True
			else:
				if self.direction_selection == True:
					if row == self.ant_location[0]+1:
						self.direction = '-x'
						self.clear_select_cells()
					elif column == self.ant_location[1]-1:
						self.direction = '-y'
						self.clear_select_cells()
					elif column == self.ant_location[1]+1: 
						self.direction = '+y'
						self.clear_select_cells()
					elif row == self.ant_location[0]-1:
						self.direction = '+x'
						self.direction_selection = False
						self.clear_select_cells()
					else:
						self.clear_select_cells()
						self.grid.cells[self.ant_location[0]][self.ant_location[1]] = 0
						self.ant_location = [row, column]
						self.grid.cells[row][column] = 'ANT'
						self.grid.cells[row+1][column] = 'SELECT'
						self.grid.cells[row-1][column] = 'SELECT'
						self.grid.cells[row][column+1] = 'SELECT'
						self.grid.cells[row][column-1] = 'SELECT'
						self.ant_placed = True
						self.direction_selection = True
				else:
					self.clear_select_cells()
					self.grid.cells[self.ant_location[0]][self.ant_location[1]] = 0
					self.ant_location = [row, column]
					self.cell_under_ant = self.grid.cells[row][column]
					self.grid.cells[row][column] = 'ANT'
					self.grid.cells[row+1][column] = 'SELECT'
					self.grid.cells[row-1][column] = 'SELECT'
					self.grid.cells[row][column+1] = 'SELECT'
					self.grid.cells[row][column-1] = 'SELECT'
					self.ant_placed = True
					self.direction_selection = True


	# change to ant variations
	def rule_down(self):
		if self.is_running() == False:
			if self.rule_index < len(self.rule_list) - 1:
				self.rule_index += 1
			else:
				self.rule_index = 0

	# change to ant variations
	def rule_up(self):
		if self.is_running() == False:
			if self.rule_index > 0:
				self.rule_index -= 1
			else:
				self.rule_index = len(self.rule_list) - 1